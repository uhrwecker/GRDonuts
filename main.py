from spacetime.schwarzschild import *
from spacetime.kerr import *
from spacetime.qmetric import *
from inverse.kerr import InverseKerr
from inverse.schwarzschild import InverseSchwarzschild
from vis.simple import *
from vis.polar import *

import matplotlib.pyplot as pl


k = QMetric(r_range=(2, 30), verbose=True)
k.two_parameter_variation_stability_test('q', (-5, 5), 'l', (0, 15),
                                         num1=50, num2=50)

k = QMetric()
p = BeautyPlotter()
p.plot(k, label='')
