#!/usr/bin/env python

import sys

import rospy

import modulair_core
from modulair_core import ModulairAppWidget

from PySide import QtGui

"""	@brief Low level Wrapper of ModulairAppWidget. Parent this class to obtain Qt Context to execute your QGLWidget """
"""	@author Ceasar Hernandez """

class GLWallCanvas(ModulairAppWidget):

	def __init__(self, name, anonymous = True):

		""" Initializes the rosnode and create a QApplication"""

		rospy.init_node(name, anonymous = anonymous)

		self.app = QtGui.QApplication(sys.argv)	
		
		super(GLWallCanvas, self).__init__(name, self.app)

		self.default_width = self.width_
		self.default_height = self.height_ * self.height_perc_
		pass

	def use_default_layout(self, widget):


		""" Creates a default qt grid layout which will let to add the user's widget
		@param widget : QGLWidget - User widget"""

		default_layout = QtGui.QGridLayout()
		default_layout.addWidget(widget)
		self.setLayout(default_layout)
		pass