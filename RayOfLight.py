import numpy as np

class RayOfLight:
    def __init__(self, P, U):
        self.P = np.array([0, 0, 0])
        self.U = np.array([0, 0, 1])
