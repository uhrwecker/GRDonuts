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

class LkQMetric():
    def __init__(self, rms=True, rmb=False):
        self.rms = rms
        self.rmb = rmb

    def _lk(self, q, r):

        alpha = 1 - 2/r

        lk_up = r * np.sqrt(q+1)
        lk_down = alpha**(1+q) * np.sqrt(r - q/alpha)

        return lk_up/lk_down

    def compute(self, q, r=None, plus=True):
        l = []

        if r:
            l.append(self._lk(q, r))

        if self.rms:
            if plus:
                r = 4+3*q + np.sqrt(5*q**2 + 10*q + 4)
            else:
                r = 4+3*q - np.sqrt(5*q**2 + 10*q + 4)
            l.append(self._lk(q, r))

        return l
            
        
            
        
