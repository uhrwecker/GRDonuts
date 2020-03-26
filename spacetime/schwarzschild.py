import numpy as np
from spacetime.potential import Potential

###################################################################

class Schwarzschild(Potential):
    def __init__(self, theta=np.pi/2, l=3.8, r_range=(2, 18), num=10000,
                 cont_without_eq=False, verbose=True):
        super().__init__(r_range=r_range, num=num,
                         cont_without_eq=cont_without_eq, verbose=verbose)
        self.theta = theta
        self.l = l

    def compute_w(self):
        oben = self.r**2 * (self.r - 2) * np.sin(self.theta)**2
        unten = self.r**3 * np.sin(self.theta)**2 - self.l**2 * (self.r - 2)

        w = 0.5 * np.log(oben/unten)

        return w

###################################################################

class SchwarzschildDeSitter(Potential):
    def __init__(self, theta=np.pi/2, l=3.8, lamda=0.00004,
                 r_range=(2, 18), num=10000, cont_without_eq=False,
                 verbose=True):
        super().__init__(r_range=r_range, num=num,
                         cont_without_eq=cont_without_eq, verbose=verbose)
        self.theta = theta
        self.l = l
        self.lamda = lamda

    def compute_w(self):
        alpha = 1 - 2/self.r - self.lamda * self.r**2
        oben = alpha * self.r**2 * np.sin(self.theta)**2
        unten = self.r**2 * np.sin(self.theta)**2 - alpha * self.l**2

        w = 0.5 * np.log(oben/unten)

        return w
