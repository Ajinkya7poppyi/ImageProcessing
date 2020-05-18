# Python Program To Add Border To Image Using OpenCV
# Author:- Ajinkya Patil
# Github:- https://github.com/Ajinkya7poppyi/

import cv2
import numpy as np
	
#Path of image file to be read
image_read_path="H:/input.jpg"

#Window Name
window_name="Input Image"

#Border Window Name
window_border_name="Bordered Image"

#Time to waitfor
wait_time=0

#Load an image
#cv2.IMREAD_COLOR = Default flag for imread. Loads color image.
#cv2.IMREAD_GRAYSCALE = Loads image as grayscale.
#cv2.IMREAD_UNCHANGED = Loads image which have alpha channels.
#cv2.IMREAD_ANYCOLOR = Loads image in any possible format
#cv2.IMREAD_ANYDEPTH = Loads image in 16-bit/32-bit otherwise converts it to 8-bit
input_img = cv2.imread(image_read_path,cv2.IMREAD_UNCHANGED)

#Check if image is loaded 
if input_img is not None:
	#Create a Window
	#cv2.WINDOW_NORMAL = Enables window to resize.
	#cv2.WINDOW_AUTOSIZE = Default flag. Auto resizes window size to fit an image.
	cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
	#Show image in window
	cv2.imshow(window_name,input_img)
	#Wait untill user enter any key
	cv2.waitKey(wait_time)
	#Destroy Window
	cv2.destroyWindow(window_name)
	
	print ("Hello, Welcome To Border Padding")
	#Get the image dimesion in a tuple
	img_dimension= input_img.shape
	
	print ("Input image is " + str(len(img_dimension)) + " dimesional") 
	print ("Input Image rows: " + str(img_dimension[0]) + " cols: " + str(img_dimension[1]))

	#Get left border width from user	
	left = None
	#Loops untill user enters valid number
	while True:
		try:
			left = int(input("Enter Left Border Width:"))
			break
		except:
			print("Please Enter Valid Number")
		
	#Get right border width from user	
	right = None
	#Loops untill user enters valid number
	while True:
		try:
			right = int(input("Enter Right Border Width:"))
			break
		except:
			print("Please Enter Valid Number")

	#Get Top border width from user	
	top = None
	#Loops untill user enters valid number
	while True:
		try:
			top = int(input("Enter Top Border Width:"))
			break
		except:
			print("Please Enter Valid Number")

	#Get Bottom border width from user	
	bottom = None
	#Loops untill user enters valid number
	while True:
		try:
			bottom = int(input("Enter Bottom Border Width:"))
			break
		except:
			print("Please Enter Valid Number")				
				
	#Loop Forever
	while True:
		#Ask User to choose Border
		print ("Choose Your Border:")
		print ("1. Replicate")
		print ("2. Reflect")
		print ("3. Reflect101")
		print ("4. Wrap")
		print ("5. Constant")
		print ("6. Exit")
		choice = None	
		#Loops untill user enters valid number
		while True:
			try:
				choice = int(input("Your Option: "))
				break
			except:
				print("Please Enter Valid Option")		
		
		#Exit from the while loop
		if choice == 6:
			break
			
		#if user choose to get value
		elif choice == 1:
			border = cv2.BORDER_REPLICATE
			
		#if user choose to get value
		elif choice == 2:
			border = cv2.BORDER_REFLECT

		#if user choose to get value
		elif choice == 3:
			border = cv2.BORDER_REFLECT_101

		#if user choose to get value
		elif choice == 4:
			border = cv2.BORDER_WRAP

		#if user choose to get value
		elif choice == 5:
			border = cv2.BORDER_CONSTANT
			
		else:
			print ("Please Select A Valid Operation")
			continue

		#Various border types, image boundaries are denoted with '|'
		# BORDER_REPLICATE:     aaaaaa|abcdefgh|hhhhhhh
		# BORDER_REFLECT:       fedcba|abcdefgh|hgfedcb
		# BORDER_REFLECT_101:   gfedcb|abcdefgh|gfedcba
		# BORDER_WRAP:          cdefgh|abcdefgh|abcdefg
		# BORDER_CONSTANT:      iiiiii|abcdefgh|iiiiiii  with some specified 'i'	
		# BORDER_COLOR:			color of the border for BORDER_CONSTANT
		BORDER_COLOR = [255,255,255]
		border_img = cv2.copyMakeBorder(input_img, top, bottom, left, right, border, value=BORDER_COLOR)
		
		#Create a Window
		cv2.namedWindow(window_border_name,cv2.WINDOW_NORMAL)
		#Show image in window
		cv2.imshow(window_border_name,border_img)
		#Wait untill user enter any key
		cv2.waitKey(wait_time)  
		#Destroy Window
		cv2.destroyWindow(window_border_name)
			
else:
	print ("Please Check The Path of Input File")
