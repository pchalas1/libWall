
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

        super(BouncingBall, self).__init__(10)
        self.n = 4
        self.ball = [None for i in xrange(0,self.n)]            
        self._enableGlut()
        self.cam = Camera('ORTHOGRAPHIC')
        pass

    def paint(self):      

        """Overloaded function from GLWidget
        """

        for i in xrange(0,self.n): 
            # log_warn(self.ball[i].pos())
            self.ball[i].render()            
        pass


    def initGL(self):    

        """Overloaded function from GLWidget
        """

        self.cam.setEye(0,0,-2)        
        self.cam.on()        
        # self.cam.rotateAxis(90,0,1,0)

        for i in xrange(0,self.n):            
            self.ball[i] = Sphere(0.1,30,30)      
        # self.ball[0].moveX(0.6)
            self.ball[i].randomSpeedAndPos()            
        
    def idle(self):

        """Overloaded function from GLWidget
        """                           
        
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
        # self.ball[0].rotateY(2)
        self.update_widget()
        pass        