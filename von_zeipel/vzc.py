import numpy as np

'''
Label any new implementation of von-Zeipel cylinders in another spacetime
by prefixing VZC, followed by the id of the spacetime.
'''

class VZCBase():
    def __init__(self, l, r0, r_range=(2, 18),
                 num=10000, verbose=True):
        self.r_in, self.r_out = r_range
        self.num = num
        self.r = np.linspace(self.r_in, self.r_out,
                             num=self.num, endpoint=True)
        self.verbose = verbose

        self.l = l
        self.r0 = r0


    def compute_theta(self):
        raise NotImplementedError()

    def horizon(self, theta):
        raise NotImplementedError()

    def get_r(self):
        return self.r

    def get_r0(self):
        return self.r0

    def set_r0(self, r_new):
        self.r0 = r_new
