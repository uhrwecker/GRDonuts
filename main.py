from spacetime import *
from inverse import *
from vis import *
from von_zeipel import *

import time

import matplotlib.pyplot as pl
import numpy as np

er = ErezRosen(q=-5, l=3.57, r_range=(2, 30), num=100000)

w = er.get_w()
r = er.get_r()

_, wm, _, _ = er.util.retrieve_extrema(w, r)

def find_intersec(x, f, g):
    idx = np.argwhere(np.diff(np.sign(f -g))).flatten()

    return x[idx[1:]]

rr = []
tt = []

rs = er.get_r()
ts = np.linspace(np.pi/2-np.pi/180 *15, np.pi/2+np.pi/180 *15, num=1000)

for theta in ts:
    setattr(er, 'theta', theta)
    w = er.compute_w()
    root = find_intersec(rs, w, wm)
    rr += root.tolist()
    tt += [theta for n in range(len(root))]

rr = np.array(rr)
tt = np.array(tt) - np.pi/2

fig = pl.figure(figsize=(10, 5))
ax = fig.add_subplot(122, projection='polar')
ax.scatter(tt, rr, s=1, label='q=-5, l=3.57')

ax.set_ylim(0, 10)from spacetime import *
from inverse import *
from vis import *
from von_zeipel import *

import time

import matplotlib.pyplot as pl
import numpy as np

er = ErezRosen(q=-5, l=3.57, r_range=(2, 30), num=100000)

w = er.get_w()
r = er.get_r()

_, wm, _, _ = er.util.retrieve_extrema(w, r)

def find_intersec(x, f, g):
    idx = np.argwhere(np.diff(np.sign(f -g))).flatten()

    return x[idx[1:]]

#ax.set_xlim(-np.pi/16, np.pi/16)
ax.set_thetamin(-15)
ax.set_thetamax(15)

ax.set_ylabel('theta')
ax.set_xlabel('r/M')

ax.legend()

pl.show()

er = ErezRosen(q=-5, l=3.57, r_range=(0, 30), num=100000)
w = er.get_w()
r = er.get_r()
    
idx = np.where(w < wm[0])

ax2.plot(r, w, label='q=-5, l=3.57')
ax2.axhline(wm[0], color='orange', ls='--', alpha=0.7)
ax2.fill_between(r[idx], w[idx], [wm[0] for n in range(len(idx))],
                color='green', alpha=0.4)

ax2.set_xlabel('r/M')
ax2.set_ylabel('W')

ax2.set_xlim(0, 10)
ax2.set_ylim(-0.065, -0.05)

ax2.legend()
##
##pl.grid()
pl.show()
