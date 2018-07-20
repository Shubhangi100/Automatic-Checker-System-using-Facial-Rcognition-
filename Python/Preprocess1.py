import cv2
import os
import numpy as np 

## Calculate the coordinates for cropping the image
x=105
y=20
w=420
h=400

for i in range(200):
	path=f"F:\\Dev\\MLprojects\\Automatic_Checker_System\\{i+1}"
	src_files = os.listdir(path)

	for file in src_files:
		full_file_name = os.path.join(path, file)
		img= cv2.imread(full_file_name)

		img_c= img[y:y+h,x:x+w]

		cv2.imwrite(full_file_name,img_c)


	







