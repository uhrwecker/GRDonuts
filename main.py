from spacetime import *
from inverse import *
from vis import *
from von_zeipel import *

import time

import matplotlib.pyplot as pl
import numpy as np

#potential = Schwarzschild(r_range=(2, 500), num=1000000)

#pott = OneParamVarPlotter()
#pott.plot(potential, 'l', (3.5, 4))

potential = QMetric(l=2.5,
                    q=-0.5050505050505050505 ,
                    r_range=(2, 1000), num=1000000)
#potential.two_parameter_variation_stability_test('q', (1, 2), 'l', (8, 10),
#                                                 num1=100, num2=100)

##pott = OneParamVarPlotter()
##pott.plot(potential, 'q', (-0.36, -0.353))
setattr(potential, 'q', -0.354165)
setattr(potential, 'l', 2.5)
pll = BeautyPlotter()
pll.plot(potential, label='l=2.5, q=-0.354165')

pot1 = InverseQMetric(l=9, w=-0.005441146888701489, q=1.23,
                     r_range=(2, 400), num=1000000)
pot2 = InverseQMetric(l=2.5, w=-0.0016239053521697056, q=-0.354165,
                      r_range=(2, 400), num=100000)
####
pll = SimplePolarPlotter()
pll.plot(pot2, ymargin=90, label='w=-0.0016239, l=2.5, q=-0.354165')
##
pm = PolarScharPlotter()
pm.plot([pot1, pot2], ['l=9, q=1.23', 'l=2.5, q=-0.354165'], ymargin=80)


#extr = potential.util.retrieve_extrema(potential.get_w(), potential.get_r())
#print(extr)

##p = QMetric(l=5, q=0.34, r_range=(2.5, 20), num=10000)
##p.one_parameter_variation_stability_test('l', (4, 6))
##
##liste = []
##for l in np.linspace(4.96, 5.11, num=5):
##    pott = QMetric(l=l, q=0.34, r_range=(2.5, 20), num=10000)
##    res = pott.util.retrieve_extrema(pott.get_w(), pott.get_r())#
##
##    maxx = InverseQMetric(l=l, q=0.33, w=res[1][0], r_range=(2.5, 20), num=10000)
##    liste.append(maxx)
##
##label = ['q=0.34, l='+str(i.l) for i in liste]
##
##pm = PolarScharPlotter()
##pm.plot(liste, label, ymargin=20)
##pot = QMetric(l=5, q=0.33, num=10000, r_range=(2.5, 20))
##
###pm = SimplePlotter()
###pm.plot(pot)
##start_time = time.time()
##print('Start calculating...')
##p = TwoParamVarPlotter()
##p.plot(pot, 'l', (0, 10), 'q', (-2, 2), num1=250, num2=250)
##print('Done; took {}s / {}min.'.format(time.time() - start_time,
##                                       (time.time() - start_time)/60))
##
#pl = ScharVZCPlotter()
#pl.plot(pot, 'r0', rs=np.linspace(0, 20, num=15, endpoint=True),
#        label='q=5')
