from .easter_calculater import Easter


class network():
    def __init__(self, year):
        self.EASTER, self.Ascension, self.Pentecost = Easter(year)

    def triodion(self):
        pass

    def pentextarion(self):
        pass

    def daily_readings(self):
        pass

    def non_static_celebrations(self):
        pass
