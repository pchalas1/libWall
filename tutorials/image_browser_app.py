#!/usr/bin/env python

import roslib; roslib.load_manifest('modulair_apps_python')
from image_browser import ImageBrowser
from wall import *

class ImageBrowserApp(GLWallCanvas):

	signal_next_image = create_signal()
	signal_prev_image = create_signal()

	def __init__(self, name):
		super(ImageBrowserApp, self).__init__(name)

		path = '/home/kraven/dev/modulair/modulair_apps_python/media/images/'	

		# Create a OGLWidget
		self.image_browser_widget = ImageBrowser(path, self.default_width, self.default_height)

		# Set the widget on the layout.		
		self.use_default_layout(self.image_browser_widget)

		# Connect the signals to the gesture
		self.signal_next_image.connect(self.image_browser_widget.next_image)
		self.signal_prev_image.connect(self.image_browser_widget.prev_image)
		pass


	def user_event_cb(self, msg):
		
		"""Check the gestures being passed in ROS
		"""

		self.current_user_event_ = msg

		# Emit qt signal according to the gestures of th user
		if msg.message == 'left_hand_on_head':
			self.signal_prev_image.emit()
		elif msg.message == 'right_hand_on_head':
			self.signal_next_image.emit()
		pass

if __name__ == '__main__':

	# Create the applicaiton
	app_canvas = ImageBrowserApp('image_browser')
	log_warn('image_browser: Started')

	# Execute the applicaition
	app_canvas.app.exec_()
	log_warn('image_browser: Finished')