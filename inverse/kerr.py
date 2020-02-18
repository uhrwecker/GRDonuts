import numpy as np
from spacetime.potential import Potential

class InverseKerr(Potential):
    def __init__(self, w=-0.0042, a=0.5, l=4.14,
                 r_range=(2, 18), num=10000, cont_without_eq=False,
                 verbose=True):
        super().__init__(r_range=r_range, num=num,
                         cont_without_eq=cont_without_eq,
                         verbose=verbose)

        self.w = w
        self.a = a
        self.l = l

    def compute_w(self):
        Delta = self.r**2 - 2*self.r + self.a**2
        alpha = np.exp(2*self.w)
        beta = self.r**2 * (self.r**2 + self.a**2)
        gamma = self.a**2 * (self.r**2 + self.a**2)
        delta = 2*self.r*self.a**2
        eps = 4 * self.r * self.a * self.l
        lamda = self.r**2 * Delta / alpha
        nu = self.a**2 * Delta / alpha
        sigma = delta + nu - gamma
        mu = lamda + nu - beta - gamma - eps - self.a**2*self.l**2

        first_root = mu**2 + 4 * sigma * Delta * self.l**2
        pq = (mu + np.sqrt(first_root)) / (2 * sigma)

        sin_theta = np.sqrt(pq)
        res1 = np.arcsin(sin_theta) - np.pi/2
        sin_theta = - np.sqrt(pq)
        res2 = np.arcsin(sin_theta) - 3* np.pi/2
        return np.concatenate((res2, res1))
