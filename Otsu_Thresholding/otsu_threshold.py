# Python Program To Apply Otsu Thresholding Using OpenCV
# Author:- Ajinkya Patil
# Github:- https://github.com/Ajinkya7poppyi/

import cv2

#Path of image file to be read
image_read_path="H:/MyVisionRoom/img.jpg"

#Window Name
window_name="Input Image"

#Window Name
window_thresh_name="Thresh Image"

#Window Name
window_otsu_name="Otsu Image"

#Window Name
window_blur_otsu_name="Otsu Blur Image"

#Time to waitfor
wait_time=0

#Threshodl value
threshold = 127 

#Maximum value of intensity in image
maxval = 255

#Default Block size of gaussian filter
blockSize = 5

#Binary threshold type
globalThresholdType = cv2.THRESH_BINARY

#Otsu threshold type
otsuThresholdType = cv2.THRESH_OTSU

#Standard deviation for gaussian filter
gaussianStdDeviation = 0

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
	
	print ("Hello, Welcome To Otsu Threshold Operations")
	#Get the image dimesion in a tuple
	img_dimension= input_img.shape
	
	if img_dimension > 2:
		img_gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
	else:
		img_gray = input_img
		
	#retval, dst = cv2.threshold(src, thresh, maxval, type[, dst])
	#src: source input image
	#thresh: threshold value
	#maxval: maximum value that image can have
	#type: type of thresholding
	#dst: output image
	#retval: threshold value
	#Alternative Method
	#threshold_img = None
	#cv2.threshold(input_img, threshold, maxval, threshold_type, threshold_img)
	ret, img_global_thresh = cv2.threshold(img_gray, threshold, maxval, globalThresholdType)
	ret, img_otsu_thresh = cv2.threshold(img_gray, threshold, maxval, globalThresholdType + otsuThresholdType)
	
	#Otsu's thresholding after Gaussian filtering
	#Gaussian filter is highly effective in removing gaussian noise
	#dst = cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])
	#src: source input image
	#ksize: Gaussian kernel size
	#sigmaX: Gaussian kernel standard deviation in X direction
	#sigmaY: Gaussian kernel standard deviation in Y direction
	#if sigmaY is zero, it is set to be equal to sigmaX, if both sigmas are zeros, they are computed from ksize.width and ksize.height , respectively
	#borderType: Pixel extrapolation method
	#dst: output image
	img_blur = cv2.GaussianBlur(img_gray,(blockSize, blockSize), gaussianStdDeviation)
	ret, img_blur_otsu_thresh = cv2.threshold(img_blur, threshold, maxval, globalThresholdType + otsuThresholdType)
		
	#Create a Window
	#cv2.WINDOW_NORMAL = Enables window to resize.
	#cv2.WINDOW_AUTOSIZE = Default flag. Auto resizes window size to fit an image.
	cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
	
	#Show image in window
	cv2.imshow(window_name,input_img)
	#Wait untill user enter any key
	cv2.waitKey(wait_time)
	#Show image in window
	cv2.imshow(window_thresh_name,img_global_thresh)
	#Wait untill user enter any key
	cv2.waitKey(wait_time)
	#Show image in window
	cv2.imshow(window_otsu_name,img_otsu_thresh)
	#Wait untill user enter any key
	cv2.waitKey(wait_time)
	#Show image in window
	cv2.imshow(window_blur_otsu_name,img_blur_otsu_thresh)
	#Wait untill user enter any key
	cv2.waitKey(wait_time)
	#Destroy All Window
	cv2.destroyAllWindows()
	
else:
	print ("Please Check The Path of Input File")
