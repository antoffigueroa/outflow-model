import numpy as np
from Point import *
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

    def change_i(self, new_i):
        self.i = new_i

    def change_pa(self, new_pa):
        self.pa = new_pa

    def change_theta(self, new_theta):
        self.theta = new_theta

    def change_V_max(self, new_V_max):
        self.V_max = new_V_max

    def calculate_D(self):
        return np.array([[0, 0, 1]])

    def calculate_M(self):
        D = self.calculate_D()
        M = np.dot(np.transpose(D), D) - np.cos(self.theta)**2*np.identity(3)
        return M

    def find_intersection_t(self, ray):
        U = ray.U
        P = ray.P
        M = self.calculate_M()
        c_0 = np.dot(np.dot(P, M), np.transpose(P))
        c_1 = np.dot(np.dot(U, M), np.transpose(P))
        c_2 = np.dot(np.dot(U, M), np.transpose(U))
        delta = c_1**2 - c_2 * c_0
        if delta < 0:
            print "No intersection points"
            return ()
        elif delta == 0:
            return (-c_1/c_2,)
        else:
            t_1 = (-c_1 + np.sqrt(delta))/c_2
            t_2 = (-c_1 - np.sqrt(delta))/c_2
            return (t_1, t_2)

    def intersection_point(self, ray):
        t = self.find_intersection_t(ray)
        if len(t)==2:
            x_1 = ray.exact_point(t[0])
            x_2 = ray.exact_point(t[1])
            return (x_1, x_2)
        if len(t)==1:
            x = ray.exact_point(t[0])
            return (x,)
        if len(t)==0:
            return ()
