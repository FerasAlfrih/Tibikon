import json


class Feast():
    def toJSON(self):
        return self.__dict__

    def __init__(self):
        self.vispers = self.Vispers()
        self.morning = self.Morning()
        self.liturgy = self.Liturgy()

    def Morning(self):
        return 'morning'

    def Vispers(self):
        return 'vispers'

    def Liturgy(self):
        return 'liturgy'


class Circle(Feast):
    def toJSON(self):
        return self.__dict__

    def __init__(self):
        self.vispers = self.Vispers()
        self.morning = self.Morning()
        self.liturgy = self.Liturgy()

    def Morning(self):
        return 'Circle morning'

    def Vispers(self):
        return 'Circle vispers'

    def Liturgy(self):
        return 'Circle liturgy'


class Star(Feast):
    def toJSON(self):
        return self.__dict__

    def __init__(self):
        self.vispers = self.Vispers()
        self.morning = self.Morning()
        self.liturgy = self.Liturgy()

    def Morning(self):
        return 'Star morning'

    def Vispers(self):
        return 'Star vispers'

    def Liturgy(self):
        return 'Star liturgy'


class Flake(Feast):
    def toJSON(self):
        return self.__dict__

    def __init__(self):
        self.vispers = self.Vispers()
        self.morning = self.Morning()
        self.liturgy = self.Liturgy()

    def Morning(self):
        return 'Flake morning'

    def Vispers(self):
        return 'Flake vispers'

    def Liturgy(self):
        return 'Flake liturgy'


class celticCross(Feast):
    def toJSON(self):
        return self.__dict__

    def __init__(self):
        self.vispers = self.Vispers()
        self.morning = self.Morning()
        self.liturgy = self.Liturgy()

    def Morning(self):
        return 'cleticCross morning'

    def Vispers(self):
        return 'cleticCross vispers'

    def Liturgy(self):
        return 'cleticCross liturgy'


class germanCross(Feast):
    def toJSON(self):
        return self.__dict__

    def __init__(self):
        self.vispers = self.Vispers()
        self.morning = self.Morning()
        self.liturgy = self.Liturgy()

    def Morning(self):
        return 'German morning'

    def Vispers(self):
        return 'German vispers'

    def Liturgy(self):
        return 'German liturgy'


class outlineCross(Feast):
    def toJSON(self):
        return self.__dict__

    def __init__(self):
        self.vispers = self.Vispers()
        self.morning = self.Morning()
        self.liturgy = self.Liturgy()

    def Morning(self):
        return 'outlineCross morning'

    def Vispers(self):
        return 'outlineCross vispers'

    def Liturgy(self):
        return 'outlineCross liturgy'


class Easter(Feast):
    def toJSON(self):
        return self.__dict__

    def __init__(self):
        self.vispers = self.Vispers()
        self.morning = self.Morning()
        self.liturgy = self.Liturgy()

    def Morning(self):
        return 'morning'

    def Vispers(self):
        return 'vispers'

    def Liturgy(self):
        return 'liturgy'
