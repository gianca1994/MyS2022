class Dam:
    def __init__(self):
        self.amount = 500
        self.birth_rate = 0.08

    def getAmount(self) -> int:
        return self.amount

    def setAmount(self, val) -> None:
        self.amount = val

    def getBirthRate(self) -> float:
        return self.birth_rate

    def setBirthRate(self, val) -> None:
        self.birth_rate = val

    def __repr__(self):
        return 'Dam [' \
               'Amount: %r ' \
               'Birth Rate: %r' \
               ']' % \
               (
                   self.amount,
                   self.birth_rate
               )
