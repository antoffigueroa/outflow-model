import numpy as np
from RayOfLight import *

class Outflow:
    def __init__(self, inclination=None, p_a=None, theta=None, V_max=None):
        if inclination == None:
            self.i = 0
        else:
            self.i = inclination
        if p_a == None:
            self.pa = 0
        else:
            self.pa = p_a
        if theta == None:
            self.theta = np.deg2rad(60)
        else:
            self.theta = np.deg2rad(theta)
        if V_max == None:
            self.V_max = 100
        else:
            self.V_max = V_max

    def change_i(self, inclination):
        self.i = inclination

    def change_pa(self, p_a):
        self.pa = p_a

    def change_theta(self, theta):
        self.theta = theta

    def change_V_max(self, V_max):
        self.V_max = V_max

    def calculate_D(self):
        return np.array([0, 0, 1])

    def calculate_M(self):
        D = self.calculate_D()
        M = np.dot(np.transpose(D), D) - np.cos(self.theta)**2*np.identity(3)
        return M

    def find_intersection_t(self, ray):
        U = ray.U
        P = ray.P
        M = self.calculate_M()
        c_0 = np.dot(np.dot(np.transpose(P), M), P)
        c_1 = np.dot(np.dot(np.transpose(U), M), P)
        c_2 = np.dot(np.dot(np.transpose(U), M), U)
        delta = c_1**2 - c_2 * c_0
        if delta < 0:
            print "No intersection points"
            return
        elif delta == 0:
            return -c_1/c_2
        else:
            t_1 = (-c_1 + np.sqrt(c_1**2 - c_2*c_0))/c_2
            t_2 = (-c_1 - np.sqrt(c_1**2 - c_2*c_0))/c_2
            return (t_1, t_2)

    def intersection_point(self, ray):
        (t_1, t_2) = self.find_intersection_t(ray)
        x_1 = ray.exact_point(t_1)
        x_2 = ray.exact_point(t_2)
        return (x_1, x_2)
