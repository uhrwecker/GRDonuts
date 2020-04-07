from spacetime import *
from inverse import *
from vis import *
from von_zeipel import *


import time

import matplotlib.pyplot as pl
import numpy as np

pot = VZCQMetric(q=5, num=100000, r_range=(0, 20))

pl = ScharVZCPlotter()
pl.plot(pot, 'r0', rs=np.linspace(0, 20, num=15, endpoint=True),
        label='q=5')
