import cv2
import numpy as np 
import os
 
path= 'F:\\Dev\\MLprojects\\Automatic_Checker_System\\checking'
src_files= os.listdir(path)
#for files in src_files:
#	full_path= os.path.join(path,files)
#	img= cv2.imread(full_path)
#	img1=files
#	img1= list(img1)
#	count= 'z'
#	for i in range(len(img1)):
#		if img1[i]=='a':
#			img1[i]= '-'
#			count='a'
#		elif img1[i]== 'b':
#			img1[i]= '-'
#			count='b'
#	if count=='a':
#		img1.insert(-4,'a')

#	if count== 'b':
#		img1.insert(-4,'b')
	
#	img1= "".join(img1)


#	cv2.imwrite(img1,img)

def adjust_gamma(image, gamma=1.0):

   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)

for files in src_files:
	full_name= os.path.join(path,files)  
	original = cv2.imread(full_name, 1)
	
	gamma = 0.3
	                                   # change the value here to get different result
	adjusted = adjust_gamma(original, gamma=gamma)
	files= list(files)
	files.insert(-5,'i')
	files= "".join(files)

	cv2.imwrite(files, adjusted)


