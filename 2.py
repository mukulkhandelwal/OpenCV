#Loading Video Files

import cv2
import numpy as numpy

cap = cv2.VideoCapture(0) #1,2
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc,20.0,(640,480))


print(cap.isOpened())
	
while True :
	ret, frame = cap.read()
	
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	out.write(frame)	
	cv2.imshow('frame',frame)
	#cv2.imshow('gray',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
out.release()  #save file
cv2.destroyAllWindows()
