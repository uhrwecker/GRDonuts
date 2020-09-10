import numpy as np

from spacetime.potential import Potential

class ErezRosen(Potential):
    def __init__(self, theta=np.pi/2, q=0, l=3.8,
                 r_range=(3, 20), num=10000, cont_without_eq=False,
                 verbose=True):
        super().__init__(r_range=r_range, num=num,
                         cont_without_eq=cont_without_eq,
                         verbose=verbose)

        self.theta = theta
        self.q = q
        self.l = l

    def compute_w(self):
        x = self.r - 1
        y = np.cos(self.theta)

        P2 = 0.5*(3*y**2 - 1)
        Q2 = (3*x**2 - 1)/4 * np.log((x-1)/(x+1)) + 3*x/2

        f = (x - 1)/(x + 1) * np.exp(- 2*self.q * P2 * Q2)

        upper = f * np.sin(self.theta)**2 * (self.r**2 - 2*self.r)
        lower = np.sin(self.theta)**2 * (self.r**2 - 2*self.r) - \
                self.l**2 * f**2

        w = 0.5 * np.log(upper/lower)
     
        return w 
        
