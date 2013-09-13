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

		# Set the camera to Perspective view
		self.cam = Camera('PERSPECTIVE')
		pass

	def initGL(self):

		"""Overloaded function from GLWidget
        """

        # Create a model object
		self.model = Model()

		# Load the model that has to be rendered
		self.model.load_model(self.path_)

		#Set the camera eye position, so that the model can be viewed efficiently in the screen coordinates
		self.cam.setEye(0,0,-60)

		# Switch on the camera to view the scene
		# Default camera parameters will be used if no specific parameters are defined
		self.cam.on()

		pass

	def paint(self):

		"""Overloaded function from GLWidget
        """

        # This block basically rotates the model about it's own axis, then translates the model to 10 units in the Z direction, 
        # then roates the model around the center from where it was translated.
        # To understand the functionality of PushMatrix please refer http://www.opengl.org/sdk/docs/man2/xhtml/glPushMatrix.xml
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

        # Rotation angle will be updated after every 30ms
		self.roty = self.roty + 2

		# Update the widget, which basically is a call to pain function
		self.update_widget()				
		pass	