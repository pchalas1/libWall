from OpenGL.GL import *

import numpy 

class Group(object):  
    """TODO
    """      
    def __init__(self, parent):                
        # List of objects in this group.
        self._objects = []

        # Center position of the group, in world coordinates.
        self._centralPos = numpy.zeros(4)                

        # Rotation of the group.
        self.rotation = numpy.identity(4)

        # Radius of the sphere that bounds all the objects in the group.
        self._radius = 0

        # Maximum distance between two objects in the group.
        self._maxDistance = 0

        # Indicates whether the object is rotatingScene or not.
        self.rotatingScene = False

        # Vector from the object's screen center to the point where it was clicked.
        self.fromCenter = numpy.zeros(2)

        # Maximum object size of all objects in this group.
        self.maxObjectSize = 0 

    def __iter__(self):
        """
        Object that will have the iteration items.
        """

        return self._objects.__iter__()

    def __len__(self):
        """
        Returns how many objects there are in this group.
        """

        return len(self._objects)

    def leftClickPressEvent(self, x, y):
        """
        Method called when the left mouse button is pressed.
        """
        pass

    def leftClickMoveEvent(self, x, y):
        """
        Method called when the mouse moves and the left mouse button is pressed.
        """
        pass

    def rightClickEvent(self, x, y):
        """
        Method called when the right mouse button is pressed.
        """
        pass

    def rightClickMoveEvent(self, x, y):
        """
        Method called when the mouse moves and the right mouse button is pressed.
        """
        pass

    def rightClickReleaseEvent(self, x, y):
        """
        Method called when the left mouse button is released.
        """
        pass                

    @property
    def centralPosition(self):
        """
        Center position of the group, in world coordinates.
        """

        return self._centralPos

    @centralPosition.setter
    def centralPosition(self, value):
        """
        Sets the new central position of the group, shifting all the objects' central positions.
        """
        pass

    @property
    def radius(self):
        """
        Radius of the sphere that bounds all the objects in the group.
        """

        return self._radius

    def add(self, object, autoSelect=True):
        """
        Adds an object to the group.
        """
        pass

    def remove(self, object, autoDeselect=True):
        """
        Removes an object from the group.
        """
        pass

    def removeAll(self):
        """
        Removes all objects from the group.
        """
        pass

    def updateRadiusAndCenter(self):
        """
        Updates the radius and center of the group. Also updates the maxObjectSize attribute.
        This method is O(n^2).
        """
        pass

    def render(self, pickingMode=False):
        """
        Renders the group effects. Does not render the objects.
        """
        pass
