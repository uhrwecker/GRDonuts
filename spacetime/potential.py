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

    def compute_w(self):
        '''
        Implement this function for your metric
        '''
        raise NotImplementedError

    def one_parameter_variation_stability_test(self, name, rang,
                                               num=1000, log_open=False):
        
        def check_for_stability(name, value):            
            setattr(self, name, value)
            self.get_w()

        print('Start the variation on {}:'.format(name))

        self.cwouteq = True
        self.util.verbose = False

        closed_values = []
        for value in np.linspace(rang[0], rang[1], num=num):
            try:
                check_for_stability(name, value)
                closed_values.append(value)
                print('- closed for {}={}!'.format(name, value))
            except:
                if log_open:
                    print('- open for {}={}.'.format(name, value))
                else:
                    pass

        if closed_values == []:
            print('No closed surfaces found for the specified range.')

        return closed_values
            
    def get_w(self):
        w = self.compute_w()
        self.util.check_for_stable_point(w, self.cwouteq)
        return w

    def get_r(self):
        return self.r

    def get_r_range(self):
        return self.r_in, self.r_out




