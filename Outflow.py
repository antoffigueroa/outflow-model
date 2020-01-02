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
            self.theta = np.deg2grad(60)
        else:
            self.theta = np.deg2grad(theta)
        if V_max == None:
            self.V_max = 100
        else:
            self.V_max = V_max
