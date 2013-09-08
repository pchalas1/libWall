import numpy
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
from random import *

from .gl_utils import *
from .gl_lighting import Lighting
	
import math

class Sphere(object):	

	""" @author : Preetham Chalasani
	@brief : Create a Sphere Object with specific number of stacks and slices.
	"""

	def __init__(self, *args):

		"""
		@param args : Radius, slices , stacks OR default values will be applied
		"""

		self.__rad = 0.3
		self.__slices = 30
		self.__stacks = 30

		if len(args) == 1:
			self.__rad = float(args[0])
			pass
		elif len(args) == 3:
			self.__rad = float(args[0])
			self.__slices = args[1]
			self.__stacks = args[2]
			pass				

		self.__makeTexCoords = False
		self.__speed = [0,0,0]
		self.__position = [0,0,0]
		self.__range = [[-1+self.__rad,1-self.__rad],[-1+self.__rad,1-self.__rad],[-1+self.__rad,1-self.__rad]]
		self.collision = False

		self.__rotAngles = [0,0,0]

		self.__lighting = None
		self.__initLighting()

	def __initLighting(self):

		"""Initialize lighting
		"""

		self.__lighting = Lighting()		
		self.__lighting.addLight(GL_LIGHT0)
		self.__lighting.setLight(GL_LIGHT0, [ 1.0, 1.0, -1.0, 0.0 ], [1,0,1], [ 1.0, 1.0, 1.0, 1.0 ] , [0,0,1])
		pass

	def setMakeTexCoords(self, boolean):

		"""Set if texture coordinates are needed or Not
		@param boolean
		"""

		self.__makeTexCoords = boolean
		pass

	def numOfSlices(self, n):

		"""Set/get number of slices
		@param n : Number of slices
		@return n Number of slices
		"""

		if slices == None:
			return self.__slices
		elif type(n) is 'int':			
			self.__slices = n
		else:
			log_err("Not a valid argument")		
		pass

	def numOfStacks(self, n):

		"""Set/get number of stacks
		@param n : Number of stacks
		@return n Number of stacks
		"""		

		if stacks == None:
			return self.__stacks
		elif type(n) is 'int':			
			self.__stacks = n
		else:
			log_err("Not a valid argument")		
		pass

	def radius(self, n=None):

		"""Set/get radius
		@param n : radius
		@return n radius
		"""

		if n == None:
			return self.__rad
		elif type(n) in ['int','long','float']:			
			self.__rad = n
		else:
			log_err("Not a valid argument")		
		pass

	def render(self):

		"""Renders the sphere object with stored rotation, translation and scaling values
		"""

		glPushMatrix()		
		glMaterialfv(GL_FRONT, GL_SPECULAR, [ 1.0, 1.0, 1.0, 1.0 ]);
		glMaterialf(GL_FRONT, GL_SHININESS, 100);			
		self.__lighting.render()

		glRotatef(self.__rotAngles[0], 1, 0, 0)
		glRotatef(self.__rotAngles[1], 0, 1, 0)
		glRotatef(self.__rotAngles[2], 0, 0, 1)
		
		glTranslatef(self.__position[0], self.__position[1], self.__position[2])					

		glutSolidSphere(self.__rad, self.__slices, self.__stacks)
		glPopMatrix()
		pass

	def scale(self,xScale, yScale, zScale):		

		"""Scale the sphere object
		@param xScale : Scaling value in X-direction
		@param yScale : Scaling value in Y-direction
		@param zScale : Scaling value in Z-direction
		"""

		glScalef(xScale, yScale, zScale)						
		self.__updatePos()
		pass

	def rotateX(self, ang):

		"""	Set the roatition angle about the X axis
		@param ang : Rotation in degrees
		"""

		self.__rotAngles[0] = self.__rotAngles[0] + ang
		pass

	def rotateY(self, ang):

		"""	Set the roatition angle about the Y axis
		@param ang : Rotation in degrees
		"""

		self.__rotAngles[1] = self.__rotAngles[1] + ang		
		pass

	def rotateZ(self, ang):

		"""	Set the roatition angle about the Z axis
		@param ang : Rotation in degrees
		"""

		self.__rotAngles[2] = self.__rotAngles[2] + ang		
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

	def speed(self, *args):

		"""Set speed of the sphere to move
		@param x : speed in X direction
		@param y : speed in Y direction
		@param z : speed in Z direction
		"""
		if len(args) == 0:
			return self.__speed
		elif type(args[0]).__name__ == 'list':
			self.__speed = args[0]
		elif len(args) == 3:
			self.__speed = [args[0], args[1], args[2]]			
		pass

	def randomSpeed(self):

		"""Set Random speed
		"""

		self.__speed = [random()*0.04, random()*0.05,random()*0.07]
		pass

	def randomPos(self):

		"""Set random position of the sphere 
		"""

		self.__position = [random()*1, random()*1,0]
		pass

	def randomSpeedAndPos(self):

		"""Set random position and speed on the sphere
		"""

		self.__speed = [random()*0.04, random()*0.05, 0]
		self.__position = [random()*1, random()*1, 0]
		pass

	def randomColor(self):

		"""Set random color 
		"""

		pass

	def range(self, rangeVal=None):

		"""Set a range of motion for the sphere object
		@param rangeVal : a list of 2x3 where each row define negative and positive limits of X,Y,Z
		"""
		if rangeVal == None:
			return self.__range
		elif type(rangeVal).__name__ is 'list':							
			self.__range = rangeVal
		pass

	def setXRange(self, negRange, posRange):

		"""Set a range of motion in X-direction
		@param negRange,posRange : Negative and positive limits of the sphere object in X-direction
		"""

		self.__range[0][0] = negRange
		self.__range[0][1] = negRange
		pass

	def setYRange(self, negRange, posRange):

		"""Set a range of motion in Y-direction
		@param negRange,posRange : Negative and positive limits of the sphere object in Y-direction
		"""

		self.__range[1][0] = negRange
		self.__range[1][1] = negRange
		pass

	def setZRange(self, negRange, posRange):

		"""Set a range of motion in Z-direction
		@param negRange,posRange : Negative and positive limits of the sphere object in Z-direction
		"""

		self.__range[2][0] = negRange
		self.__range[2][1] = negRange
		pass	

	def position(self, *args):

		"""Set/get the position of the sphere
		@param args : x,y,z, position or a list containing x,y,z position or None(Getter)
		@return position : Center position of the sphere
		"""

		if len(args) == 0:
			return self.__position		
		elif (type(args[0]).__name__) == 'list':
			self.__position = posValue		
		elif len(args) == 3:
			self.__position = [args[0], args[1], args[2]]
		pass

	def moveX(self, dist):

		""" Move the sphere position from the current position along X-axis
		@param dist : Value to move
		"""

		self.__position[0] = self.__position[0] + dist
		pass

	def moveY(self, dist):

		""" Move the sphere position from the current position along Y-axis
		@param dist : Value to move
		"""

		self.__position[1] = self.__position[1] + dist
		pass

	def moveZ(self, dist):

		""" Move the sphere position from the current position along Z-axis
		@param dist : Value to move
		"""

		self.__position[2] = self.__position[2] + dist
		pass	

	def move(self, *args):

		""" Move the sphere position from the current position along X,Y,Z-axis
		@param args : x,y,z values or a list of 3 distance valuea
		"""

		if len(args) == 3:
			self.__position[0] = self.__position[0] + args[0]
			self.__position[1] = self.__position[1] + args[1]
			self.__position[2] = self.__position[2] + args[2]
			pass
		elif (type(args[0]).__name__) == 'list':
			self.__position = [sum(values) for values in zip( *([self.__position] + [args[0]]) )]
		elif len(args) == 0:
			return self.__position
		pass

	def checkCollision(self, a):

		"""Check Collision with another sphere
		@param a : Sphere
		@return boolean
		"""

		if type(a).__name__ == 'Sphere':
			temp = pow(self.__position[0] - a.position()[0], 2) + pow(self.__position[1] - a.position()[1], 2) + pow(self.__position[2] - a.position()[2], 2)

			if temp < pow(self.__rad + a.radius(), 2):
				if not self.collision or not a.collision:
					tempVal = self.__speed
					self.__speed = a.speed()
					a.speed(tempVal)

					self.collision = True
					a.collision = True
				else:
					self.collision = False
					a.collision = False
				pass
			else:
				self.collision = False
				a.collision = False
			pass
		pass
		
