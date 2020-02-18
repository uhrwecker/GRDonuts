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




