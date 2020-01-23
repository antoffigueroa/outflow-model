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
        new_coord = np.array([[r, theta, phi]])
        self.change_coord(new_coord)
        self.change_system('spherical')

    def sphe2cyl(self):
        if self.sys != 'spherical':
            print 'ERROR: coordinates are not spherical'
            return
        else:
            r = self.coord[0][0]
            theta = self.coord[0][1]
            phi = self.coord[0][2]
            rho = r*np.sin(theta)
            z = r*np.cos(theta)
        new_coord = np.array([[rho, phi, z]])
        self.change_coord(new_coord)
        self.change_system('cylindrical')

    def cyl2cart(self):
        if self.sys != 'cylindrical':
            print 'ERROR: coordinates are not cylindrical'
            return
        else:
            rho = self.coord[0][0]
            phi = self.coord[0][1]
            z = self.coord[0][2]
            x = rho*np.cos(phi)
            y = rho*np.sin(phi)
        new_coord = np.array([[x, y, z]])
        self.change_coord(new_coord)
        self.change_system('cartesian')

    def cart2cyl(self):
        if self.sys != 'cartesian':
            print 'ERROR: coordinates are not cartesian'
            return
        else:
            x = self.coord[0][0]
            y = self.coord[0][1]
            z = self.coord[0][2]
            rho = np.sqrt(x**2 + y**2)
            if x == 0 and y == 0:
                phi = 0
            elif x >= 0:
                phi = np.arcsin(y/rho)
            else:
                phi = -np.arcsin(y/rho) + np.pi
        new_coord = np.array([[rho, phi, z]])
        self.change_coord(new_coord)
        self.change_system('cylindical')

    def cyl2sphe(self):
        if self.sys != 'cylindrycal':
            print 'ERROR: coordinates are not cylindrical'
            return
        else:
            rho = self.coord[0][0]
            phi = self.coord[0][1]
            z = self.coord[0][2]
            r = np.sqrt(rho**2 + z**2)
            theta = np.arctan(rho/z)
        new_coord = np.array([[r, theta, phi]])
        self.change_coord(new_coord)
        self.change_system('spherical')

    def sphe2cart(self):
        if self.sys != 'spherical':
            print 'ERROR: coordinates are not spherical'
            return
        else:
            r = self.coord[0][0]
            theta = self.coord[0][1]
            phi = self.coord[0][2]
            x = r*np.sin(theta)*np.cos(phi)
            y = r*np.sin(theta)*np.sin(phi)
            z = r*np.cos(theta)
        new_coord = np.array([[x, y, z]])
        self.change_coord(new_coord)
        self.change_system('cartesian')
