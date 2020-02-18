import numpy as np
from util.utility import UtilStability

class Potential():
    def __init__(self, r_range=(2, 18), num=10000, cont_without_eq=True,
                 verbose=True):
        self.r_in, self.r_out = r_range
        self.num = num
        self.r = np.linspace(self.r_in, self.r_out, num=self.num)
        self.cwouteq = cont_without_eq
        self.verbose = verbose
        self.util = UtilStability()

    def compute_w(self, *args, **kwargs):
        '''
        Implement this function for your metric
        '''
        raise NotImplementedError

    def get_r(self):
        return self.r

    def get_r_range(self):
        return self.r_in, self.r_out

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

        self.util.check_for_stable_point(w, self.cwouteq)

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

        self.util.check_for_stable_point(w, self.cwouteq)

        return w

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
