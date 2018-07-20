import cv2
import numpy as np 
import os
import shutil

path= 'F:\\Dev\\MLprojects\\New folder'
src_files= os.listdir(path)
num=1
for files in src_files:
	src_file= os.path.join(path,files)
	x= files.split('-')[-2]
	dest_file= f'F:\\Dev\\MLprojects\\test_dir\\{x}\\{files}'
	shutil.move(src_file, dest_file)
	print(num)
	num+=1