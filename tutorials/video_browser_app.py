#!/usr/bin/env python

import roslib; roslib.load_manifest('modulair_appmaker')
from video_browser import VideoBrowser
import wall

class VideoBrowserApp(GLWallCanvas):

	def __init__(self, name):
		super(VideoBrowserApp, self).__init__(name)

		path = '/home/kel/modulair/modulair_apps_python/media/vids/random.avi'

		self.video_browser_widget = VideoBrowser(path, self.default_width, self.default_height)
		self.use_default_layout(self.video_browser_widget)
		pass

if __name__ == '__main__':
	app_canvas = VideoBrowserApp('video_browser')
	log_warn('video_browser: Started')
	app_canvas.app.exec_()
	log_warn('video_browser: Finished')