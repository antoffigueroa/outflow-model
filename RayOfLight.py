import numpy as np

class RayOfLight:
    def __init__(self, point=None, direction=None):
        if point == None:
            self.P = np.array([0, 0, 0])
            self.U = np.array([0, 0, 1])
        else:
            self.P = point
            self.U = direction
