import cv2
import numpy as np 
import os

for i in range(200):
	path=f"F:\\Dev\\MLprojects\\Automatic_Checker_System\\{i+1}"
	src_files = os.listdir(path)
	num=1
	for file in src_files:
		filename= os.path.join(path,file)
		img = cv2.imread(filename)
		
		flip_img = cv2.flip(img,1)
		string = f"{i+1}-" + str(num+14)+ '.jpg'
		cv2.imwrite(f"F:\\Dev\\MLprojects\\Automatic_Checker_System\\{i+1}\\{string}",flip_img)
		num+=1



