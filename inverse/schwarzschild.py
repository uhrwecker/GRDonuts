import numpy as np
from spacetime.potential import Potential

class InverseSchwarzschild(Potential):
    def __init__(self, l=3.8, w=-0.045, r_range=(2, 18),
                 num=10000, cont_without_eq=False, verbose=True):
        super().__init__(r_range=r_range, num=num,
                         cont_without_eq=cont_without_eq,
                         verbose=verbose)
        self.w = w
        self.l = l

    def compute_w(self):
        oben = self.l**2 * (2 - self.r)*np.exp(2*self.w)
        unten = (1 - np.exp(2*self.w)) * self.r**3 - 2*self.r**2
        arg = oben/unten
        res1 = np.arccos(np.sqrt(arg))
        res2 = np.arccos(-np.sqrt(arg)) - np.pi

        return np.concatenate((res2, res1))
