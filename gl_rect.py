from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
from .gl_frame import Frame
from .gl_vec3 import *

class Rectangle(object):

	"""	@author Preetham Chalasani
	@brief Create a Rectangle"""

	def __init__(self, x, y, z, w, h):
		"""Initializes rectangle paramets according to the input values.
		@param x,y,z : Bottomleft vertex of the rectangle
		@param w : Width in x direction
		@param h : Height in y direction
		"""

		super(Rectangle, self).__init__()
		self.__x = float(x)
		self.__y = float(y)
		self.__z = float(z)
		self.__w = float(w)
		self.__h = float(h)

		self.__v1 = Vec3(self.__x,self.__y, self.__z)
		self.__v2 = Vec3(self.__x + self.__w, self.__y, self.__z)
		self.__v3 = Vec3(self.__x + self.__w, self.__y + self.__h, self.__z)
		self.__v4 = Vec3(self.__x, self.__y + self.__h, self.__z)

		self.__pos = [self.__x + self.__w/2, self.__y + self.__h/2, self.__z]
		self.__tMatrix = 0
		glDisable(GL_CULL_FACE)	
		self.__rotAngles = [0,0,0]
		self.__scaleVal = [1,1,1]	

	def width(self,width=None):
		"""Set/get the width of the rectangle
		@param width 
		@return width of the rectangle
		"""
		if width == None:
			return self.__w
		else:
			self.__w = width
				
	def height(self,height=None):
		"""Set/get the height of the rectangle
		@param height 
		@return height of the rectangle
		"""
		if height == None:
			return self.__h
		else:
			self.__h = height

	def position(self, *args):
		"""Set/get the position of the rectangle
		@param args : x,y,z, position or a list containing x,y,z position or None(Getter)
		@return position : Center position of the rectangle
		"""
		if len(args) == 0:
			return self.__pos

		elif len(args) == 3:
			self.__pos[0] = args[0]
			self.__pos[1] = args[1]
			self.__pos[2] = args[2]
			pass
		elif (type(args[0]).__name__) == 'list':
			self.__pos = args[0]
		
		pass

	def v1(self):
		""" Returns bottom left vertex
		@return v1 : Bottom left vertex
		"""
		return self.__v1		

	def v2(self):
		""" Returns bottom right vertex
		@return v2 : Bottom right vertex
		"""
		return self.__v2

	def v3(self):
		""" Returns top right vertex
		@return v3 : Top right vertex
		"""
		return self.__v3

	def v4(self):
		""" Returns top left vertex
		@return v4 : Top left vertex
		"""
		return self.__v4

	def drawObject(self):		

		"""Draws the rectangle object
		"""

		glTranslatef(0,0,self.__z)
		glRectf(self.__x, self.__y, self.__x + self.__w, self.__y + self.__h)
		pass

	def render(self):

		"""Renders the rectangle object with stored rotation, translation and scaling values
		"""

		glPushMatrix()

		glScalef(self.__scaleVal[0], self.__scaleVal[1], self.__scaleVal[2])

		glRotatef(self.__rotAngles[0], 1, 0, 0)
		glRotatef(self.__rotAngles[1], 0, 1, 0)
		glRotatef(self.__rotAngles[2], 0, 0, 1)

		glTranslatef(self.__pos[0], self.__pos[1], self.__pos[2])
		
		self.drawObject()	

		glPopMatrix()
		pass

	def rotateX(self, ang):

		"""	Set the roatition angle about the X axis
		@param ang : Rotation in degrees
		"""

		self.__rotAngles[0] = self.__rotAngles[0] + ang
		self.__updatePos()
		pass

	def rotateY(self, ang):

		"""	Set the roatition angle about the Y axis
		@param ang : Rotation in degrees
		"""

		self.__rotAngles[1] = self.__rotAngles[1] + ang
		self.__updatePos()
		pass

	def rotateZ(self, ang):

		"""	Set the roatition angle about the Z axis
		@param ang : Rotation in degrees
		"""

		self.__rotAngles[2] = self.__rotAngles[2] + ang
		self.__updatePos()
		pass

	def rotate(self, *args):

		"""	Set the roatition angle about the X,Y,Z axis
		@param args : x,y,z angles in degrees or a list of 3 angles 
		"""

		if type(args[0]).__name__ == 'list' and len(args[0] == 3) :
			self.__rotAngles = args[0]
			pass
		elif len(args) == 3:
			self.__rotAngles[0] = args[0]
			self.__rotAngles[1] = args[1]
			self.__rotAngles[2] = args[2]
			pass
		pass

	def moveX(self, dist):

		""" Move the rectangle position from the current position along X-axis
		@param dist : Value to move
		"""

		self.__pos[0] = self.__pos[0] + dist
		self.__updatePos()
		pass

	def moveY(self, dist):

		""" Move the rectangle position from the current position along Y-axis
		@param dist : Value to move
		"""

		self.__pos[1] = self.__pos[1] + dist
		self.__updatePos()
		pass

	def moveZ(self, dist):

		""" Move the rectangle position from the current position along Z-axis
		@param dist : Value to move
		"""

		self.__pos[2] = self.__pos[2] + dist
		self.__updatePos()
		pass

	def move(self, *args):

		""" Move the rectangle position from the current position along X,Y,Z-axis
		@param args : x,y,z values or a list of 3 distance valuea
		"""

		if len(args) == 3:
			self.__pos[0] = self.__pos[0] + args[0]
			self.__pos[1] = self.__pos[1] + args[1]
			self.__pos[2] = self.__pos[2] + args[2]
			pass
		elif (type(args[0]).__name__) == 'list':
			self.__pos = [sum(values) for values in zip( *([self.__pos] + [args[0]]) )]
		elif len(args) == 0:
			return self.__pos
		self.__updatePos()
		pass

	def scale(self,xScale, yScale, zScale):		

		"""Scale the rectangle object
		@param xScale : Scaling value in X-direction
		@param yScale : Scaling value in Y-direction
		@param zScale : Scaling value in Z-direction
		"""

		glScalef(xScale, yScale, zScale)						
		self.__updatePos()
		pass

	def __updatePos(self):

		"""Update the vertix positions according to the transformation of the object.
		"""

		r = Vec3(self.__rotAngles[0], self.__rotAngles[1], self.__rotAngles[2])
		v  = Vec3(self.__pos[0], self.__pos[1], self.__pos[2])				
		self.__tMatrix = Frame(r,v)

		self.__v1 = self.__tMatrix * self.__v1
		self.__v2 = self.__tMatrix * self.__v2
		self.__v3 = self.__tMatrix * self.__v3
		self.__v4 = self.__tMatrix * self.__v4
		pass

	def frameMatrix(self):

		""" Transformation Matrix for the object from the starting postition
		@return tMatrix : Frame
		"""

		return self.__tMatrix		