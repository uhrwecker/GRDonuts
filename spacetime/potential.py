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

    def get_w(self):
        w = self.compute_w()
        self.util.check_for_stable_point(w, self.cwouteq)
        return w

    def get_r(self):
        return self.r

    def get_r_range(self):
        return self.r_in, self.r_out

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

    def two_parameter_variation_stability_test(self, name1, rang1,
                                               name2, rang2, num1=1000,
                                               num2=1000, log_open=False):
        def check_for_stability(name1, value1, name2, value2):            
            setattr(self, name1, value1)
            setattr(self, name2, value2)
            self.get_w()

        self.cwouteq = True
        self.util.verbose = False

        closed_values = []
        for v1 in np.linspace(rang1[0], rang1[1], num=num1):
            row = []
            for v2 in np.linspace(rang2[0], rang2[1], num=num2):
                try:
                    check_for_stability(name1, v1, name2, v2)
                    #row.append((v1, v2))
                    row.append(1)
                    if self.verbose:
                        print('- closed for {}={} and {}={}!'.format(name1, v1,
                                                                 name2, v2))
                except:
                    row.append(np.nan)
                    if log_open:
                        if self.verbose:
                            print('- open for {}={} and {}={}.'.format(name1, v1,
                                                                   name2, v2))
                    else:
                        pass
            closed_values.append(row)
                    
        return closed_values



