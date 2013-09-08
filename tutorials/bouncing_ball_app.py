#!/usr/bin/env python

import roslib; roslib.load_manifest('modulair_apps_python')
from bouncing_ball import BouncingBall
from wall import *

class BouncingBallApp(GLWallCanvas):

	# signal_next_image = create_signal()
	# signal_prev_image = create_signal()

	def __init__(self, name):
		super(BouncingBallApp, self).__init__(name)

		self.bouncing_ball_widget = BouncingBall(self.default_width, self.default_height)
		self.use_default_layout(self.bouncing_ball_widget)

		# self.signal_next_image.connect(self.bouncing_ball_widget.next_image)
		# self.signal_prev_image.connect(self.bouncing_ball_widget.prev_image)
		pass

	# def user_event_cb(self, msg):
	# 	self.current_user_event_ = msg

	# 	if msg.message == 'left_hand_on_head':
	# 		self.signal_prev_image.emit()
	# 	elif msg.message == 'right_hand_on_head':
	# 		self.signal_next_image.emit()
	# 	pass

if __name__ == '__main__':
	app_canvas = BouncingBallApp('bouncing_wall')
	log_warn('bouncing_wall: Started')
	app_canvas.app.exec_()
	log_warn('bouncing_wall: Finished')