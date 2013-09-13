
#!/usr/bin/env python

from wall import *

from math import pow
from math import sqrt


class BouncingBall(GLWidget):

    """ @author Preetham Chalasani
    @brief Create few balls and let them bounce accross the walls of the screen
    """

    def __init__(self,width, height, parent=None):

        """@param width : Width of the Screen
        @param height : Height of the Screen
        """

        # Initiate Glwidget with 10 fps
        super(BouncingBall, self).__init__(10)
        self.n = 4        
        self.ball = [None for i in xrange(0,self.n)]            

        # Enable glut for creating the sphere object
        self._enableGlut()

        # Set the camera to Orthographic view
        self.cam = Camera('ORTHOGRAPHIC')
        pass


    def initGL(self):    

        """Overloaded function from GLWidget
        """

        #Set the camera eye position, so that the object can be viewed efficiently in the screen coordinates
        self.cam.setEye(0,0,-2)        

        # Switch on the camera to view the scene
        # Default camera parameters will be used if no specific parameters are defined
        self.cam.on()                

        # Create sphere objects and give it a random position and a random speed
        for i in xrange(0,self.n):            
            self.ball[i] = Sphere(0.1,30,30)              
            self.ball[i].randomSpeedAndPos()            

    def paint(self):      

        """Overloaded function from GLWidget
        """

        # Render the sphere object previously initialized
        for i in xrange(0,self.n):             
            self.ball[i].render()            
        pass
        
    def idle(self):

        """Overloaded function from GLWidget
        """                           
        
        # Check for collision in each frame and bounce them back.
    	for i in xrange(0,self.n):            
            for j in xrange(0,3):    		                
                self.ball[i].position()[j] = self.ball[i].position()[j] + self.ball[i].speed()[j]

                if (self.ball[i].position()[j] > self.ball[i].range()[j][1]) :            
                    self.ball[i].position()[j] = self.ball[i].range()[j][1]
                    self.ball[i].speed()[j] = -self.ball[i].speed()[j]                    

                elif (self.ball[i].position()[j] < self.ball[i].range()[j][0]) :
                    self.ball[i].position()[j] = self.ball[i].range()[j][0]
                    self.ball[i].speed()[j] = -self.ball[i].speed()[j]
                pass

            for k in xrange(i+1, self.n):
                self.ball[i].checkCollision(self.ball[k])
                pass
        
        # Update the widget, which basically is a call to pain function
        self.update_widget()
        pass        