from spacetime.schwarzschild import *
from spacetime.kerr import *
from spacetime.qmetric import *
from inverse.kerr import InverseKerr
from inverse.schwarzschild import InverseSchwarzschild
from vis.simple import *
from vis.polar import *


k = Kerr()
k.one_parameter_variation_stability_test('a', (0, 1))
#p = BeautyPlotter()
#p.plot(k, label='')
