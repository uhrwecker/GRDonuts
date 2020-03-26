from spacetime.schwarzschild import *
from spacetime.kerr import *
from inverse.kerr import InverseKerr
from inverse.schwarzschild import InverseSchwarzschild
from vis.simple import *
from vis.polar import *
import matplotlib.pyplot as pl

k = Kerr()
p = BeautyPlotter()
p.plot(k)

#k = [InverseSchwarzschild(w=-0.048+0.001*n, l=3.8, r_range=(2, 17)) for n in range(0, 7)]
#label = ['l=3.8, w={}'.format(str(-0.049+0.001*n)[:7]) for n in range(0, 7)]
#p = PolarScharrPlotter(figsize=(10, 10), save='./new.png')
#lc = InverseSchwarzschild(w=-0.0416, r_range=(2, 17))
#p.plot(k, label, xmargin=2, ymargin=27, horizon=True,
#       last_closed=lc, legend_loc='upper left')

k = [InverseKerr(w=-0.043+0.0004*n, a=0.5, l=4.14, r_range=(2, 18)) for n in range(0, 7)]
label = ['l=4.14, a=0.5, w={}'.format(str(-0.043+0.0004*n)[:7]) for n in range(0, 7)]
p = PolarScharrPlotter(figsize=(8, 8))
last_closed = InverseKerr(w=-0.040275, a=0.5, l=4.14, r_range=(2, 18))
p.plot(k, label, xmargin=1, ymargin=7, legend_loc='upper left',
       last_closed=last_closed, horizon=True)
