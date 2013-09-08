Modulair Python Library
=======================

This library helps user to create applications for Balaur Wall. It is still under development, however there are some sample applications that will guide you through the library functionality.

Dependencies
------------
- Ros      : Installation guide can be found at http://wiki.ros.org/
- Pyopengl : Installation guide can be found at http://pyopengl.sourceforge.net/documentation/installation.html
- PyKDL    : Installation guide can be found at http://www.orocos.org/kdl/installation-manual

Other Dependencies of the modualir framework of the wall.

Library Files
-------------

- **gl_camera**      : Setup a camera to view a scene and display on the viewport. A camera can be placed at any point on the screen by giving it a positon of the eye,i.e camera, position of the reference point and direction of up vector.
- **gl_frame**       : Frame with a translation and a rotation. Helps to store a transformation matrix.
- **gl_vec3**		     : 3D Vector class. Helps to store a vector with functionality of a normal vector.
- **gl_group**       : **TODO**
- **gl_lighting**    : Setup lighting for the scene. Used mainly to enable single/multiple Light sources. These light sources have many properties like diffusion, ambience etc .
- **gl_material**    : This refers to the properties of an object that determine how it interacts with light. Material properties like shininess, specularity etc have to binded with the objects.
- **gl_matrix**      : **TODO**
- **gl_model**       : Helps to load a model. Right now it has an auto rotate feature.
- **gl_object**      : Currently only sphere object is available. Helps to render a sphere on the screen at specified/random position. There are some other features like collision with another sphere, direction to move the sphere etc.
- **gl_quad**        : To create a quad, which basically is a rectangle, but this quad class helps to load an image onto it.
- **gl_rect**        : Create a recatangle object. Renders a rectangle object on the screen.
- **gl_rot3x3**      : Rotation Matrix **TODO**
- **gl_utils**       : Utility class, containing basic functinality of loading a video or image etc
- **gl_wall_canvas** : Low level Wrapper of ModulairAppWidget. Parent this class to obtain Qt Context to execute your QGLWidget
- **gl_widget_base** : Low level Wrapper of Qt Opengl.QGLWidget. Parent this class to obtain OpenGL Context.


Tutorial Files
--------------

- **imgage_browser** : Simple image browser application. 
- **video_browser**  : Simple video browser application.
- **bouncing_ball**  : Fun application which display few balls and let them bounce accross the walls of the screen and with themselves.
- **model_browser**  : To load a model and display on the screen.
- **solar_system**   : Its just a testing application that can be used for bug testing. **(Not Important)**

Important Note 
-------------- 
- All the tutorial files ending with '_app.py' are the application files that creates the widget object and launces it. These files have to be given read/write/execute privelages (chmod 777 filename)

- A launch file has to be created for every application and put in the launch folder. 

- To launch the applicaiton, call roslaunch modulair_apps_python application_name.

Documentation
-------------
Documenatation of the library can be found at http://pchalas1.github.io/libWall/


Please mail pchalas1@hotmail.com to report any kind of bugs
