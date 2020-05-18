# Python Program To Read/Write an Image Using OpenCV
# Author:- Ajinkya Patil
# Github:- https://github.com/Ajinkya7poppyi/

import cv2

#Path of image file to be read
image_read_path='H:/input.jpg'

#Path of image file to be written
image_write_path='H:/output.jpg'

#Window Name
window_name='Input Image'

#Escape ASCII Keycode
esc_keycode=27

#Key for which to waitfor
save_key='s'

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
	#Check if any key is pressed
	k = cv2.waitKey(wait_time)
	#Check if ESC key is pressed. ASCII Keycode of ESC=27
	if k == esc_keycode:  
		#Destroy Window
		cv2.destroyWindow(window_name)
	#check if s key is pressed. 	
	elif k == ord(save_key): 
		#Write image to filepath
		cv2.imwrite(image_write_path,input_img)
		cv2.destroyWindow(window_name)
else:
	print 'Please Check The Path of Input File'