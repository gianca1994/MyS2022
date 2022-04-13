class Terrain:
    def __init__(self, maximum_cap=5000):
        self.maximum_cap = maximum_cap
        self.current_cap = 0

    def getMaximumCap(self) -> int:
        return self.maximum_cap

    def setMaximumCap(self, val) -> None:
        self.maximum_cap = val

    def getCurrentCap(self) -> int:
        return self.current_cap

    def setCurrentCap(self, val) -> None:
        self.current_cap = self.maximum_cap - val

    def __repr__(self):
        return 'Terrain [' \
               'Maximum cap: %r ' \
               'Current cap: %r' \
               ']' % \
               (
                   self.maximum_cap,
                   self.current_cap
               )
