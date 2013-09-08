from .gl_vec3 import Vec3
from .gl_utils import *

import PyKDL
import math

class Frame(object):	

	"""	@author Preetham Chalasani
	@brief Frame with a translation and a rotation.
	"""

	def __init__(self, rot, trans):

		"""Intialize a frame with a rotation and a translation
		@param rot : Rotation vector (degrees), Vec3
		@param trans : Translation Vector, Vec3
		"""

		self.__rotationVec = 0
		self.__transVec = 0
		self.__frame = 0

		if type(rot).__name__ == 'Vec3' and type(trans).__name__ == 'Vec3':
			pass			
			self.__rotationVec = rot
			self.__transVec = trans
			
		elif type(rot).__name__ == 'list' and type(trans).__name__ == 'list':
			self.__rotationVec = Vec3(rot)
			self.__transVec = Vec3(trans)
			
		elif type(rot).__name__ == 'list' and type(trans).__name__ == 'Vec3':
			self.__rotationVec = Vec3(rot)
			self.__transVec = trans
			
		elif type(rot).__name__ == 'Vec3' and type(trans).__name__ == 'list':
			self.__rotationVec = rot
			self.__transVec = Vec3(trans)

		if not type(self.__transVec).__name__ == 'int' or not type(self.__rotationVec).__name__ == 'int' :
			self.__frame = PyKDL.Frame(PyKDL.Rotation.EulerZYX(self.__rotationVec[0]*math.pi/180, 
											self.__rotationVec[1]*math.pi/180, 
											self.__rotationVec[2]*math.pi/180),
								PyKDL.Vector(self.__transVec[0],
									   self.__transVec[1],
									   self.__transVec[2])
							   )
		pass

	def translation(self, value=None):

		"""Set/get a translation vector
		@param value : Vec3
		@return translation : Vec3 
		"""

		if type(value).__name__ == 'Vec3':
			self.__transVec = value
		elif type(value).__name__ == 'list':
			self.__transVec = Vec3(value)			
		elif value == None:
			return self.__transVec
		pass

	def rotation(self, value=None):

		"""Set/get a rotation vector
		@param value : Vec3
		@return rotation : Vec3 
		"""

		if type(value).__name__ == 'Vec3':
			self.__rotationVec = value
		elif type(value).__name__ == 'list':
			self.__rotationVec = Vec3(value)			
		elif value == None:
			return self.__rotationVec
		pass

	def matrix(self):

		"""Return the frame matrix		
		@return matrix : Frame 
		"""

		return self.__frame	

	def __toFrame(self, kdlFrame):		
		t = Vec3(kdlFrame.p[0], kdlFrame.p[1], kdlFrame.p[2])
		r = Vec3(kdlFrame.M.GetEulerZYX()[0], 
				 kdlFrame.M.GetEulerZYX()[1], 
				 kdlFrame.M.GetEulerZYX()[2])
				
		return Frame(r,t)		
		
	def __mul__(self, a):

		"""Frame multiplication with a Vec3 or another Frame
		@param a : Vec3 or Frame
		@return val : Vec3 or Frame
		"""

		temp = 0
		if type(a).__name__ == 'Vec3':
			temp = self.__frame * PyKDL.Vector(a.X(), a.Y(), a.Z())
			return(Vec3(temp[0], temp[1], temp[2]))	

		elif type(a).__name__ == 'list' and len(a) == 3:
			temp = self.__frame * PyKDL.Vector(a[0], a[1], a[2])
			return(Vec3(temp[0], temp[1], temp[2]))	

		elif type(a).__name__ == 'Frame':			
			tempVec = PyKDL.Vector(a.translation()[0], a.translation()[1], a.translation()[2])
			tempRot = PyKDL.Rotation.EulerZYX(a.rotation()[0], a.rotation()[1], a.rotation()[2])

			tempFrame = self.__frame * PyKDL.Frame(tempRot, tempVec)			
			return self.__toFrame(tempFrame)
	
	def __str__(self):		
		return(str(self.__transVec) + str(self.__rotationVec))	