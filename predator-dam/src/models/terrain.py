class Terrain:
    def __init__(self):
        self.maximum_capacity = 5000
        self.current_capacity = 0

    def getMaximumCapacity(self) -> int:
        return self.maximum_capacity

    def setMaximumCapacity(self, val) -> None:
        self.maximum_capacity = val

    def getCurrentCapacity(self) -> int:
        return self.current_capacity

    def setCurrentCapacity(self, val) -> None:
        self.current_capacity = self.maximum_capacity - val

    def __repr__(self):
        return 'Terrain [' \
               'Maximum Capacity: %r ' \
               'Current Capacity: %r' \
               ']' % \
               (
                   self.maximum_capacity,
                   self.current_capacity
               )
