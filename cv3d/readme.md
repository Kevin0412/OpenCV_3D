# 1.import
from cv3d import IIID,IIID2

# 2.create a new list
objects=[]

# 3.append objects
objects.append([(0,0,0),(600,0,0),(0,0,255),1,8,'line'])
such as:
[(0,0,0),(600,0,0),(0,0,255),1,8,'line'] means a line starts (0,0,0),ends (600,0,0),color BGR(0,0,255) is red,thickness 1,lineType 8;
[(20,10,30),(255,0,0),10,1,'ring'] means a ring centers (20,10,30),color BGR(255,0,0) is blue,radius 10,thickness 1;
[(50,20,40),(0,255,0),10,1,'sphere'] means a sphere centers (50,20,40),color BGR(0,255,0) is green,radius 10,thickness 1(not supported in overall view).

# 4.show
orthogonality or perspectivity:
IIID.show(objects,(0,0,0),1280,720,[120,-15,1,0,-1],(1,0))
#show all elements in list 'object',rotating center (0,0,0),frame size 1280x720,the first and second ones of the list are azimuth,the third and fourth ones of the list are rotating speed,the last one of the list means mode,mode -1 directly shows the objects,mode 0 returns the frame,mode 1 returns the azmuth,the tuple means the way of show:(1,0) means orthogonality,frame ratio is 1;(495,330) means perspectivity,distance between the observer and rotating center is 495,frame ratio of the objects whose distance to the observer is 330 is 1.
#The way to change the azimuth in mode -1 is pressing w,a,s,d.And rotating speed means the speed of changing the azimuth.Press ESC to exit.

overall view:
IIID2.show(objects,(0,0,0),3840,1920)
#show all objects in list 'object',observer at (0,0,0),frame size 3840x1920.It returns the frame.


# 一、导入
from cv3d import IIID,IIID2

# 二、创建一个新列表
objects=[]

# 三、添加物体
objects.append([(0,0,0),(600,0,0),(0,0,255),1,8,'line'])
例如:
[(0,0,0),(600,0,0),(0,0,255),1,8,'line']表示一条以(0,0,0)为起点，(600,0,0)为中点，颜色BGR(0,0,255)即红色，粗细为1，直线类型为8的直线；
[(20,10,30),(255,0,0),10,1,'ring']表示一个以(20,10,30)为圆心，颜色BGR(255,0,0)即蓝色，半径为10，粗细为1的圆环；
[(50,20,40),(0,255,0),10,1,'sphere']表示一个以(50,20,40)为圆心，颜色BGR(0,255,0)即绿色，半径为10，粗细为1的球体（全景暂不支持）。

# 四、展示
正交或透视：
IIID.show(objects,(0,0,0),1280,720,[120,-15,1,0,-1],(1,0))
#展示列表'objects'中所有元素，旋转中心(0,0,0)，图像大小1280x720，列表中第一、二个参数表示方位角，第三、四个参数表示旋转速度，最后一个参数表示模式，模式-1为直接展示，模式0返回图像，模式1返回方位角，元组表示渲染方式：(1,0)表示正交渲染，画面比例为1；(495,330)表示透视渲染，观察者与旋转中心的距离为495，距观察者330的物体在画面中的比例为1。
#在模式-1中，按w,a,s,d改变方向角。旋转速度就是这里的改变方向角的速度。按ESC退出。

全景：
IIID2.show(objects,(0,0,0),3840,1920)
#展示列表'objects'中所有元素，观察者在(0,0,0)处，图像大小3840x1920，返回的是图像。