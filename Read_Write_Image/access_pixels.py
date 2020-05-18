# Python Program To Access Pixels Using OpenCV
# Author:- Ajinkya Patil
# Github:- https://github.com/Ajinkya7poppyi/

import cv2

#Get pixel value at location
def get_pixel(row, col, index):
	#Check if image is 3-dimensional
	if index is not None:
		#Access value at input_img(row,col) in index space
		value = input_img[row, col, index]
	else:
		#Access value at input_img(row,col)
		value = input_img[row, col]
	
	return value	
	
#Set pixel value at location	
def set_pixel(row, col, index, value):
	#Check if image is 3-dimensional
	if index is not None:
		#Pass value to input_img(row,col) in index space
		input_img[row, col, index] = value
	else:
		#Pass value to input_img(row,col)
		input_img[row, col] = value
	
#Path of image file to be read
image_read_path="H:/img.jpg"

#Window Name
window_name="Input Image"

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
	
	print ("Hello, Welcome To Pixel Operations")
	#Get the image dimesion in a tuple
	img_dimension= input_img.shape
	
	print ("Input image is " + str(len(img_dimension)) + " dimesional") 
	print ("Input Image rows: " + str(img_dimension[0]) + " cols: " + str(img_dimension[1]))
	
	#Loop Forever
	while True:
		#Ask User to choose operation
		print ("Choose Your Operation:")
		print ("1. Get Pixel")
		print ("2. Set Pixel")
		print ("3. Exit")
		choice = None	
		#Loops untill user enters valid number
		while True:
			try:
				choice = int(input("Your Option: "))
				break
			except:
				print("Please Enter Valid Number")		
		
		#Exit from the while loop
		if choice == 3:
			break
		
		#Get data from user if valid operations
		if choice == 1 or choice == 2:
			#Get row from user	
			row = None
			#Loops untill user enters valid number
			while True:
				try:
					row = int(input("Enter Row:"))
					break
				except:
					print("Please Enter Valid Number")
		
			#if user input is greater than actual rows set it to max rows value
			if row >= img_dimension[0]:
				row = img_dimension[0]-1
		
			#Get col from user
			col = None
			#Loops untill user enters valid number
			while True:
				try:
					row = int(input("Enter Column:"))
					break
				except:
					print("Please Enter Valid Number")
			#if user input is greater than actual cols set it to max cols value
			if col >= img_dimension[1]:
				col = img_dimension[1]-1
		
			#Set indx to None considering 2 dimensional image
			indx = None
	
			#If image has more than 2 dimensions
			if len(img_dimension) > 2:
				#Get index from user
				#Loops untill user enters valid number
				while True:
					try:
						indx = int(input("Enter Index:"))
						break
					except:
						print("Please Enter Valid Number")
				#if user input is greater than actual indices set it to max index value
				if indx >= img_dimension[2]:
					indx = img_dimension[2]-1
	
		#if user choose to get value
		if choice == 1:
			print ("Value is " + str(get_pixel(row, col, indx)))
		
		#if user choose to set value
		elif choice == 2:
			val = None
			#Get value to et from user
			#Loops untill user enters valid number
			while True:
				try:
					val = int(input("Enter Value:"))
					break
				except:
					print("Please Enter Valid Number")
			#call set_pixel function
			set_pixel(row, col, indx, val)
			#Create a Window
			cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
			#Show image in window
			cv2.imshow(window_name,input_img)
			#Wait untill user enter any key
			cv2.waitKey(wait_time)  
			#Destroy Window
			cv2.destroyWindow(window_name)
			
		else:
			print ("Please Select A Valid Operation")
else:
	print ("Please Check The Path of Input File")