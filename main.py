from spacetime.schwarzschild import *
from spacetime.kerr import *
from spacetime.qmetric import *
from inverse.kerr import InverseKerr
from inverse.schwarzschild import InverseSchwarzschild
from inverse.qmetric import InverseQMetric
from vis.simple import *
from vis.polar import *
from vis.variation import *

import time

import matplotlib.pyplot as pl

##pot = QMetric()
##
##p = BeautyPlotter()
##p.plot(pot)

s1 = time.time()

pot = [InverseQMetric(w=-0.0527-0.0002*n, r_range=(2, 20)) for n in range(8)]
label = ['l=8, q=1.13, w={}'.format(str(-0.0527-0.0002*n)[:7]) for n in range(8)]

last_closed = InverseQMetric(w=-0.052683)

p = PolarScharrPlotter(figsize=(10, 10), save='./q_polar.png')
p.plot(pot, label, ymargin=10, last_closed=last_closed)

print('It took {}s'.format(str(time.time()-s1)[:8]))

