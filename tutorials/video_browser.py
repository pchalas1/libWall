#!/usr/bin/env python

import wall

class VideoBrowser(GLWidget):

	""" @author Preetham Chalasani
    @brief Simple Video browser application
    """

	def __init__(self, path, width, height, parent = None):

		"""@param path : Path to a video file
		@param width : Width of the Screen
        @param height : Height of the Screen
        """		

		self.path_ = path
		self.video_width_ = width
		self.video_height_ = height

		self.video = load_video(path)
		self.fps = get_video_fps(self.video)

		log_warn('FPS: ' + str(self.fps))

		super(VideoBrowser, self).__init__(delay = self.fps, parent = parent)
		pass

	def initGL(self):

		"""Overloaded function from GLWidget
        """

		self.quad = Rectangle(0, 0, self.video_width_, self.video_height_, get_next_frame(self.video), 'IPL')
		pass

	def paint(self):

		"""Overloaded function from GLWidget
        """

		self.quad.draw()
		pass

	def idle(self):

		"""Overloaded function from GLWidget
        """

		frame = get_next_frame(self.video)
		if frame == None:
			self.clean_up()
			return
		self.quad.load_texture(frame, 'IPL')
		self.update_widget()
		pass