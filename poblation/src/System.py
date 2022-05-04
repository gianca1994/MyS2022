import modsim as ms


class MSystem:
    def __init__(self, t_0, t_end, p_0, p_end):
        self.t_0 = t_0
        self.t_end = t_end
        self.p_0 = p_0
        self.p_end = p_end
        self.birth_rate = 0.027
        self.mortality_rate = 0.01
        self.annual_growth = self.p_end - self.p_0 / self.t_end - self.t_0
        self.alpha = 0.025
        self.beta = -0.0018

    def __repr__(self):
        return ms.System(
            t_0=self.t_0,
            t_end=self.t_end,
            annual_growth=self.annual_growth,
            p_0=self.p_0,
            birth_rate=self.birth_rate,
            mortality_rate=self.mortality_rate
        )
