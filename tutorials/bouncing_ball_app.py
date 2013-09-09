#!/usr/bin/env python

import roslib; roslib.load_manifest('modulair_apps_python')
from bouncing_ball import BouncingBall
from wall import *

class BouncingBallApp(GLWallCanvas):

	def __init__(self, name):
		super(BouncingBallApp, self).__init__(name)

		# Create a OGLWidget
		self.bouncing_ball_widget = BouncingBall(self.default_width, self.default_height)

		# Set the widget on the layout.		
		self.use_default_layout(self.bouncing_ball_widget)
		pass

if __name__ == '__main__':

	# Create the applicaiton
	app_canvas = BouncingBallApp('bouncing_wall')
	log_warn('bouncing_wall: Started')

	# Execute the applicaition
	app_canvas.app.exec_()
	log_warn('bouncing_wall: Finished')