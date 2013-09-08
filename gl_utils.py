#!/usr/bin/env python

import os
import sys
import re
import rospy
import numpy
import cv
from PIL import Image
from PySide import QtGui, QtCore

def create_app(app_name, app_class, anonymous = True):	

	"""Create an application 
	@param app_name : Application Name
	@param app_class : Application Class Name ,e.g, widget class
	@param anonymous : True
	@return app : Applicaiotn handle
	@return app_canvas : Widget handle
	"""

	rospy.init_node(name, anonymous)
	
	app = QtGui.QApplication(sys.argv)
	
	app_canvas = app_class(app_name, app)

	return app, app_canvas

def log_info(msg):

	"""Print the message on the terminal
	@param msg : Any type of object
	"""

	rospy.loginfo(msg)
	pass

def log_warn(msg):

	"""Print a warning message on the terminal
	@param msg : Any type of object
	"""

	rospy.logwarn(msg)
	pass

def log_err(msg):

	"""Print an error message on the terminal
	@param msg : Any type of object 
	"""

	rospy.logerr(msg)
	pass

def create_signal():

	"""Create a Qt signal
	@return signal : QT Signal
	"""

	signal = QtCore.Signal()
	return signal


default_img_file_formats = ['.jpg', '.png', '.jpeg', '.bmp']

def add_file_format(format):

	"""Add an image format to the list from which a image has to be searched
	@param format : File format like .png, .jpg
	"""

	default_img_file_formats.append(format)
	pass

def find_image_files(path, formats = None):

	"""Search images in the path specified
	@param path : Directory to search
	@param formats : Image formats to search for
	@return file_locs : File names that match the format specified
	"""

	if formats == None:
		formats = default_img_file_formats

	files = os.listdir(path)

	file_regex = ''
	for ext in formats:
		file_regex += '.*' + ext + '|'

	file_locs = []
	for img in files:
		if re.match(file_regex, img):
			file_locs.append(path + img)

	return file_locs

def load_image_files(image_files):

	"""Load image files to an array format
	@param image_files : Image file names
	@return images : list of array
	"""

	images = []
	for img in image_files:
		tmp = Image.open(img)
		images.append(tmp)

	return images

def to_string(image):

	"""Convert image to String	
	"""

	return image.tostring('raw', 'RGBX', 0, -1)


def load_video(path):

	"""Load video from the path
	@param path : Location of the video file
	@return opencv video handle
	"""

	return cv.CaptureFromFile(path)

def get_next_frame(video):

	"""Captures next frame in the video
	@param video : opencv video handle
	"""

	image = cv.QueryFrame(video)
	cv.Flip(image, None, 0)
	# cv.CvtColor(image, image, cv.CV_BGR2RGB)
	image_arr = ipl2tex(image)

	return image_arr

def get_video_fps(video):

	"""Fps of the video
	@param video : opencv video handle
	"""

	return int(cv.GetCaptureProperty(video, cv.CV_CAP_PROP_FPS))

def ipl2tex(image):

	"""Convert image from ipl to tex format
	@param image : image in iple format
	@return outimage : Image in tex format
	"""

	depth2dtype = { 
		cv.IPL_DEPTH_8U: 	'uint8', 
		cv.IPL_DEPTH_8S: 	'int8', 
		cv.IPL_DEPTH_16U: 	'uint16', 
		cv.IPL_DEPTH_16S: 	'int16', 
		cv.IPL_DEPTH_32S: 	'int32', 
		cv.IPL_DEPTH_32F: 	'float32', 
		cv.IPL_DEPTH_64F: 	'float64', 
	} 
	arr_dtype = image.depth
	tex = numpy.fromstring(
		image.tostring(),
		dtype = depth2dtype[arr_dtype],
		count = image.width * image.height * image.nChannels
		)
	tex.shape = (image.height, image.width, image.nChannels)
	return tex


# class NonOverridable(type):
# 	def __new__(self, name, bases, dct):
# 		if bases and "roo" in dct:
# 			raise SyntaxError, "Overriding roo is not allowed"
# 		return type.__new__(self, name, bases, dct)
