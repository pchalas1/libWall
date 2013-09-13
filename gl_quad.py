#!/usr/bin/env python

### OpenGL Imports ###
from OpenGL.GL import *
from OpenGL.GLU import *

from gl_utils import *
import threading

class Quad(object):

	"""@author : Preetham Chalasani
	@brief To create a quad, which basically is a rectangle, but this quad class helps to load an image onto it.
	"""

	def __init__(self, x, y, width, height, image = None, img_type = None):
		super(Quad, self).__init__()

		self.__x = x
		self.__y = y
		self.__width = width
		self.__height = height

		self.__texture = 0		

		if image != None and img_type != None:
			self.__load_texture(image, img_type)

		self.__obj = self.__make_commandlist()
		pass

	def __make_commandlist(self):
		
		"""To make a commandlist which creates the quad with binded textur coordinates.
		"""

		gen_list = glGenLists(1)
		glNewList(gen_list, GL_COMPILE)							

		glBegin(GL_QUADS)
				
		glTexCoord3f(0.0, 0.0, 0.0)
		glVertex3f(-1, -1, 0.0)
		
		glTexCoord3f(1.0, 0.0, 0.0)
		glVertex3f(1, -1,0.0)


		glTexCoord3f(1.0, 1.0, 0.0)
		glVertex3f(1, 1, 0.0)

		glTexCoord3f(0.0, 1.0, 0.0)
		glVertex3f(-1,1, 0.0)

		glEnd()		

		glEndList()

		return gen_list

	def __load_texture(self, image, type):

		"""Load a texture(image) on to the quad.
		"""

		if type == 'PIL':
			self.__set_image_texture(image)
		elif type == 'IPL':
			self.__set_frame_texture(image)
		pass

	def __set_image_texture(self, image):

		"""Set texture 
		"""

		self.__texture_needed = True
		img_x = image.size[0]
		img_y = image.size[1]

		raw_image = to_string(image)
		glGenTextures(1, self.__texture)
		glBindTexture(GL_TEXTURE_2D, self.__texture)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_R, GL_REPEAT)

		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		glTexImage2D(GL_TEXTURE_2D, 0, 3, img_x, img_y, 0, GL_RGBA, GL_UNSIGNED_BYTE, raw_image)
		self.update()
		pass

	def __set_frame_texture(self, frame):		
		glGenTextures(1, self.__texture)
		glBindTexture(GL_TEXTURE_2D, self.__texture)
		
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, frame.shape[1], frame.shape[0], 0, GL_BGR, GL_UNSIGNED_BYTE, frame)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		self.update()
		pass

	def update(self):

		"""Updates the commandlist
		"""

		self.__obj = self.__make_commandlist()
		pass

	def draw(self):

		"""Call the generated commandlist.	
		"""

		glCallList(self.__obj)
		pass