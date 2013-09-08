#!/usr/bin/env python

from wall import *

from math import pow
from math import sqrt


class ObjectTesting(GLWidget):
    def __init__(self,width, height, parent=None):        
        super(ObjectTesting, self).__init__(10)
        self.n = 1
        self.rect = [None for i in xrange(0,self.n)]            
        self._enableGlut()
        self.cam = Camera('PERSPECTIVE')        
        pass

    def paint(self):         
        for i in xrange(0,self.n):            
            self.rect[i].render()             
        pass


    def initGL(self):            
        self.cam.setEye(0,0,4)                
        self.cam.on()                
        self.rect[0] = Rectangle(-0.5, -0.5, 0, 1, 1)                
        self.rect[0].moveX(0.5)                                
                        
    def _idle(self):                    
        # self.rect[0].rotateY(2)        
        self._update_widget()        
        pass    