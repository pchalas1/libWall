#!/usr/bin/env python

import roslib; roslib.load_manifest('modulair_apps_python')
from object_testing import ObjectTesting
from wall import *

class ObjectTestingApp(GLWallCanvas):

	def __init__(self, name):
		super(ObjectTestingApp, self).__init__(name)

		self.object_testing_widget = ObjectTesting(self.default_width, self.default_height)
		self.use_default_layout(self.object_testing_widget)

		pass


if __name__ == '__main__':
	app_canvas = ObjectTestingApp('image_browser')
	log_warn('image_browser: Started')
	app_canvas._app.exec_()
	log_warn('image_browser: Finished')