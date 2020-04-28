from von_zeipel.vzc import VZCBase

import numpy as np

class VZCQMetric(VZCBase):
    def __init__(self, q=1, r0=4, r_range=(2, 22),
                 num=10000, verbose=True):
        super().__init__(l=0, r0=r0, r_range=r_range,
                         num=num, verbose=verbose)

        self.q = q

    def compute_theta(self):
        alpha = 1 - 2/self.r
        alpha_0 = 1 - 2/self.r0
        argument = 1/(self.r**2) * alpha**(1+2*self.q) * \
                   alpha_0**(-1-2*self.q) * self.r0**2
        theta1 = np.arccos(np.sqrt(argument))
        theta2 = np.arccos(-np.sqrt(argument)) - np.pi

        return (theta1, theta2)

    def horizon(self, theta):
        return [0.001 for n in range(len(theta))]
