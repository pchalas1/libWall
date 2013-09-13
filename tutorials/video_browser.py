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

		# Load video from the specified directory
		self.video = load_video(path)

		# Get the fps of the video
		self.fps = get_video_fps(self.video)

		log_warn('FPS: ' + str(self.fps))

		# Set the fps for the idle function
		super(VideoBrowser, self).__init__(delay = self.fps, parent = parent)
		pass

	def initGL(self):

		"""Overloaded function from GLWidget
        """

        # Create a quad of a specific width and height on which the image has to 
		# be rendered. Also specify the image name and type of image format.
		self.quad = Rectangle(0, 0, self.video_width_, self.video_height_, get_next_frame(self.video), 'IPL')
		pass

	def paint(self):

		"""Overloaded function from GLWidget
        """

        # Draw the quad with previously defined parameters.
		self.quad.draw()
		pass

	def idle(self):

		"""Overloaded function from GLWidget
        """

        # Grab the next frame of the video 
		frame = get_next_frame(self.video)

		# If no frame, meaning video has ended
		if frame == None:
			self.clean_up()
			return

		# Load the corresonding texture
		self.quad.load_texture(frame, 'IPL')

		# Update the widget, which basically is a call to pain function
		self.update_widget()
		pass