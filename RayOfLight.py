import numpy as np

class RayOfLight:
    def __init__(self, point=None, direction=None):
        if point == None:
            self.P = np.array([0, 0, 0])
        else:
            self.P = point
        if direction == None:
            self.U = np.array([0, 0, 1])
        else:
            self.U = direction

    def change_P(self, new_P):
        self.P = new_P

    def exact_point(self, t):
        x_t = self.P + t * self.U
        return x_t
