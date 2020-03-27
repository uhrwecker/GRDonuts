from spacetime.schwarzschild import *
from spacetime.kerr import *
from spacetime.qmetric import *
from inverse.kerr import InverseKerr
from inverse.schwarzschild import InverseSchwarzschild
from vis.simple import *
from vis.polar import *
from vis.variation import *

import matplotlib.pyplot as pl


k = Kerr(verbose=True, r_range=(2, 200))
values = k.one_parameter_variation_stability_test('l', (3, 5), num=1000)

p = TwoParamVarPlotter()
p.plot(k, 'a', (-1, 1), 'l', (-10, 10), num1=100, num2=100)



