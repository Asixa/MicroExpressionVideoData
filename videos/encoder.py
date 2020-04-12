import cv2
import numpy as np



def downscale(name,downscale):
    cap = cv2.VideoCapture(name+'full.mp4')
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # float
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # float
    fps = int(cap.get(cv2.CAP_PROP_FPS)) # float
    w=int(width*downscale)
    h=int(height*downscale)
    fourcc = cv2.VideoWriter_fourcc(*'mp42')
    out = cv2.VideoWriter(name+str(downscale)+'.mp4',fourcc, fps, (w,h))
    
    while True:
        ret, frame = cap.read()
        if ret == True:
            b = cv2.resize(frame,(w,h),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
            out.write(b)
        else:
            break
        
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def downscaleAllResolution(name):
    downscale(name,0.5)
    downscale(name,0.25)
    downscale(name,0.125)
    downscale(name,0.0625)
    downscale(name,0.03125)


downscaleAllResolution("metv-con-2/")
downscaleAllResolution("metv-con-3/")
downscaleAllResolution("metv-hap-1/")
downscaleAllResolution("metv-neu-1/")
downscaleAllResolution("metv-sad-1/")
downscaleAllResolution("metv-sad-2/")
downscaleAllResolution("metv-sad-3/")
downscaleAllResolution("metv-sad-4/")