import numpy as np
import matplotlib.pyplot as pl

class Plotter():
    def __init__(self, figsize=(10, 8), save=None):
        self.figure = pl.figure(figsize=figsize)
        self.save = save

    def plot(self, potential, *args, label='', xmargin=0, ymargin=0.003):
        raise NotImplementedError()

    def _adjust_plot(self, r, xm, ym, wmin, wmax, ax):
        ax.set_xlim(r[0]-xm, r[-1]+xm)
        ax.set_ylim(wmin-ym, wmax+ym)
        ax.set_xlabel('R/M')
        ax.set_ylabel('W')
        ax.legend()

class SimplePlotter(Plotter):
    def __init__(self, figsize=(10, 8), save=None):
        super().__init__(figsize=figsize, save=save)

    def plot(self, potential, label='', xmargin=0, ymargin=0.003):
        w = potential.get_w()
        r = potential.get_r()
        wmin, wmax, _, _ = potential.util.retrieve_extrema(w, r)
        pl.plot(r, w, label=label)
        self._adjust_plot(r, xmargin, ymargin, wmin[0], wmax[0])
        if self.save:
            pl.savefig(self.save)
        else:
            pl.show()


class ScharPlotter(Plotter):
    def __init__(self, figsize=(10, 8), save=None, show=True,
                 max_show=False):
        super().__init__(figsize=figsize, save=save)

    def plot(self, pot_list, label_list, xmargin=0, ymargin=0.003):
        yminmin = 1000
        ymaxmax = -1000
        for item, label in zip(pot_list, label_list):
            w = item.get_w()
            r = item.get_r()
            wmin, wmax, _, _ = item.util.retrieve_extrema(w, r)
            pl.plot(r, w, label=label)
            if wmin[0] < yminmin:
                yminmin = wmin[0]
            if wmax[0] > ymaxmax:
                ymaxmax = wmax[0]
        self._adjust_plot(r, xmargin, ymargin, wmin[0], wmax[0])
        if self.save:
            pl.savefig(self.save)
        else:
            pl.show()
    

class BeautyPlotter(Plotter):
    def __init__(self, figsize=(10, 8), save=None, show=True):
        super().__init__(figsize=figsize, save=save)

    def plot(self, potential, label='', xmargin=0, ymargin=0.003,
             show=True, fill=True, max_show=True, ax=None):
        if not ax:
            ax = pl.gca()
        r = potential.get_r()
        w = potential.get_w()
        wmin, wmax, rmin, rmax = potential.util.retrieve_extrema(w, r)
        try:
            int_l = np.where(r == rmax[0])[0][0]
        except:
            int_l = np.where(r == rmax[0])[0]
        try:
            int_r = np.where(w > wmax[0])[0][0]
        except:
            raise ValueError('Increase r_range.')
        
        if max_show:
            ax.axhline(wmax, alpha=0.5, c='red', ls='--')
        if fill:
            if int_l < int_r:
                ax.fill_between(r[int_l:int_r], [wmax[0] for n in r[int_l:int_r]],
                                w[int_l:int_r], color='green', alpha=0.4)
            else:
                ax.fill_between(r[int_r:int_l], [wmax[0] for n in r[int_r:int_l]],
                                w[int_r:int_l], color='green', alpha=0.4)
        ax.plot(r, w, label=label)
        self._adjust_plot(r, xmargin, ymargin, wmin[0], wmax[0], ax)

        if self.save:
            pl.savefig(self.save)
        if show:
            return ax

    

    
