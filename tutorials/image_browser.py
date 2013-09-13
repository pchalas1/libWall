#!/usr/bin/env python

from wall import *

class ImageBrowser(GLWidget):

	"""	@author Preetham Chalasani
	@brief Simple Image browser application
	"""

	def __init__(self, path, width, height, parent = None):

		"""@param path : Path to a folder
		@param width : Width of the Screen
		@param height : Height of the Screen
		"""

		super(ImageBrowser, self).__init__(parent = parent)

		self.path_ = path
		self.width_ = width
		self.height_ = height

		# Load images from the directory specified
		self.images = load_image_files(find_image_files(self.path_))
		self.num_imgages = len(self.images)
		self.img_indx = 0		

		# Set the camera to Perspective view
		self.cam = Camera('PERSPECTIVE')
		pass

	def initGL(self):

		"""Overloaded function from GLWidget
		"""

		# Create a quad of a specific width and height on which the image has to 
		# be rendered. Also specify the image name and type of image format.
		self.quad = Quad(0, 0, self.width_, self.height_, self.images[self.img_indx], 'PIL')				

		# Switch on the camera to view the scene
		# Default camera parameters will be used if no specific parameters are defined
		self.cam.on()
		pass

	def paint(self):

		"""Overloaded function from GLWidget
		"""

		# Draw the quad with previously defined parameters.
		self.quad.draw()
		
		pass

	def next_image(self):

		"""Signal to show next image
		"""

		# Keeping track of image number in the directory
		self.img_indx = (self.img_indx + 1) % self.num_imgages

		# Load the corresonding texture
		self.quad.load_texture(self.images[self.img_indx], 'PIL')

		# Update the widget, which basically is a call to pain function
		self.update_widget()
		pass

	def prev_image(self):

		"""Signal to show previous image
		"""

		# Keeping track of image number in the directory
		self.img_indx = (self.img_indx - 1) % self.num_imgages

		# Load the corresonding texture
		self.quad.load_texture(self.images[self.img_indx], 'PIL')

		# Update the widget, which basically is a call to pain function
		self.update_widget()
		pass	