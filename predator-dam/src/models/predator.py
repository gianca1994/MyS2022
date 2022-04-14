class Predator:
    def __init__(self, amount=10):
        self.amount = amount
        self.mortality_rate = 0.2

    def getAmount(self) -> int:
        return self.amount

    def setAmount(self, val) -> None:
        self.amount = val

    def getMortalityRate(self) -> float:
        return self.mortality_rate

    def setMortalityRate(self, val) -> None:
        self.mortality_rate = val

    def __repr__(self):
        return 'Predator [' \
               'Amount: %r ' \
               'Mortality Rate: %r' \
               ']' % \
               (
                   self.amount,
                   self.mortality_rate
               )
