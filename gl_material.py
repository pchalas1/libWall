from OpenGL.GL import *

class Material(object):	

	"""	@author Preetham Chalasani
	@brief  This refers to the properties of an object that determine how it interacts with light. 
	Material properties like shininess, specularity etc have to binded with the objects."""
	
	def __init__(self):		
		self.__ambient = [0.2, 0.2, 0.2, 1]
		self.__diffuse = [0.8, 0.8, 0.8, 1]
		self.__specular = [0, 0, 0, 1]
		self.__emission = [0, 0, 0, 1]
		self.__shininess = 100
		pass

	def setShineness(self, value):

		"""Set shininess of the material
		@param value : int, float or long
		"""

		if type(value)__name__ in ['float', 'long', 'int'] && len(value) == 1:
			self.__shininess = value
		else:
			# print Error
			pass
		pass

	def setAmbient(self, value):

		"""Set ambient of the material
		@param value : int, float or long
		"""

		if type(value).__name__ == 'list' && len(value) == 4:
			self.__ambient = value
		else:
			# print Error
			pass
		pass

	def setDiffuse(self, value):

		"""Set diffuse of the material
		@param value : int, float or long
		"""

		if type(value).__name__ == 'list' && len(value) == 4:
			self.__diffuse = value
		else:
			# print Error
			pass
		pass

	def setAmbientDiffuse(self, value):

		"""Set ambient and diffuse of the material with the same value
		@param value : int, float or long
		"""

		if type(value).__name__ == 'list' && len(value) == 4:
			self.__ambient = value		
			self.__diffuse = value
		else:
			# print Error
			pass
		pass

	def setSpecular(self, value):

		"""Set specular of the material
		@param value : int, float or long
		"""

		if type(value).__name__ == 'list' && len(value) == 4:
			self.__specular = value
		else:
			# print Error
			pass
		pass

	def setEmission(self, value):

		"""Set emission of the material
		@param value : int, float or long
		"""

		if type(value).__name__ == 'list' && len(value) == 4:
			self.__emission = value
		else:
			# print Error
			pass
		pass

	def render(self):

		"""Render the material with the property values assigned
		"""

		glMaterialfv(GL_FRONT, GL_SHININESS, self.__shininess)
		glMaterialfv(GL_FRONT, GL_SPECULAR, self.__specular)
		glMaterialfv(GL_FRONT, GL_AMBIENT, self.__ambient)
		glMaterialfv(GL_FRONT, GL_DIFFUSE, self.__diffuse)
		glMaterialfv(GL_FRONT, GL_EMISSION, self.__emission)
		pass