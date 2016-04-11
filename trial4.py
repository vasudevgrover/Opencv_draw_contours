import cv2
import numpy as np
cap=cv2.VideoCapture(0)
param1=[250,250,250]
param2=[255,255,255]
img=np.zeros((480,640),np.uint8)
while(1):
    ret,frame=cap.read()
    lower=np.array(param1)
    upper=np.array(param2)
    mask=cv2.inRange(frame,lower,upper)
    contours,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    max_area = -1
    for i in range(len(contours)):
        cnt=contours[i]
        area = cv2.contourArea(cnt)
        if(area>max_area):
            max_area=area
            ci=i
    cnt=contours[ci]
    cv2.drawContours(frame,contours,ci,(0,255,0),3)
   
    M=cv2.moments(contours[ci])
    cx=int(M['m10']/M['m00'])
    cy=int(M['m01']/M['m00'])
    cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
    cv2.imshow("yo1",mask)
    cv2.imshow("yo",frame)
    if cv2.waitKey(1)==115:
        x=cx
        y=cy
        print "START"
    if cv2.waitKey(1)==101:
        print "oho"
        p=cx
        q=cy
        cv2.line(img,(x,y),(p,q),(255,255,255),3)
        
    cv2.imshow("made",img)    
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()

