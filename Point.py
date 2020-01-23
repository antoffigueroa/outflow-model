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

    def change_system(self, new_system):
        self.sys = new_system
    
    def cart2sphe(self):
        if self.sys != 'cartesian':
            print 'ERROR: coordinates are not cartesian'
            return
        else:
            x = self.coord[0][0]
            y = self.coord[0][1]
            z = self.coord[0][2]
            r = np.sqrt(x**2 + y**2 + z**2)
            if z > 0.:
                theta = np.arctan((np.sqrt(x**2 + y**2))/z)
            elif z == 0.:
                theta = np.pi/2.
            else:
                theta = np.arctan((np.sqrt(x**2 + y**2))/z) + np.pi
            if x > 0:
                if y >= 0:
                    phi = np.arctan(y/x)
                else:
                    phi = 2*np.pi + np.arctan(y/x)
            elif x==0:
                phi = np.pi/2*np.sign(y)
            else:
                phi = np.pi + np.arctan(y/x)
