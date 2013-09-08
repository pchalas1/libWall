#!/usr/bin/env python

from wall import *

class ModelBrowser(GLWidget):

	def __init__(self, path, width, height, parent = None):

		"""@param path : Path to a model
		@param width : Width of the Screen
        @param height : Height of the Screen
        """

		super(ModelBrowser, self).__init__(parent = parent)
		self.path_ = path
		self.width_ = width
		self.height_ = height
		self.inc  = 0
		self.roty = 0;
		self.cam = Camera('GLU_PERSPECTIVE')
		pass

	def initGL(self):

		"""Overloaded function from GLWidget
        """

		self.model = Model()
		self.model.load_model(self.path_)
		self.cam.setEye(0,0,-60)
		self.cam.on()

		pass

	def paint(self):

		"""Overloaded function from GLWidget
        """

		self.cam.on()				

		glPushMatrix()
		glRotatef(self.roty, 0.0, 1.0,0.0)						
		glTranslatef(0,0,10)
		glRotatef(self.roty*2, 1.0, 0.0,0.0)						
		self.model.render()
		glPopMatrix()
		
		pass

	def idle(self):

		"""Overloaded function from GLWidget
        """

		self.roty = self.roty + 2
		self.update_widget()				
		pass	