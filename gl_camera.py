#!/usr/bin/env python

### OpenGL Imports ###
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import rospy
import math

from .gl_utils import *

class Camera(object):		

	"""	@author Preetham Chalasani
	@brief Setup a camera to view a scene and display on the viewport. 
	A camera can be placed at any point on the screen by giving it a positon of the eye,i.e camera, position of the reference point 
	and direction of up vector.
	"""

	def __init__(self, projectionType = None):

		""" Create a Camera with a specific projection.
		@param projectionType : 'ORTHOGRAPHIC', 'ORTHO2D' or 'PERSPECTIVE'
		"""

		super(Camera, self).__init__()

		# Projection Type
		self.__viewType = projectionType

		# Camera Number
		self.__camNumber = 0

		# Camera Active or Not
		self.__enabled = False

		# Default Projection Information
		self.__nearl = 0.1
		self.__farl = 100		
		self.__left = -1
		self.__right = 1
		self.__top = -1
		self.__bottom = 1
		self.__aspect = 1
		self.__fov = 60

		# Normal to the eye Location
		self.__normalX = 0
		self.__normalY = 0
		self.__normalZ = 0

		# View to scene center vector
		self.__viewX = 0
		self.__viewY = 0
		self.__viewZ = 0

		# Cumulative eye rotation
		self.__rotationEyeX = 0
		self.__rotationEyeY = 0

		# Eye Position		
		self.__eyeX = 0
		self.__eyeY = 0
		self.__eyeZ = 5

		# Scene Center
		self.__centerX = 0
		self.__centerY = 0
		self.__centerZ = 0

		# Up Orientation Vector
		self.__upX = 0
		self.__upY = 1
		self.__upZ = 0				

		self.calculateNormal()

	def moveLeft(self, dist):

		"""Move the camera to the camera's left
		@param dist : Distance
		"""

		self.__eyeX = self.__eyeX + (self.__normalX * -dist)
		self.__eyeY = self.__eyeY + (self.__normalY * -dist)
		self.__eyeZ = self.__eyeZ + (self.__normalZ * -dist)

		self.__centerX = self.__centerX + (self.__normalX * -dist)
		self.__centerY = self.__centerY + (self.__normalY * -dist)
		self.__centerZ = self.__centerZ + (self.__normalZ * -dist)

		pass

	def moveRight(self, dist):

		"""Move the camera to the camera's right
		@param dist : Distance
		"""

		self.__eyeX = self.__eyeX + (self.__normalX * dist)
		self.__eyeY = self.__eyeY + (self.__normalY * dist)
		self.__eyeZ = self.__eyeZ + (self.__normalZ * dist)

		self.__centerX = self.__centerX + (self.__normalX * dist)
		self.__centerY = self.__centerY + (self.__normalY * dist)
		self.__centerZ = self.__centerZ + (self.__normalZ * dist)
		pass

	def moveUp(self, dist):

		"""Move the camera up by some value
		@param dist : Distance
		"""

		self.__eyeX = self.__eyeX + (self.__upX * dist)
		self.__eyeY = self.__eyeY + (self.__upY * dist)
		self.__eyeZ = self.__eyeZ + (self.__upZ * dist)

		self.__centerX = self.__centerX + (self.__upX * dist)
		self.__centerY = self.__centerY + (self.__upY * dist)
		self.__centerZ = self.__centerZ + (self.__upZ * dist)
		pass

	def moveDown(self, dist):

		"""Move the camera down by some value
		@param dist : Distance
		"""

		self.__eyeX = self.__eyeX + (self.__upX * -dist)
		self.__eyeY = self.__eyeY + (self.__upY * -dist)
		self.__eyeZ = self.__eyeZ + (self.__upZ * -dist)

		self.__centerX = self.__centerX + (self.__upX * -dist)
		self.__centerY = self.__centerY + (self.__upY * -dist)
		self.__centerZ = self.__centerZ + (self.__upZ * -dist)
		pass

	def moveForward(self, dist):

		"""Move the camera forward by some value
		@param dist : Distance
		"""

		self.__eyeX = self.__eyeX + (self.__viewX * dist)
		self.__eyeY = self.__eyeY + (self.__viewY * dist)
		self.__eyeZ = self.__eyeZ + (self.__viewZ * dist)

		self.__centerX = self.__centerX + (self.__viewX * dist)
		self.__centerY = self.__centerY + (self.__viewY * dist)
		self.__centerZ = self.__centerZ + (self.__viewZ * dist)
		pass

	def moveBackward(self, dist):

		"""Move the camera backward by some value
		@param dist : Distance
		"""

		self.__eyeX = self.__eyeX + (self.__viewX * -dist)
		self.__eyeY = self.__eyeY + (self.__viewY * -dist)
		self.__eyeZ = self.__eyeZ + (self.__viewZ * -dist)

		self.__centerX = self.__centerX + (self.__viewX * -dist)
		self.__centerY = self.__centerY + (self.__viewY * -dist)
		self.__centerZ = self.__centerZ + (self.__viewZ * -dist)
		pass

	def moveEye(self, dx, dy, dz):

		"""Move the camera's eye
		@param dx,dy,dz : Eye displacement
		"""

		self.__eyeX = self.__eyeX + dx
		self.__eyeY = self.__eyeY + dy
		self.__eyeZ = self.__eyeZ + dz
		pass

	def moveCenter(self, dx, dy, dz):

		"""Move the camera's center
		@param dx,dy,dz : Center displacement
		"""

		self.__centerX = self.__centerX + dx
		self.__centerY = self.__centerY + dy
		self.__centerZ = self.__centerZ + dz
		pass

	def rotateEye(self, dx, dy):

		"""Rotate the camera's eye
		@param dx,dy : Rotation about X and Y axis rrespectively
		"""

		self.__rotationEyeX = self.__rotationEyeX + dx
		self.__rotationEyeY = self.__rotationEyeY + dy

		# Rotate about the Up/Down Plane
		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()

		glLoadIdentity()
		glRotatef(-dx, self.__normalX, self.__normalY, self.__normalZ)
		rotate = glGetFloatv(GL_MODELVIEW_MATRIX)		

		# Calculate a new up direction
		newUpX = (rotate[0][0] * self.__upX + rotate[0][1] * self.__upY + rotate[0][2] * self.__upZ + rotate[0][3])
		newUpY = (rotate[1][0] * self.__upX + rotate[1][1] * self.__upY + rotate[1][2] * self.__upZ + rotate[1][3])
		newUpZ = (rotate[2][0] * self.__upX + rotate[2][1] * self.__upY + rotate[2][2] * self.__upZ + rotate[2][3])

		self.__upX = newUpX
		self.__upY = newUpY
		self.__upZ = newUpZ		

		newSceneX = (rotate[0][0] * self.__viewX + rotate[0][1] * self.__viewY + rotate[0][2] * self.__viewZ + rotate[0][3])
		newSceneY = (rotate[1][0] * self.__viewX + rotate[1][1] * self.__viewY + rotate[1][2] * self.__viewZ + rotate[1][3])
		newSceneZ = (rotate[2][0] * self.__viewX + rotate[2][1] * self.__viewY + rotate[2][2] * self.__viewZ + rotate[2][3])

		glLoadIdentity()
		glRotatef(-dy, self.__upX, self.__upY, self.__upZ)
		rotate = glGetFloatv(GL_MODELVIEW_MATRIX)
		glPopMatrix()

		newSceneX1 = (rotate[0][0] * newSceneX + rotate[0][1] * newSceneY + rotate[0][2] * newSceneZ + rotate[0][3])
		newSceneY1 = (rotate[1][0] * newSceneX + rotate[1][1] * newSceneY + rotate[1][2] * newSceneZ + rotate[1][3])
		newSceneZ1 = (rotate[2][0] * newSceneX + rotate[2][1] * newSceneY + rotate[2][2] * newSceneZ + rotate[2][3])

		self.__centerX = self.__eyeX + newSceneX1
		self.__centerY = self.__eyeY + newSceneY1
		self.__centerZ = self.__eyeZ + newSceneZ1

		# Update Vectors
		self.calculateNormal()

		pass

	def rotatePoint(self, dx, dy):		
		# calculate vector from the current view to the point
		self.setCenter(0,0,0)
		self.calculateNormal()

		self.__rotationEyeX = self.__rotationEyeX + dx
		self.__rotationEyeY = self.__rotationEyeY + dy

		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()

		glLoadIdentity()
		glRotatef(dx, self.__normalX, self.__normalY, self.__normalZ)
		rotate = glGetDoublev(GL_MODELVIEW_MATRIX)

		# Calculate new up direction
		newUpX = (rotate[0][0] * self.__upX + rotate[0][1] * self.__upY + rotate[0][2] * self.__upZ  + rotate[0][3])
		newUpY = (rotate[1][0] * self.__upX + rotate[1][1] * self.__upY + rotate[1][2] * self.__upZ  + rotate[1][3])
		newUpZ = (rotate[2][0] * self.__upX + rotate[2][1] * self.__upY + rotate[2][2] * self.__upZ  + rotate[2][3])

		self.__upX = newUpX
		self.__upY = newUpY
		self.__upZ = newUpZ

		newSceneX = (rotate[0][0] * -self.__viewX + rotate[0][1] * -self.__viewY + rotate[0][2] * -self.__viewZ  + rotate[0][3])
		newSceneY = (rotate[1][0] * -self.__viewX + rotate[1][1] * -self.__viewY + rotate[1][2] * -self.__viewZ  + rotate[1][3])
		newSceneZ = (rotate[2][0] * -self.__viewX + rotate[2][1] * -self.__viewY + rotate[2][2] * -self.__viewZ + rotate[2][3])

		glLoadIdentity()
		glRotated(dy, self.__upX, self.__upY, self.__upZ)
		rotate = glGetDoublev(GL_MODELVIEW_MATRIX)
		glPopMatrix()

		newSceneX1 = (rotate[0][0] * newSceneX + rotate[0][1] * newSceneY + rotate[0][2] * newSceneZ  + rotate[0][3]);
		newSceneY1 = (rotate[1][0] * newSceneX + rotate[1][1] * newSceneY + rotate[1][2] * newSceneZ  + rotate[1][3]);
		newSceneZ1 = (rotate[2][0] * newSceneX + rotate[2][1] * newSceneY + rotate[2][2] * newSceneZ  + rotate[2][3]);

		self.__eyeX = newSceneX1
		self.__eyeY = newSceneY1
		self.__eyeZ = newSceneZ1

		# Update Vectors
		self.calculateNormal()

		pass

	def rotateAxis(self, deg, x, y, z):
		glRotatef(deg, x, y, z)
		pass
	
	def on(self):

		"""Swithch on the camera
		"""

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()

		if self.__viewType == 'ORTHO2D':
			gluOrtho2D(self.__left, self.__right, self.__top, self.__bottom)
			pass

		elif self.__viewType == 'ORTHOGRAPHIC':
			glOrtho(self.__left, self.__right, self.__top, self.__bottom, self.__nearl, self.__farl)
			pass

		else:
			gluPerspective(self.__fov, self.__aspect, self.__nearl, self.__farl)
			pass		

		self.lookAtScene()

		pass
	
	def lookAtScene(self):

		"""Force the camera to look at the scene
		"""

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluLookAt(self.__eyeX, self.__eyeY, self.__eyeZ, 
				self.__centerX, self.__centerY, self.__centerZ,
				self.__upX, self.__upY, self.__upZ)
		pass
	
	def off(self):

		"""Turns off the camera and resets any effects on opengl
		"""

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		pass

	def modelViewMatrix(self):

		"""Return Model view matrix
		@return matrix : list of 16
		"""

		return glGetFloatv(GL_MODELVIEW_MATRIX)

	def projMatrix(self):

		"""Return Projection matrix
		@return matrix : List of 16
		"""

		return glGetFloatv(GL_PROJECTION_MATRIX)
		pass

	def clear(self, r, g, b, clearDepth = True):

		"""Clear the color and depth buffer
		@param r,g,b : RGB value of the color

		@param clearDepth : False, not to clear the depth buffer, else True
		"""

		glClearColor(r, g, b, 0)
		glClearColor(GL_COLOR_BUFFER_BIT)
		if clearDepth:
			glClear(GL_DEPTH_BUFFER_BIT)
		pass

	def setProjection(self, *args):

		"""Set the Projection Type		

		"""

		if len(args) == 5 and args[4] == 'ORTHO2D':			
			self.__left = args[0]
			self.__right = args[1]
			self.__top = args[2]
			self.__bottom = args[3]
			self.__viewType = ars[4]
			pass

		elif len(args) == 5 and args[4] == 'PERSPECTIVE':			
			self.__fov = args[0]
			self.__aspect = args[1]
			self.__nearl = args[2]			
			self.__farl = args[3]
			self.__viewType = ars[4]
			pass

		elif len(args) == 7 and args[6] == 'ORTHOGRAPHIC':			
			self.__left = args[0]
			self.__right = args[1]
			self.__top = args[2]
			self.__bottom = args[3]
			self.__nearl = args[4]
			self.__farl = args[5]
			self.__viewType = ars[6]
			pass

		else:
			print("Error : Number of arguments not correct")

		pass
	
	def setEye(self, ex, ey, ez):

		"""Set the camera's eye vector
		@param ex,ey,ez : Vector
		"""

		self.__eyeX = ex
		self.__eyeY = ey
		self.__eyeZ = ez
		pass

	def setUp(self, ux, uy, uz):

		"""Set the camera's up vector
		@param ux,uy,uz : Vector
		"""

		self.__upX = ux
		self.__upY = uy
		self.__upZ = uz

		self.calculateNormal()
		pass

	def setCenter(self, cx, cy, cz):

		"""Set the camera's center
		@param cx,cy,cz : Position
		"""

		self.__centerX = cx
		self.__centerY = cy
		self.__centerZ = cz
		pass

	def setCameraNumber(self, val):

		"""Set the camera number
		@param val : 'long' , 'float' or 'int'
		"""

		self.__camNumber = val
		pass

	def getProjection(self):	# 3

		"""Return the Projection Type
		@return : 'ORTHOGRAPHIC', 'ORTHO2D' or 'PERSPECTIVE'
		"""

		return self.__viewType

	def getEye(self):

		"""Return the eye position of the camera
		@return x,y,z : Position
		"""

		return [self.__eyeX, self.__eyeY, self.__eyeZ]

	def getUp(self):

		"""Return the up vector of the camera
		@return x,y,z : Vector
		"""

		return [self.__upX, self.__upY, self.__upZ]		

	def getCenter(self):

		"""Return the center position of the camera
		@return x,y,z : Position
		"""

		return [self.__centerX, self.__centerY, self.__centerZ]		

	def calculateNormal(self):

		"""Calculates the normal of up vector and eye to center vector
		@return x,y,z : Position
		"""

		# Determine view Vector
		self.__viewX = self.__centerX - self.__eyeX
		self.__viewY = self.__centerY - self.__eyeY
		self.__viewZ = self.__centerZ - self.__eyeZ

		# Calculate cross product of the view and up vectors
		self.__normalX = (self.__viewY * self.__upZ) - (self.__upY * self.__viewZ)
		self.__normalY = (self.__viewZ * self.__upX) - (self.__upZ * self.__viewX)
		self.__normalZ = (self.__viewX * self.__upY) - (self.__upX * self.__viewY)

		# Set to be a unit normal		
		magnitude = float(math.sqrt(pow(self.__normalX,2) + pow(self.__normalY,2) + pow(self.__normalZ,2)))
		
		self.__normalX = float(float(self.__normalX)/magnitude)
		self.__normalY = float(float(self.__normalY)/magnitude)
		self.__normalZ = float(float(self.__normalZ)/magnitude)
		pass