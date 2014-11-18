Modulair Python Library
=======================

This library helps user to create applications for Balaur Wall. It is still under development, however there are some sample applications that will guide you through the library functionality. [**Read more**](http://www.cs.jhu.edu/balaur/about.html) about the Balaur Display Wall

Dependencies
------------
- Ros      : Installation guide can be found [**here**](http://wiki.ros.org/)
- Python   : Installation guide can be found [**here**](http://www.python.org/getit/)
- Numpy    : Installation guide can be found [**here**](http://docs.scipy.org/doc/numpy/user/install.html)
- Pyopengl : Installation guide can be found [**here**](http://pyopengl.sourceforge.net/documentation/installation.html)
- PyKDL    : Installation guide can be found [**here**](http://www.orocos.org/kdl/installation-manual)
- OpenCV   : Installation guide can be found [**here**](http://opencv.willowgarage.com/wiki/InstallGuide)

Other Dependencies of the modualir framework of the wall.

Library Files
-------------

- **gl_camera**      : Setup a camera to view a scene and display on the viewport. A camera can be placed at any point on the screen by giving it a positon of the eye,i.e camera, position of the reference point and direction of up vector. [**Learn more**](http://www.opengl.org/archives/resources/faq/technical/viewing.htm)
- **gl_frame**       : Frame with a translation and a rotation. Helps to store a transformation matrix.
- **gl_vec3**        : 3D Vector class. Helps to store a vector with the same functionality as of a normal vector.
- **gl_group**       : **TODO**
- **gl_lighting**    : Setup lighting for the scene. Used mainly to enable single/multiple Light sources. These light sources have many properties like diffusion, ambience etc . [**Learn more**](http://www.opengl.org/archives/resources/faq/technical/lights.htm)
- **gl_material**    : This refers to the properties of an object that determine how it interacts with light. Material properties like shininess, specularity etc have to binded with the objects. [**Learn more**](http://www.glprogramming.com/red/chapter05.html)
- **gl_matrix**      : **TODO**
- **gl_model**       : Helps to load a model. Right now it has an auto rotate feature. 
- **gl_object**      : Currently only sphere object is available. Helps to render a sphere on the screen at specified/random position. There are some other features like collision with another sphere, direction to move the sphere etc. [**Learn more**](http://www.opengl.org/documentation/specs/glut/spec3/node81.html)
- **gl_quad**        : To create a quad, which basically is a rectangle object, but quad class helps to load an image onto it. (No image can be directly rendered on the screen, it has to be rendered over a quad) [**Learn more**](http://www.opengl.org/wiki/Primitive)
- **gl_rect**        : Create a recatangle object. Renders a rectangle object on the screen.
- **gl_rot3x3**      : Rotation Matrix **TODO**
- **gl_utils**       : Utility class, containing basic functinality of loading a video or image etc.
- **gl_wall_canvas** : Low level Wrapper of ModulairAppWidget. Parent this class to obtain Qt-Context to execute your QGLWidget. [**Learn more**](http://qt-project.org/doc/qt-5.0/qtopengl/qglwidget.html)
- **gl_widget_base** : Low level Wrapper of Qt Opengl.QGLWidget. Parent this class to obtain OpenGL Context.


Tutorial Files
--------------

- **imgage_browser** : Simple image browser application. 
- **video_browser**  : Simple video browser application.
- **bouncing_ball**  : Fun application which display few balls and let them bounce accross the walls of the screen and with themselves.
- **model_browser**  : To load a model and display on the screen.
- **solar_system**   : Its just a testing application that can be used for bug testing. **(Not Important)**
- **object_testing** : It is also  a testing application that can be used for bug testing. **(Not Important)**

Important Note 
-------------- 
- To use the library, download modulair framework. Then create a rospackage for your development. Refer [**this**](http://wiki.ros.org/ROS/Tutorials/CreatingPackage), to create a ros package. 
- After creating the ropackage include the dependencies(rospy, kdl, modulair_core) in the manifest.xml and rosmake the package.
- Copy the folder launch into the rospackage. Create a folder 'scripts' in the packge and copy all the tutorial files into that folder. Create a folder 'wall' and copy all library files into that folder. 
- All the tutorial files ending with '_app.py' are the application files that creates the widget object and launces it. These files have to be given read/write/execute privelages (chmod 777 filename)
- To launch the applicaiton, make sure roscore is running. Then call roslaunch modulair_core modulair_core_laptop.launch, so that ros parameters are set. Finally call roslaunch Package_name application_name.launch


Documentation
-------------
Documenatation of the library can be found [**here**](http://pchalas1.github.io/libWall/)

Reference Material
------------------
- [**Opengl Red Book**](http://www.glprogramming.com/red/)
- [**Opengl Super Bible**](http://www.win.tue.nl/~ymazuryk/books/OpenGL_SB.pdf)
