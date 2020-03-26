import numpy as np
from spacetime.potential import Potential

class QMetric(Potential):
    def __init__(self, theta=np.pi/2, q=1.13, l=8,
                 r_range=(6, 20), num=1000, cont_without_eq=False,
                 verbose=True):
        super().__init__(r_range=r_range, num=num,
                         cont_without_eq=cont_without_eq,
                         verbose=verbose)

        self.theta = theta
        self.q = q
        self.l = l

    def compute_w(self):
        alpha = 1 - 2/self.r

        oben = alpha**(1+self.q) * self.r**2 * np.sin(self.theta)**2
        unten = -self.l**2 * alpha**(1 + 2*self.q) + self.r**2 * np.sin(self.theta)**2

        w = 0.5 * np.log(oben/unten)

        return w
