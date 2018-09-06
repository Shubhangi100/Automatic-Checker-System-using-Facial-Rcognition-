## This script is used to crop out the facial portion in the training images

import cv2
import numpy as np 
import os


for i in range(1,200):
	
	path=f""
	src_files = os.listdir(path)
	num=1
	for file in src_files:
		full_file= os.path.join(path,file)
		webcam = cv2.VideoCapture(full_file) 

		classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
		classifier1 = cv2.CascadeClassifier('haarcascade_profileface.xml')

		while webcam.isOpened():
		    (rval, im) = webcam.read()
		    if rval== False:
		        break
		    
		    orig= im
		    faces= classifier.detectMultiScale(im)
		    faces1= classifier1.detectMultiScale(orig)
		    for (x,y,w,h) in faces:
		        sub_face= im[y:y+h, x:x+w]
		        string = f"{i+1}-" + str(num+28)+ '.jpg'
		        cv2.imwrite(f"",sub_face)
		        num+=1
		    
		    for (x,y,w,h) in faces1:
		        sub_face= im[y:y+h, x:x+w]
		        string = f"{i+1}-" + str(num+28)+ '.jpg'
		        cv2.imwrite(f"",sub_face)
		        num+=1		        

		



