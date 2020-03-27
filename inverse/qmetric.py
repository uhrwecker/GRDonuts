import numpy as np
from inverse.inverse_potential import InversePotential

class InverseQMetric(InversePotential):
    def __init__(self, l=8, w=-0.053, q=1.13, r_range=(2, 20),
                 num=10000, cont_without_eq=False, verbose=True):
        super().__init__(w, r_range=r_range, num=num,
                         cont_without_eq=cont_without_eq,
                         verbose=verbose)
        self.l = l
        self.q = q

    def compute_theta(self):
        beta = np.exp(2*self.w)
        alpha = 1 - 2/self.r

        oben = beta * self.l**2 * alpha**(1+2*self.q)
        unten = beta * self.r**2 - alpha**(1+self.q) * self.r**2

        arg = oben/unten
        res1 = np.arccos(np.sqrt(arg))
        res2 = np.arccos(-np.sqrt(arg))- np.pi

        return np.concatenate((res2, res1))

    def horizon(self, theta):
        raise NotImplementedError('There is no horizon for a naked singularity.')
        
