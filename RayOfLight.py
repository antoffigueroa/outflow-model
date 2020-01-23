import numpy as np
from Point import *

class RayOfLight:
    def __init__(self, coordinate=None, direction=None, sys=None):
        if coordinates == None:
            self.P = Point()
        else:
            self.P = Point(coordinates=coordinate, system=sys)
        if direction == None:
            self.U = Point(coordinates=np.array([[0, 0, 1]]), system=sys)
        else:
            self.U = Point(coordinates=coordinate, system=sys)

    def change_P(self, new_P):
        self.P.change_coord(coordinates=new_P)

    def change_U(self, new_U):
        self.U.change_coord(coordinates=new_U)

    def exact_point(self, t):
        x_t = self.P + t * self.U
        return x_t
