class Terrain:
    def __init__(self, maximum_cap=5000, week=1):
        self.maximum_cap = maximum_cap
        self.current_cap = 0
        self.week = week

    def getMaximumCap(self) -> int:
        return self.maximum_cap

    def setMaximumCap(self, val) -> None:
        self.maximum_cap = val

    def getCurrentCap(self) -> int:
        return self.current_cap

    def setCurrentCap(self, val) -> None:
        self.current_cap = self.maximum_cap - val

    def getWeek(self) -> int:
        return self.week

    def setWeek(self, val) -> None:
        self.week = val

    def __repr__(self):
        return 'Terrain [' \
               'Maximum cap: %r ' \
               'Current cap: %r' \
               ']' % \
               (
                   self.maximum_cap,
                   self.current_cap
               )
