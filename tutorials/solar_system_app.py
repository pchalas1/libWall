#!/usr/bin/env python

import roslib; roslib.load_manifest('modulair_apps_python')
from solar_system import SolarSystem
from wall import *

class SolarSystemApp(GLWallCanvas):
	def __init__(self, name):
		super(SolarSystemApp, self).__init__(name)
		
		self.solar_system_widget = SolarSystem(self.default_width, self.default_height)
		self.use_default_layout(self.solar_system_widget)
		pass

if __name__ == '__main__':
	app_canvas = SolarSystemApp('solar_system')
	log_warn('solar_system: Started')
	app_canvas.app.exec_()
	log_warn('solar_system: Finished')