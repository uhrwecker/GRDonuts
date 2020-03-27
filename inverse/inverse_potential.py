from spacetime.potential import Potential

class InversePotential(Potential):
    def __init__(self, w, **kwargs):
        super().__init__(**kwargs)
        self.w = w

    def compute_theta(self):
        raise NotImplementedError()

    def horizon(self):
        raise NotImplementedError()

    def get_w(self):
        return w
