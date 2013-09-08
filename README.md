Modulair Python Library
=======================

This library helps user to create applications for Balaur Wall. It is still under development, however there are some sample applications that will guide you through the library functionality.

Library Files
-------------

- gl_camera      : Setup a camera to view a scene and display on the viewport.
- gl_frame       : Frame with a translation and a rotation.
- gl_vec3		 : 3D Vector class
- gl_group       : TODO
- gl_lighting    : Lighting for the scene. Used to enable single/multiple Light sources
- gl_material    : 
- gl_matrix      : TODO
- gl_model       : Model Loader
- gl_object      : Currently only sphere object is available. Rectangle will come under this class in the later release
- gl_quad        : To create a quad
- gl_rect        : Create a recatangle object
- gl_rot3x3      : Rotation Matrix TODO
- gl_utils       : Utility class, containing basic functinality of loading a video or image etc
- gl_wall_canvas : Low level Wrapper of ModulairAppWidget. Parent this class to obtain Qt Context to execute your QGLWidget
- gl_widget_base : Low level Wrapper of Qt Opengl.QGLWidget. Parent this class to obtain OpenGL Context.


Tutorial Files
--------------

- imgage_browser : Simple image browser application
- video_browser  : Simple video browser application
- bouncing_ball  : Create few balls and let them bounce accross the walls of the screen
- model_browser  : Load a model
- solar_system   : Its just a testing application that can be used for bug testing

Important Note 
-------------- 
- All the tutorial files ending with '_app.py' are the application files that creates the widget object and launces it. These files have to be given read/write/execute privelages (chmod 777 filename)

- A launch file has to be created for every application and put in the launch folder. 

- To launch the applicaiton, call roslaunch modulair_apps_python application_name.

Documentation
-------------
Documenatation of the library can be found at http://cs.jhu.edu/~pchalas1/pythonLibDoc/annotated.html


Please mail pchalas1@hotmail.com to report any kind of bugs
