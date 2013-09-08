#!/usr/bin/env python

### PySide Imports ###
from PySide import QtOpenGL
from PySide.QtCore import QTimer
### OpenGL Imports ###
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from .gl_utils import *

"""	@brief Low level Wrapper of Qt Opengl.QGLWidget. Parent this class to obtain OpenGL Context. """
"""	@author Preetham Chalasani, Ceasar Hernandez """


class GLWidget(QtOpenGL.QGLWidget):	
	
	def __init__(self, delay = 0, parent = None):

		QtOpenGL.QGLWidget.__init__(self, parent)

		self.__timer = QTimer()
		self.__timer.timeout.connect(self.idle)
		self.__timer.start(delay)
		pass

	def initializeGL(self):		

		""" Initializes openGL and sets up various opengl rule (Only few atm)
		
		Note : Do not override this function
		"""

		# __metaclass__= NonOverridable
		glEnable(GL_TEXTURE_2D)
		glClearColor(0.7, 0.7, 0.7, 0.7)
		glClearDepth(1.0)		
		glShadeModel(GL_SMOOTH)		
		glEnable(GL_CULL_FACE)				
		glEnable(GL_NORMALIZE)
		# glEnable(GL_LIGHT0)
		# glEnable(GL_LIGHTING)
		self.initGL()
		pass

	def paintGL(self):

		""" Clears the back buffer then calls the _paint method
		
		Note : Do not overload this function
		"""

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)		   
		self.paint()
		pass

	def resizeGL(self, width, height):	

		"""Resizes the gl camera to match the widget size.
		
		Note : Do not overload this function
		@param width : Width of the widget
		@param height : Height of the widget
		"""

		self.resize(width, height)
		pass
	
	def initGL(self):

		""" Lets the user initialise some openGL rules """		

		pass
	
	def paint(self):				

		"""Lets the user draw his scene"""

		pass
	
	def idle(self):

		""" This function gets called in a loop with the timer specified in the constructor
		Default timer is 10 micro seconds
		Useful for recursive rendering
		"""

		pass

	def update_widget(self):

		""" Updates the scene by calling _paint method """

		self.updateGL()
		pass
	
	def resize(self, width, height):


		""" Lets the user handle the widget resize event. 
		By default, this method resizes the view to the widget size.
		
		Note : Do not override this function unless it is very important. 
			    Since wall size cannot be changed, overriding this function will not be fruitful
		@param width : Width of the widget
		@param height : Height of the widget
		""" 

		pass
		       
	def __clean_up(self):
		
		""" Clean up event
		"""
		self.__timer.stop()

		pass

	def _enableGlut(self):

		""" Enable glut """ 

		glutInit()
		pass