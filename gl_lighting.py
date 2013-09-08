from OpenGL.GL import *

class Lighting(object):

	"""	@author Preetham Chalasani
	@brief  Lighting for the scene. Used to enable single/multiple Light sources. 
	This class helps to setup a light source at some position on the screen from which light will be emitted"""

	def __init__(self):
		self.__lights = {}
		glEnable(GL_LIGHTING)
	
	def addLight(self, id):

		"""Adds a Light with the given id to the scene 
		@param id : GL_LIGHTi where i = 0, 1, 2 .. GL_MAX_LIGHTS
		"""

		newLight = Light(id)
		self.__lights[id] = newLight

	def setLight(self, id, position, diffuse, specular, ambient):	

		"""Set the light properties for the id
		@param id : GL_LIGHTi where i = 0, 1, 2 .. GL_MAX_LIGHTS
		@param position :  A list containing four fixed-point or floating-point values that specify the position of the light in homogeneous object coordinates.
		@param diffuse : A list containing four fixed-point or floating-point values that specify the diffuse RGBA intensity of the light. 
		@param specular : A list containing four fixed-point or floating-point values that specify the specular RGBA intensity of the light. 
		@param ambient : A list containing four fixed-point or floating-point values that specify the ambient RGBA intensity of the light. 
		"""

		self.__lights[id].set(position, diffuse, specular, ambient)

	def render(self):	

		"""
		Render all light sources on to the scene.
		"""

		for light in self.__lights.values():
			light.render()

class Light(object):      
	"""	@author Preetham Chalasani 
		@brief Individual Light source properties"""
	

	def __init__(self, id):

		"""
		Enables the light source with the specified id
		@param id : GL_LIGHTi where i = 0, 1, 2 .. GL_MAX_LIGHTS
		"""

		self.__id = id
		glEnable(id)

		self.__position = []
		self.__diffuse = []
		self.__specular = []
		self.__ambient = []

	def set(self, position, diffuse, specular, ambient):

		"""Set the light parameteres
		@param position :  A list containing four fixed-point or floating-point values that specify the position of the light in homogeneous object coordinates.
		@param diffuse : A list containing four fixed-point or floating-point values that specify the diffuse RGBA intensity of the light. 
		@param specular : A list containing four fixed-point or floating-point values that specify the specular RGBA intensity of the light. 
		@param ambient : A list containing four fixed-point or floating-point values that specify the ambient RGBA intensity of the light. 
		"""

		self.__position = position
		self.__diffuse = diffuse
		self.__specular = specular
		self.__ambient = ambient

	def render(self):

		"""Render the light source.
		"""

		glLight(self.__id, GL_POSITION, self.__position)
		glLight(self.__id, GL_DIFFUSE,  self.__diffuse)
		glLight(self.__id, GL_SPECULAR, self.__specular)
		glLight(self.__id, GL_AMBIENT,  self.__ambient)