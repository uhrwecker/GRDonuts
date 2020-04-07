import numpy as np
import matplotlib.pyplot as pl
from vis.simple import Plotter

class SimplePolarPlotter(Plotter):
    def __init__(self, figsize=(10, 10), save=None):
        super().__init__(figsize=figsize, save=save)

    def plot(self, potential, label='', xmargin=0, ymargin=10):
        thetas = potential.compute_theta()
        r = potential.get_r()
        rs = np.concatenate((r, r))

        theta_max = np.nanmax(np.abs(thetas))
        pl.polar(thetas, rs, label=label)
        pl.ylim(r[0] - xmargin, r[-1] + xmargin)
        pl.xlim((-theta_max-ymargin)/180*np.pi, (theta_max+ymargin)/180*np.pi)
        pl.legend()
        
        if self.save:
            pl.savefig(self.save)
        else:
            pl.show()

class SimpleVZCPlotter(Plotter):
    def __init__(self, figsize=(10, 10), save=None):
        super().__init__(figsize=figsize, save=save)

    def plot(self, potential, label='', xmargin=0, ymargin=10):
        thetas = potential.compute_theta()
        r = potential.get_r()

        theta_max = np.nanmax(np.abs(thetas[0]))
        
        pl.polar(thetas[0], r, label=label, c='blue')
        pl.polar(thetas[1], r, label=label, c='blue')
        
        pl.ylim(r[0] - xmargin, r[-1] + xmargin)
        pl.xlim(-np.pi/2,
                np.pi/2)
        pl.legend()
        
        if self.save:
            pl.savefig(self.save)
        else:
            pl.show()


class ScharVZCPlotter(Plotter):
    def __init__(self, figsize=(10, 10), save=None):
        super().__init__(figsize=figsize, save=save)

    def plot(self, potential, name, rs, label='', xmargin=0, ymargin=10,
             horizon=True):
        for r in rs[:-1]:
            setattr(potential, name, r)
            thetas = potential.compute_theta()
            r = potential.get_r()

            theta_max = np.nanmax(np.abs(thetas[0]))
            
            pl.polar(thetas[0], r, c='blue')
            pl.polar(thetas[1], r, c='blue')

        r = rs[-1]
        setattr(potential, name, r)
        thetas = potential.compute_theta()
        r = potential.get_r()

        theta_max = np.nanmax(np.abs(thetas[0]))
            
        pl.polar(thetas[0], r, c='blue')
        pl.polar(thetas[1], r, label=label, c='blue')
        
        
        pl.ylim(r[0] - xmargin, r[-1] + xmargin)
        pl.xlim(-np.pi/2,
                np.pi/2)
        pl.legend()

        if horizon:
            vartheta = np.linspace(0, np.pi*2, num=1000, endpoint=True)
            hori = potential.horizon(vartheta)

            pl.polar(vartheta, hori, label='Horizon', c='gray')
            pl.fill_between(vartheta, 0, hori)
        
        if self.save:
            pl.savefig(self.save)
        else:
            pl.show()


class PolarScharPlotter(Plotter):
    def __init__(self, figsize=(10, 10), save=None):
        super().__init__(figsize=figsize, save=save)

    def plot(self, pot_list, label_list, xmargin=0, ymargin=0.003,
             legend_loc='best', last_closed=None, horizon=False):
        for item, label in zip(pot_list, label_list):
            thetas = item.compute_theta()
            r = item.get_r()
            rs = np.concatenate((r, r))

            theta_max = np.nanmax(np.abs(thetas))
            pl.polar(thetas, rs, label=label)

        if horizon:
            vartheta = np.linspace(0, np.pi*2, num=1000, endpoint=True)
            hori = item.horizon(vartheta)

            pl.polar(vartheta, hori, label='Horizon', c='gray')
            pl.fill_between(vartheta, 0, hori)
                

        if last_closed:
            theta = last_closed.compute_theta()
            r = last_closed.get_r()
            rs = np.concatenate((r, r))
            pl.polar(theta, rs, label='last closed surfaces at w={}'.format(last_closed.w),
                     c='black')
            
        pl.ylim(r[0] - xmargin, r[-1] + xmargin)
        pl.xlim((-theta_max-ymargin)/180*np.pi, (theta_max+ymargin)/180*np.pi)

        pl.xlabel('r/M')
        pl.ylabel('theta')
        pl.legend(loc=legend_loc)
            
        if self.save:
            pl.savefig(self.save)
        else:
            pl.show()
            
