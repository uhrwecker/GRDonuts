import numpy as np

class UtilInverse():
    def __init__(self, verbose=True):
        self.verbose = verbose

    def find_nearest_ind(self, array, value):
        index = []
        for ind in range(len(array)-1):
            if array[ind] < value and array[ind+1] > value:
                index.append(ind)
            if array[ind] > value and array[ind+1] < value:
                index.append(ind)
        return index

    def sort_array_by_column(self, array, order=['f0']):
        bits = 'i8'+',i8'*(len(array[0])-1)
        array.view(bits).sort(order=order, axis=0)
        return array

    

class UtilStability():
    def __init__(self, verbose=True):
        self.verbose = verbose

    def retrieve_extrema(self, w, r):
        self.check_for_stable_point(w, self.verbose)
        
        min_mask = np.r_[True, w[1:] < w[:-1]] & np.r_[w[:-1] < w[1:], True]
        max_mask = np.r_[True, w[1:] > w[:-1]] & np.r_[w[:-1] > w[1:], True]

        w_min = w[min_mask]
        r_min = r[min_mask]
        w_max = w[max_mask]
        r_max = r[max_mask]

        try:

            if w_min[0] == w[0]:
                w_min = np.delete(w_min, 0)
                r_min = np.delete(r_min, 0)

            if w_max[-1] == w[-1]:
                w_max = np.delete(w_max, -1)
                r_max = np.delete(r_max, -1)

            if self.verbose:
                print('Simple extremum analysis: ')
                print('- W has maximum/a at w='+str(w_max.tolist()))
                print('- W has minimum/a at w='+str(w_min.tolist()))

            return w_min.tolist(), w_max.tolist(), r_min.tolist(), r_max.tolist()
        except:
            return [0], [0], [0], [0]

    def check_for_stable_point(self, w, exit_if_not_stable=False):
        '''
        Checks if array has at least one minimum and
        its maximum is only local
        '''
        min_mask = np.r_[True, w[1:] < w[:-1]] & np.r_[w[:-1] < w[1:], True]
        max_mask = np.r_[True, w[1:] > w[:-1]] & np.r_[w[:-1] > w[1:], True]


        w_min = w[min_mask]
        w_max = w[max_mask]

##        if w_max[0] == w[0] or w_max[0] == w[1]:
##            '''
##            The potentianl comes from +inf, so its not a stable point.
##            '''
##            raise ValueError()

        if len(w_min) < 2 and len(w_max) < 2:
            '''
            The function is monotonically. There is no stable point.
            '''
            self._error_monotonically(exit_if_not_stable)

        elif len(w_min) < 1 or len(w_max) < 1:
            '''
            The function has either a local maximum OR local minimum, but not
            both, thus is not stable
            '''
            self._error_only_one_extremum(exit_if_not_stable)

        elif w_max[0] > w_max[1]:
            '''
            The potential is not closed, there is no Roche limit.
            Matter will extend into infitiy.
            '''
            self._error_no_roche_limit(exit_if_not_stable)

        elif self.verbose and len(w_min) > 1 and len(w_max) > 1:
            print('Potential is possibly stable')

        return 0

    def closure_rating_function(self, w, r):
        wmin, wmax, rmin, rmax = self.retrieve_extrema(w, r)

        int_l = np.where(r == rmax[0])[0][0]
        int_r = np.where(w > wmax[0])[0][0]

        area_func = abs(w[int_l:int_r] - wmax[-1])

        area = np.trapz(area_func)

        return area
        

    def _error_monotonically(self, flag):
        if flag:
            raise ValueError('Potential not closed, potential is monotonically.')
        else:
            if self.verbose:
                print('WARNING: Potential not closed, potential is monotonically.')
                
    def _error_only_one_extremum(self, flag):
        if flag:
            raise ValueError('Potential not closed, only has one extremum.')
        else:
            if self.verbose:
                print('WARNING: Potential not closed, only has one extremum.')


    def _error_no_roche_limit(self, flag):
        if flag:
            raise ValueError('Potential is not closed, matter extends into infinity.')
        else:
            if self.verbose:
                print('WARNING: Potential not close, no Roche limit.')
