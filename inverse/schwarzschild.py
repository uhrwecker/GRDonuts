import numpy as np
from inverse.inverse_potential import InversePotential

class InverseSchwarzschild(InversePotential):
    def __init__(self, w=-0.045, l=3.8, r_range=(2, 18),
                 num=10000, cont_without_eq=False, verbose=True):
        super().__init__(w, r_range=r_range, num=num,
                         cont_without_eq=cont_without_eq,
                         verbose=verbose)
        self.l = l

    def compute_theta(self):
        oben = self.l**2 * (2 - self.r)*np.exp(2*self.w)
        unten = (1 - np.exp(2*self.w)) * self.r**3 - 2*self.r**2
        arg = oben/unten
        res1 = np.arccos(np.sqrt(arg))
        res2 = np.arccos(-np.sqrt(arg)) - np.pi

        return np.concatenate((res2, res1))

    def horizon(self, theta):
        return [2 for n in range(len(theta))]
