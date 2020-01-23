import numpy as np

class Point:
    def __init__(self, coordinates=None, system=None):
        if coordinates == None:
            self.coord = np.array([[0, 0, 0]])
        else:
            self.coord = coordinates
        if system == None:
            self.sys = 'cartesian'
        else:
            self.sys = system

    def change_coord(self, new_coordinates):
        self.coord = new_coordinates
