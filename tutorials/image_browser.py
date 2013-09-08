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

		self.images = load_image_files(find_image_files(self.path_))
		self.num_imgages = len(self.images)
		self.img_indx = 0		
		self.cam = Camera('PERSPECTIVE')
		pass

	def initGL(self):

		"""Overloaded function from GLWidget
		"""

		self.quad = Quad(0, 0, self.width_, self.height_, self.images[self.img_indx], 'PIL')		
		# self.rect = Rectangle(-0.5,-0.5,0,1,1)
		self.cam.on()
		pass

	def paint(self):

		"""Overloaded function from GLWidget
		"""

		self.quad.draw()
		# self.rect.render()
		pass

	def next_image(self):

		"""Signal to show next image
		"""

		self.img_indx = (self.img_indx + 1) % self.num_imgages
		self.quad.load_texture(self.images[self.img_indx], 'PIL')
		self.update_widget()
		pass

	def prev_image(self):

		"""Signal to show previous image
		"""

		self.img_indx = (self.img_indx - 1) % self.num_imgages
		self.quad.load_texture(self.images[self.img_indx], 'PIL')
		self.update_widget()
		pass	