from cv3d import IIID,IIID2
import cv2
import numpy as np
video=cv2.VideoWriter('1.mp4',cv2.VideoWriter_fourcc('H','2','6','5'),30,(1280,720))
x=20#x方向振幅
y=20#y方向振幅
object2=[]
for t in range(60):
    tx=t/30*np.pi
    ty=t/15*np.pi
    objects=[]
    objects.append([(np.sin(tx)*x,np.sin(ty)*y,-200),(np.sin(tx)*x*3/4,0,-100),(0,0,255),2,8,'line'])
    objects.append([(np.sin(tx)*x*3/4,0,-100),(0,150,200),(0,0,255),2,8,'line'])
    objects.append([(np.sin(tx)*x*3/4,0,-100),(0,-150,200),(0,0,255),2,8,'line'])
    objects.append([(np.sin(tx)*x,np.sin(ty)*y,-200),(0,255,0),20,-1,'sphere'])
    objects.append([(0,200,200),(0,-200,200),(255,0,0),4,8,'line'])
    objects.append([(np.sin(tx)*x,np.sin(ty)*y,-200),(0,255,0),1,-1,'sphere'])
    img=IIID.show(objects,(0,0,0),1280,720,[45,35,1,0,0],(1,0))
    video.write(img)
video.release()
img=IIID.show(object2,(0,0,-200),1280,720,[45,35,1,0,-1],(1,0))
s
