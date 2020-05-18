# Python Program To Read/Write a Video Using OpenCV
# Author:- Ajinkya Patil
# Github:- https://github.com/Ajinkya7poppyi/

import cv2

#Path of video file to be read
video_read_path='H:/Python/abc.avi'

#Path of video file to be written
video_write_path='H:/abc.mp4'

#Window Name
window_name='Input Video'

#Escape ASCII Keycode
esc_keycode=27

#Create an object of VideoCapture class to read video file
video_read = cv2.VideoCapture(video_read_path)
# Check if video file is loaded successfully
if (video_read.isOpened()== True): 
	#Frames per second in videofile. get method in VideoCapture class.
	fps = video_read.get(cv2.CAP_PROP_FPS)
	#Width and height of frames in video file
	size = (int(video_read.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video_read.get(cv2.CAP_PROP_FRAME_HEIGHT)))
	#Create an object of VideoWriter class to write video file.   
	#cv2.CV_FOURCC('I','4','2','0') = uncompressed YUV, 4:2:0 chroma subsampled. (.avi)
	#cv2.CV_FOURCC('P','I','M','1') = MPEG-1(.avi)
	#cv2.CV_FOURCC('M','J','P','G') = motion-JPEG(.avi)
	#cv2.CV_FOURCC('T','H','E','O') = Ogg-Vorbis(.ogv)
	#cv2.CV_FOURCC('F','L','V','1') = Flash video (.flv)
	#cv2.CV_FOURCC('M','P','4','V') = MPEG encoding (.mp4)
	#Also this form is too valid cv2.VideoWriter_fourcc(*'MJPG')
	#video_write = cv2.VideoWriter(video_write_path, cv2.VideoWriter_fourcc('M','P','4','V'), fps, size)
	video_write = cv2.VideoWriter(video_write_path, cv2.VideoWriter_fourcc(*'MP4V'), fps, size)
	#Set display frame rate
	display_rate = (int) (1/fps * 1000)
	#Create a Window
	#cv2.WINDOW_NORMAL = Enables window to resize.
	#cv2.WINDOW_AUTOSIZE = Default flag. Auto resizes window size to fit an image.
	cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
	#Read first frame from video. Return Boolean value if it succesfully reads the frame in state and captured frame in cap_frame  
	state, cap_frame = video_read.read()
	#Loop untill all frames from video file are read
	while state:
		# Display frame
		cv2.imshow(window_name,cap_frame) 
		#Write method from VideoWriter. This writes frame to video file
		video_write.write(cap_frame)
		#Read next frame from video 
		state, cap_frame = video_read.read()
		#Check if any key is pressed. 
		k = cv2.waitKey(display_rate)
		#Check if ESC key is pressed. ASCII Keycode of ESC=27
		if k == esc_keycode:  
			#Destroy Window
			cv2.destroyWindow(window_name)
			break	
	#Closes Video file	
	video_read.release()
	video_write.release()
else:
	print("Error opening video stream or file")