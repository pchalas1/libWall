#!/usr/bin/env python

import numpy
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import pyassimp
from pyassimp.postprocess import *
from pyassimp.helper import *

import random
from random import *

from gl_camera import *
import gl_utils

class Model(object):

	"""@author : Preetham Chalasani, Ceasar Hernandez
	@brief : Model Loader
	"""
	def __init__(self, parent = None):
		super(Model, self).__init__()

		self.__scene = None
		self.__angle = 1.0
		pass

	def load_model(self,path):

		"""Load model from the specified path
		@param path : Location of the model in the directory
		"""

		self.__scene = pyassimp.load(path)
		scene = self.__scene

		for index, mesh in enumerate(scene.meshes):						
			self.__prepare_gl_buffers(mesh)

		pyassimp.release(scene)
		
		pass

	def __prepare_gl_buffers(self,mesh):

		"""Prepare buffer to store mesha values
		@param mesh 
		"""

		mesh.gl = {}	

		mesh.gl["vertices"] = glGenBuffers(1)
		glBindBuffer(GL_ARRAY_BUFFER, mesh.gl["vertices"])
		glBufferData(GL_ARRAY_BUFFER, mesh.vertices, GL_STATIC_DRAW)

		mesh.gl["normals"] = glGenBuffers(1)
		glBindBuffer(GL_ARRAY_BUFFER, mesh.gl["normals"])
		glBufferData(GL_ARRAY_BUFFER, mesh.normals, GL_STATIC_DRAW)


		mesh.gl["triangles"] = glGenBuffers(1)
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, mesh.gl["triangles"])
		glBufferData(GL_ELEMENT_ARRAY_BUFFER, mesh.faces, GL_STATIC_DRAW)

		glBindBuffer(GL_ARRAY_BUFFER,0)
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,0)
		pass

	def render(self, child = None):

		"""Render the model from the buffer
		"""		

		if child == None:
			node = self.__scene.rootnode
		else:
			node = child
		# glPushMatrix()
		# m = node.transformation.transpose()
		# glMultMatrixf(m)

		for mesh in node.meshes:			
			self.__apply_material(mesh.material)

			glBindBuffer(GL_ARRAY_BUFFER, mesh.gl["vertices"])
			glEnableClientState(GL_VERTEX_ARRAY)
			glVertexPointer(3, GL_FLOAT, 0, None)

			glBindBuffer(GL_ARRAY_BUFFER, mesh.gl["normals"])
			glEnableClientState(GL_NORMAL_ARRAY)
			glNormalPointer(GL_FLOAT, 0, None)

			glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, mesh.gl["triangles"])
			glDrawElements(GL_TRIANGLES,len(mesh.faces) * 3, GL_UNSIGNED_INT, None)

			glDisableClientState(GL_VERTEX_ARRAY)
			glDisableClientState(GL_NORMAL_ARRAY)

			glBindBuffer(GL_ARRAY_BUFFER, 0)
			glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

		for child in node.children:
			self.render(child)

		# glPopMatrix()
		pass

	def __apply_material(self, mat):

		"""Apply material properties the model
		@param mat : mesh.material
		"""

		if not hasattr(mat, "gl_mat"):
			diffuse = numpy.array(mat.properties.get("diffuse", [0.8, 0.8, 0.8, 1.0]))
			specular = numpy.array(mat.properties.get("specular", [0., 0., 0., 1.0]))
			ambient = numpy.array(mat.properties.get("ambient", [0.6, 0.6, 0.6, 1.0]))
			emissive = numpy.array(mat.properties.get("emissive", [0., 0., 0., 1.0]))
			shininess = min(mat.properties.get("shininess", 1.0), 128)
			wireframe = mat.properties.get("wireframe", 0)
			twosided = mat.properties.get("twosided", 0)

			setattr(mat, "gl_mat", glGenLists(1))
			glNewList(mat.gl_mat, GL_COMPILE)

			# glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diffuse)
			# glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular)
			# glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, ambient)
			# glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, emissive)
			# glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shininess)
			glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [ 1.0, 1.0, 1.0, 1.0 ])
			glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 30)
			glLightfv(GL_LIGHT0, GL_AMBIENT,  [0.0, 0.0, 0.0, -1.0] )
			glLightfv(GL_LIGHT0, GL_POSITION, [ 1.0, 1.0, -1.0, 0.0 ])
			glEnable(GL_LIGHTING)
			glEnable(GL_LIGHT0) 
			glEnable(GL_DEPTH_TEST)
			glEnable(GL_CULL_FACE)
			# glPolygonMode(GL_FRONT_AND_BACK, GL_LINE if wireframe else GL_FILL)
			# glDisable(GL_CULL_FACE) if twosided else glEnable(GL_CULL_FACE)

			glEndList()

		glCallList(mat.gl_mat)
		pass
