import numpy as np
from spacetime.potential import Potential

class DistortedSchwarzschild(Potential):
    def __init__(self, theta=np.pi/2, l=3.8, o=1, r_range=(2, 20),
                 num=10000, cont_without_eq=False, verbose=True):
        super().__init__(r_range=r_range, num=num,
                         cont_without_eq=cont_without_eq, verbose=verbose)
        self.theta = theta
        self.l = l
        self.o = o

    def compute_w(self):
        exponent = 0.5 * self.o * ( 3*self.r**2*np.cos(self.theta)**2 - \
                                    6*self.r*np.cos(self.theta)**2 + \
                                    2*np.cos(self.theta) - self.r**2 -2*self.r)

        oben = (self.r**2 - self.r*2) * np.sin(self.theta)**2
        unten = np.exp(-2*exponent) * self.r**2 * np.sin(self.theta)**2 - \
                self.l**2 * np.exp(2*exponent) * (1 - 2/self.r)

        w = 0.5 * np.log(oben/unten)

        return w
