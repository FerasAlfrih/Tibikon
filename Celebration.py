import datetime as dt
from .models import Saints


class Celebration():
    def __init__(self, date):
        self.date = date
        self.year = date.year
        self.month = date.month
        self.day = date.day
        self.easter, self.ascension, self.pentecost = self.get_easter()
        self.paschal_network = self.paschalion()

        self.is_sunday = self.isSunday()
        self.is_paschal = self.isPaschal() if self.is_sunday else False
        self.is_easter = self.isEaster() if self.is_sunday else False
        self.celb = Saints.objects.get(day=self.day, month=self.month)
        self.saint = self.celb.saint
        self.short_saint = self.celb.name

        self.is_circle = True if self.celb.feast.strip() == 'Circle' else False
        self.is_star = True if self.celb.feast.strip() == 'Star' else False
        self.is_flake = True if self.celb.feast.strip() == 'Flake' else False
        self.is_celticCross = True if self.celb.feast.strip() == 'celticCross' else False
        self.is_germanCross = True if self.celb.feast.strip() == 'germanCross' else False
        self.is_outlineCross = True if self.celb.feast.strip() == 'outlineCross' else False

        self.occasion = self.get_occasion()
        self.celebration = self.get_celebration()

    def toJSON(self):
        return self.__dict__

    def isSunday(self):
        if self.date.strftime("%A") == "Sunday":
            return True
        else:
            return False

    def isPaschal(self):
        if self.date in self.paschal_network:
            return True
        else:
            return False

    def isEaster(self):
        if self.date == self.easter:
            return True
        else:
            return False

    def get_easter(self):
        year = self.year
        silver = year % 19
        pfm = 21+(19*silver+15) % 30
        dow = (pfm+year+year//4) % 7
        easter = pfm+7-dow
        if easter > 31:
            e = easter - 31
            easter = str(year) + ',' + '4' + ',' + str(e)
        else:
            easter = str(year) + ',' + '3' + ',' + str(easter)
        Easter = dt.datetime.strptime(easter, '%Y,%m,%d').date()
        if year < 2100:
            Easter = Easter + dt.timedelta(days=13)
        else:
            Easter = Easter + dt.timedelta(days=14)
        Ascension = Easter + dt.timedelta(days=39)
        Pentecost = Easter + dt.timedelta(days=49)
        return Easter, Ascension, Pentecost

    def paschalion(self):
        easter = self.easter
        Zacchaeus = easter - dt.timedelta(days=77)
        PnPH = easter - dt.timedelta(days=70)
        PS = easter - dt.timedelta(days=63)
        LD = easter - dt.timedelta(days=56)
        SF = easter - dt.timedelta(days=49)
        lent = easter - dt.timedelta(days=48)
        orthodoxy = easter - dt.timedelta(days=42)
        GP = easter - dt.timedelta(days=35)
        cross = easter - dt.timedelta(days=28)
        ladder = easter - dt.timedelta(days=21)
        egypt = easter - dt.timedelta(days=14)
        lazarus = easter - dt.timedelta(days=8)
        palms = easter - dt.timedelta(days=7)
        GM = easter - dt.timedelta(days=6)
        GT = easter - dt.timedelta(days=5)
        GW = easter - dt.timedelta(days=4)
        GTH = easter - dt.timedelta(days=3)
        GF = easter - dt.timedelta(days=2)
        GS = easter - dt.timedelta(days=1)
        toma = easter + dt.timedelta(days=7)
        perf = toma + dt.timedelta(days=7)
        mokh = perf + dt.timedelta(days=7)
        sam = mokh + dt.timedelta(days=7)
        blond = sam + dt.timedelta(days=7)
        fef = blond + dt.timedelta(days=7)
        saints = self.pentecost + dt.timedelta(days=7)
        aps = saints + dt.timedelta(days=1)
        if (dt.date(self.date.year, 6, 29) - aps).days > 0:
            apsfast = aps
        else:
            apsfast = "لا يوجد"

        paschal_network = {}
        paschal_network[Zacchaeus] = 'أحد زكا'
        paschal_network[PnPH] = 'أحد الفريسي والعشار'
        paschal_network[PS] = 'أحد الابن الضال'
        paschal_network[LD] = 'أحد الدينونة'
        paschal_network[SF] = 'أحد الغفران'
        paschal_network[lent] = 'بدء الصوم'
        paschal_network[orthodoxy] = 'أحد الأورثذكسية'
        paschal_network[GP] = 'أحد غريغوريوس بالاماس'
        paschal_network[cross] = 'أحد الصليب'
        paschal_network[ladder] = 'أحد السلمي'
        paschal_network[egypt] = 'أحد المصرية'
        paschal_network[lazarus] = 'سبت ألعازر'
        paschal_network[palms] = 'أحد الشعانين'
        paschal_network[GM] = 'الاثنين من أسبوع الآلام'
        paschal_network[GT] = 'الثلاثاء من أسبوع الآلام'
        paschal_network[GW] = 'أربعاء الزيت'
        paschal_network[GTH] = 'خميس الأسرار'
        paschal_network[GF] = 'الجمعة العظيمة'
        paschal_network[GS] = 'سبت النور'
        paschal_network[toma] = 'أحد  توما'
        paschal_network[perf] = 'أحد حاملات الطيب'
        paschal_network[mokh] = 'أحد  المخلع'
        paschal_network[sam] = 'أحد السامرية'
        paschal_network[blond] = 'أحد الأعمى'
        paschal_network[fef] = 'fef'
        paschal_network[saints] = 'أحد جميع القديسين'
        paschal_network[apsfast] = 'صوم الرسل'
        return paschal_network

    def get_occasion(self):
        if self.is_circle or self.is_star or self.is_flake or self.is_celticCross or self.is_germanCross or self.is_outlineCross:
            return self.celb.feast
        else:
            return 'Feast'

    def get_celebration(self):

        if self.is_sunday:
            if self.is_easter:
                return "Easter"
            elif self.is_paschal:
                return "Sunday", self.paschal_network[self.date]
            else:
                return "Sunday", self.occasion
        else:
            return self.occasion
