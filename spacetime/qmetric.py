import numpy as np
from spacetime.potential import Potential

class QMetric(Potential):
    def __init__(self, theta=np.pi/2, q=2, l=3.5,
                 r_range=(2, 18), num=1000, cont_without_eq=False,
                 verbose=True):
        super().__init__(r_range=r_range, num=num,
                         cont_without_eq=cont_without_eq,
                         verbose=verbose)

        self.theta = theta
        self.q = q
        self.l = l

    def compute_w(self):
        
