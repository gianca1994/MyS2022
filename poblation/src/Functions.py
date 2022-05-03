import modsim as ms


class Functions:
    def __init__(self, system):
        self.system = system
        self.r = self.system.alpha
        self.K = - self.system.alpha / self.system.beta

    def step_quadratic(self, pop, t):
        net_growth = self.system.alpha * pop[t] + self.system.beta * pop[t] ** 2
        print("Poblacion(%d): %.3f, Crecimiento neto: %.6f" % (t, pop[t], net_growth))
        return pop[t] + net_growth

    # New STEP_QUADRATIC:
    def step_quadratic_new(self, pop, t):
        """
        Hagamos un par de sustituciones en la ecuación para llevarla a una forma más convencional:
            r = α
            K = −α/β
        La ecuación 3.1 queda:
            ∆p = rp + (−r/K)p2
        Reordenando, tenemos la Ecuación 3.3:
            ∆p = rp(1 − p/K)
        :return:
            None
        """
        net_growth = self.r * pop[t] * (1 - (pop[t] / self.K))
        return pop[t] + net_growth

    def run_simulation(self, step_func):
        result = ms.TimeSeries()
        result[self.system.t_0] = self.system.p_0

        for t in ms.linrange(self.system.t_0, self.system.t_end):
            result[t + 1] = step_func(result, t)

        return result
