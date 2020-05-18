# Python Program To Apply Binary Thresholding Using OpenCV
# Author:- Ajinkya Patil
# Github:- https://github.com/Ajinkya7poppyi/

import cv2
	
#Path of image file to be read
image_read_path="H:/MyVisionRoom/input.jpg"

#Window Name
window_name="Input Image"

#Window Name
window_threshold_name="Threshold Image"

#Time to waitfor
wait_time=0

#Maximum value of intensity in image
maxval = 255

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
	
	print ("Hello, Welcome To Threshold Operations")
	#Get the image dimesion in a tuple
	img_dimension= input_img.shape
	
	if img_dimension > 2:
		img_gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
	else:
		img_gray = input_img
	
	#Loop Forever
	while True:
		#Ask User to choose operation
		print ("Choose Your Operation:")
		print ("1. Threshold Binary")
		print ("2. Threshold Binary Inverted")
		print ("3. Truncate")
		print ("4. Threshold To Zero")
		print ("5. Threshold To Zero Inverted")
		print ("6. Exit")
		choice = None	
		#Loops untill user enters valid number
		while True:
			try:
				choice = int(input("Your Option: "))
				if  0 < choice < 7:
					break
				raise StandardError()	
			except:
				print("Please Enter Valid Number")		
		
		#Exit from the while loop
		if choice == 6:
			break
		
		#Get Threshold from user	
		threshold = None
		#Loops untill user enters valid number
		while True:
			try:
				threshold = int(input("Enter Threshold:"))
				break
			except:
				print("Please Enter Valid Number")
		
		#if user choose to get value
		if choice == 1:
			threshold_type = cv2.THRESH_BINARY
		
		#if user choose to set value
		elif choice == 2:
			threshold_type = cv2.THRESH_BINARY_INV
		
		#if user choose to set value
		elif choice == 3:
			threshold_type = cv2.THRESH_TRUNC
			
		#if user choose to set value
		elif choice == 4:
			threshold_type = cv2.THRESH_TOZERO

		#if user choose to set value
		elif choice == 5:
			threshold_type = cv2.THRESH_TOZERO_INV
			
		#retval, dst = cv2.threshold(src, thresh, maxval, type[, dst])
		#src: source input image
		#thresh: threshold value
		#maxval: maximum value that image can have
		#type: type of thresholding
		#dst: output image
		#retval: threshold value
		ret, threshold_img = cv2.threshold(img_gray, threshold, maxval, threshold_type)
		#threshold_img = None
		#cv2.threshold(input_img, threshold, maxval, threshold_type, threshold_img)
		#Create a Window
		cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
		#Show image in window
		cv2.imshow(window_name,img_gray)
		#Create a Window
		cv2.namedWindow(window_threshold_name,cv2.WINDOW_NORMAL)
		#Show image in window
		cv2.imshow(window_threshold_name,threshold_img)
		#Wait untill user enter any key
		cv2.waitKey(wait_time)  
		#Destroy All Window
		cv2.destroyAllWindows()
			
else:
	print ("Please Check The Path of Input File")