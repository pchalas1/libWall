#!/usr/bin/env python

from wall import *

class SolarSystem(GLWidget):

	def __init__(self, width, height, parent = None):

		"""@param width : Width of the Screen
        @param height : Height of the Screen
        """

		super(SolarSystem, self).__init__(depth = True, parent = parent)		
		self.width_ = width
		self.height_ = height
		self.inc  = 0
		self.cam = Camera('GLU_PERSPECTIVE')
		self.enableGlut()
		self.sph = Sphere(0.3,30,30)
		self.year = 0;
		self.day = 0;
		pass

	def initGL(self):	

		"""Overloaded function from GLWidget
        """

		glShadeModel(GL_SMOOTH)		
		self.cam.on()		
		pass

	def paint(self):				

		"""Overloaded function from GLWidget
        """

		self.cam.on()		
		glRotatef(self.year,0,1,0)
		glTranslatef(0,0,1)
		glRotatef(self.day,0,1,0)		
		self.sph.render()		
		
		pass

	def idle(self):		

		"""Overloaded function from GLWidget
        """

		self.year = self.year+1
		self.day = self.day+1
		self.update_widget()				
		pass	