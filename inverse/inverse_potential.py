from spacetime.potential import Potential

class InversePotential(Potential):
    def __init__(w, **kwargs):
        super().__init__(**kwargs)

    def compute_theta(self):
        raise NotImplementedError()

    def horizon(self):
        raise NotImplementedError()

    def get_w(self):
        return w
