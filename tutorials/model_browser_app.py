#!/usr/bin/env python

import roslib; roslib.load_manifest('modulair_apps_python')
from model_browser import ModelBrowser
from wall import *

class ModelBrowserApp(GLWallCanvas):
	def __init__(self, name):
		super(ModelBrowserApp, self).__init__(name)
		
		path = '/home/kraven/dev/wall/models/models/MS3D/jeep1.ms3d'
		
		# Create a OGLWidget
		self.model_browser_widget = ModelBrowser(path, self.default_width, self.default_height)

		# Set the widget on the layout.
		self.use_default_layout(self.model_browser_widget)
		pass

if __name__ == '__main__':
	
	# Create the applicaiton
	app_canvas = ModelBrowserApp('model_browser')
	log_warn('model_browser: Started')

	# Execute the applicaition
	app_canvas.app.exec_()
	log_warn('model_browser: Finished')