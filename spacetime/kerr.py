import numpy as np
from spacetime.potential import Potential

###################################################################

class Kerr(Potential):
    def __init__(self, theta=np.pi/2, a=0.5, l=4.14,
                 r_range=(2, 18), num=10000, cont_without_eq=False,
                 verbose=True):
        super().__init__(r_range=r_range, num=num,
                       cont_without_eq=cont_without_eq, verbose=verbose)
        self.theta = theta
        self.a = a
        self.l = l

    def compute_w(self):
        delta = self.r**2 - 2*self.r + self.a**2
        sigma = self.r**2 + self.a**2*np.cos(self.theta)**2
        zaehler = sigma * delta * np.sin(self.theta)**2
        b = self.r**2 * sigma *np.sin(self.theta)**2
        c = self.a**2 * sigma *np.sin(self.theta)**2
        d = 2*self.r*self.a *np.sin(self.theta)**4
        e = 4*self.l*self.r*self.a *np.sin(self.theta)**2
        f = -delta * self.l**2
        g = self.l**2 * self.a**2 *np.sin(self.theta)**2
        nenner = b+c+d+e+f+g
        
        w = -0.5*np.log(nenner/zaehler)

        self.util.check_for_stable_point(w, self.cwouteq)
        
        return w
