import datetime as dt
import xml.etree.ElementTree as etree
from . import bible


class Feast():

    def __init__(self, serv, date):
        self.serv = serv
        self.d = date
        self.date = self.dater(self.d, self.serv)
        self.Easter, self.Ascension, self.Pentecost = self.easter(self.d)
        self.Zacchaeus, self.PnPH, self.PS, self.LD, self.SF, self.lent, self.orthodoxy, self.GP, self.cross, self.ladder, self.egypt, self.lazarus, self.palms, self.GM, self.GT, self.GW, self.GTH, self.GF, self.GS, self.toma, self.perf, self.mokh, self.sam, self.blond, self.fef, self.saints, self.apsfast = self.paschalion(
            self.Easter)
        self.feast, self.sink = self.feast(self.date)
        self.level = self.leveler()
        self.service = self.service()
        self.tone, self.iothina, self.pentaweek = self.toner()
        self.bireading, self.letreading = self.biread()

    def easter(self, date):
        year = date.year
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

    def paschalion(self, easter):

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
        saints = self.Pentecost + dt.timedelta(days=7)
        aps = saints + dt.timedelta(days=1)
        if (dt.date(self.date.year, 6, 29) - aps).days > 0:
            apsfast = aps
        else:
            apsfast = "لا يوجد"

        return Zacchaeus, PnPH, PS, LD, SF, lent, orthodoxy, GP, cross, ladder, egypt, lazarus, palms, GM, GT, GW, GTH, GF, GS, toma, perf, mokh, sam, blond, fef, saints, apsfast

    def is_sunday(self, date, service):
        if date.strftime("%A") == "Sunday" and service != "Vespers":
            return True
        elif date.strftime("%A") == "Saturday" and service == "Vespers":
            return True
        else:
            return False

    def dater(self, d, service):
        if service == "Vespers":
            date = d + dt.timedelta(days=1)
        else:
            date = d
        return date

    def leveler(self):
        lev = []
        if self.is_sunday(self.d, self.serv):
            lev.append('X')
        if self.feast == "":
            f = "ZZ"
        else:
            f = self.feast
        f = ''.join(f.split())
        lev.append(f)
        level = ""
        for ele in lev:
            level += ele

        return level

    def toner(self):
        date = self.date
        easter = self.Easter
        pentecost = self.Pentecost
        if date < easter:
            d = date - dt.timedelta(days=365)
            easter, a, pentecost = self.easter(d)
        tones = ['الأول', 'الثاني', 'الثالث', 'الرابع',
                 'الخامس', 'السادس', 'السابع', 'الثامن']
        iothinas = ['الأولى', 'الثانية', 'الثالثة', 'الرابعة', 'الخامسة',
                    'السادسة', 'السابعة', 'الثامنة', 'التاسعة', 'العاشرة', 'الحادية عشرة']
        delta = date - easter
        delta = (delta.days / 7)
        tone = tones[(int(delta) % 8) - 1]
        idelta = date - pentecost
        pentaweek = int(idelta.days / 7)
        if date == easter:
            iothina = iothinas[1]
        elif date == self.toma:
            iothina = iothinas[0]
        elif date == self.perf:
            iothina = iothinas[3]
        elif date == self.mokh:
            iothina = iothinas[4]
        elif date == self.sam:
            iothina = iothinas[6]
        elif date == self.blond:
            iothina = iothinas[7]
        elif date == self.fef:
            iothina = iothinas[9]
        elif date == self.palms:
            iothina = "للعيد"
        elif date == self.Easter:
            iothina = "للعيد"
        elif date == self.Pentecost:
            iothina = "للعيد"
        elif date.day == 2 and date.month == 2:
            iothina = "للعيد"
        elif date.day == 6 and date.month == 8:
            iothina = "للعيد"
        elif date.day == 25 and date.month == 3:
            iothina = "للعيد"
        elif date.day == 8 and date.month == 9:
            iothina = "للعيد"
        elif date.day == 14 and date.month == 9:
            iothina = "للعيد"
        elif date.day == 21 and date.month == 11:
            iothina = "للعيد"
        elif date.day == 15 and date.month == 8:
            iothina = "للعيد"
        else:
            iothina = iothinas[(pentaweek % 11) - 1]
        return tone, iothina, pentaweek

    def service(self):
        if self.serv == "Vespers":
            service = Vespers(self.level)
            return service
        if self.serv == "sahar":
            service = sahar(self.level)
            return service
        if self.serv == "divineLiturgie":
            service = divineLiturgie(self.level)
            return service
        if self.serv == "firstHour":
            service = firstHour(self.level)
            return service
        if self.serv == "thirdHour":
            service = thirdHour(self.level)
            return service
        if self.serv == "sixthHour":
            service = sixthHour(self.level)
            return service
        if self.serv == "ninethHour":
            service = ninethHour(self.level)
            return service
        if self.serv == "Midnight":
            service = Midnight(self.level)
            return service

    def feast(self, date):
        d = "a" + str(date.day)
        m = date.strftime("%B")
        tree = etree.parse("static/files/calendar.xml")
        root = tree.getroot()
        for node in root:
            month = str(node).split(" ")[1]
            month = month.replace("\'", "")
            month = month.capitalize()
            if month == m:
                day = node.find(d)
                i = node.find(d)[0].text
                i = i.replace("\"", "")
                i = i.replace(" ", "")
                k = node.find(d)[1].text
                day = str(day).split(" ")[1]
                day = day.replace("a", "")
                day = day.replace("\'", "")
            else:
                i = ""
                k = ""
            return i, k

    def daterange(self, date1, date2):
        for n in range(int((date2 - date1).days)+1):
            yield date1 + dt.timedelta(n)

    def biread(self):
        day, month = self.date.day, self.date.month
        easter = self.Easter
        date = self.date
        penta = self.Pentecost
        holyCross = dt.datetime.strptime(
            str(date.year) + ",9,14", "%Y,%m,%d").date()
        fridayhc = 4 - holyCross.weekday()
        if fridayhc <= 0:
            fridayhc += 7
        fridayhc = holyCross + dt.timedelta(fridayhc)
        sundayhc = 6 - holyCross.weekday()
        if sundayhc <= 0:
            sundayhc += 7
        sundayhc = holyCross + dt.timedelta(sundayhc)

        print(sundayhc)
        John = [day for day in self.daterange(easter, penta)]
        Mathew = [day for day in self.daterange(
            penta + dt.timedelta(days=1), fridayhc)]
        d = date + dt.timedelta(days=365)
        Easter, a, pentecost = self.easter(d)
        Zacchaeus, PnPH, PS, LD, SF, lent, orthodoxy, GP, cross, ladder, egypt, lazarus, palms, GM, GT, GW, GTH, GF, GS, toma, perf, mokh, sam, blond, fef, saints, apsfast = self.paschalion(
            Easter)
        Luke = [day for day in self.daterange(
            sundayhc + dt.timedelta(days=1), PS)]
        print(PS)
        print("John=", len(John)/7)
        print("Mathew=", len(Mathew)/7)
        print("Luke=", len(Luke)/7)
        a = '2021,09,19'
        b = '2022,02,20'
        d = [n for n in self.daterange(dt.datetime.strptime(
            a, '%Y,%m,%d'), dt.datetime.strptime(b, '%Y,%m,%d'))]
        print(len(d)/7)
        bireading = letreading = ""
        return bireading, letreading


class Vespers():

    def __init__(self, level):
        self.level = level

        def func_not_found():  # just in case we dont have the function
            print('No Function '+self.level+' Found!')
        func = getattr(self, self.level, func_not_found)
        self.service, self.pieces, self.fdoxa, self.prokiminon, self.readings, self.apostikn, self.apdoxa, self.serv = func()

    def XX(self):
        service = "الفصح"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def WW(self):
        service = "Sayiedi"
        tone = "لحن العيد"
        pieces = ""
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def VV(self):
        service = "Waldi"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def YY(self):
        service = "MumtazG"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def YW(self):
        service = "MumtazW"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def YV(self):
        service = "MumtazN"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def ZZ(self):
        service = "قديس يومي"
        tone = "لحن الأسبوع"
        pieces = "3 معزي + 3 ميناون"
        fdoxa = "لا يوجد"
        prokiminon = "السواعي"
        readings = "لا يوجد"
        apostikn = "المعزي"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def YVY(self):
        service = "MumtazWE"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XZZ(self):
        service = "قيامة مع عيد غير ممتاز"
        tone = "لا يوجد"
        pieces = "7 معزي + 3 ميناون "
        fdoxa = "ذكصا كانين معزي"
        prokiminon = "الرب قد ملك"
        readings = "لا يوجد"
        apostikn = "معزي"
        apdoxa = "ذكصا  كانين للحن"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + readings + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XWW(self):
        service = "QS"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XVV(self):
        service = "QW"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XYY(self):
        service = "QMG"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XYW(self):
        service = "QMW"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XYV(self):
        service = "QMN"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def WV(self):
        service = "SW"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def WYY(self):
        service = "SMG"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def WYW(self):
        service = "SMW"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def WYV(self):
        service = "SMN"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def VYY(self):
        service = "WMG"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def VYW(self):
        service = "WMW"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def VYV(self):
        service = "WMN"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def YYY(self):
        service = "2MG"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def YYW(self):
        service = "GW"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def YYV(self):
        service = "GN"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def YWW(self):
        service = "2MW"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def YWV(self):
        service = "WN"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def YVV(self):
        service = "2MN"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def ZV(self):
        service = "+W"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def ZW(self):
        service = "+S"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def ZX(self):
        service = "+Q"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def ZY(self):
        # self.zz()
        service = "قديس يومي"
        tone = " الميناون"
        pieces = "6 ميناون"
        fdoxa = "المعزي"
        prokiminon = "السواعي"
        readings = "لا يوجد"
        apostikn = "المعزي"
        apdoxa = "المعزي"
        serv = "اللحن: " + tone + " -قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def VY(self):
        service = "-W"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def YYZ(self):
        service = "-MG"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def WY(self):
        service = "-S"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XY(self):
        service = "-Q"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XWV(self):
        service = "QSW"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XWYY(self):
        service = "QSMG"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XWYW(self):
        service = "QSMW"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XWYV(self):
        service = "QSMN"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XVYY(self):
        service = "QWMG"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XVYW(self):
        service = "QWMW"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XVYV(self):
        service = "QWMN"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XYYY(self):
        service = "Q2MG"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XYYW(self):
        service = "QGW"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XYYV(self):
        service = "QGN"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XYWW(self):
        service = "Q2MW"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XYWV(self):
        service = "QWN"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XYVV(self):
        service = "Q2MN"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XZV(self):
        service = "Q+W"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XZW(self):
        service = "Q+S"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XZX(self):
        service = "Q+Q"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XZY(self):
        service = "QN+"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XVY(self):
        service = "Q-W"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XYYZ(self):
        service = "Q-MG"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XWY(self):
        service = "Q-S"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XXY(self):
        service = "Q-Q"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv

    def XYVY(self):
        service = "QMumtazWE"
        tone = "لا يوجد"
        pieces = "لا يوجد"
        fdoxa = "لا يوجد"
        prokiminon = "لا يوجد"
        readings = "لا يوجد"
        apostikn = "لا يوجد"
        apdoxa = "لا يوجد"
        serv = "اللحن: " + tone + " - قطع الغروب: " + pieces + " - الذكصا: " + fdoxa + " - البروكيمينون: " + \
            prokiminon + " - القراءات: " + \
            str(readings) + " - الأبوستيخن: " + \
            apostikn+" - ذكصا الأبوستيخن: " + apdoxa
        return service, pieces, fdoxa, prokiminon, readings, apostikn, apdoxa, serv


class sahar():

    def __init__(self, level):
        self.level = level

        def func_not_found():  # just in case we dont have the function
            print('No Function '+self.level+' Found!')
        func = getattr(self, self.level, func_not_found)
        self.service = func()

    def XX(self):
        service = "Qyamah"
        return service

    def WW(self):
        service = "Sayiedi"
        return service

    def VV(self):
        service = "Waldi"
        return service

    def YY(self):
        service = "MumtazG"
        return service

    def YW(self):
        service = "MumtazW"
        return service

    def YV(self):
        service = "MumtazN"
        return service

    def ZZ(self):
        service = "Normal"
        return service

    def YVY(self):
        service = "MumtazWE"
        return service

    def XZZ(self):
        service = "QN"
        return service

    def XWW(self):
        service = "QS"
        return service

    def XVV(self):
        service = "QW"
        return service

    def XYY(self):
        service = "QMG"
        return service

    def XYW(self):
        service = "QMW"
        return service

    def XYV(self):
        service = "QMN"
        return service

    def WV(self):
        service = "SW"
        return service

    def WYY(self):
        service = "SMG"
        return service

    def WYW(self):
        service = "SMW"
        return service

    def WYV(self):
        service = "SMN"
        return service

    def VYY(self):
        service = "WMG"
        return service

    def VYW(self):
        service = "WMW"
        return service

    def VYV(self):
        service = "WMN"
        return service

    def YYY(self):
        service = "2MG"
        return service

    def YYW(self):
        service = "GW"
        return service

    def YYV(self):
        service = "GN"
        return service

    def YWW(self):
        service = "2MW"
        return service

    def YWV(self):
        service = "WN"
        return service

    def YVV(self):
        service = "2MN"
        return service

    def ZV(self):
        service = "+W"
        return service

    def ZW(self):
        service = "+S"
        return service

    def ZX(self):
        service = "+Q"
        return service

    def ZY(self):
        service = "N+"
        return service

    def VY(self):
        service = "-W"
        return service

    def YYZ(self):
        service = "-MG"
        return service

    def WY(self):
        service = "-S"
        return service

    def XY(self):
        service = "-Q"
        return service

    def XWV(self):
        service = "QSW"
        return service

    def XWYY(self):
        service = "QSMG"
        return service

    def XWYW(self):
        service = "QSMW"
        return service

    def XWYV(self):
        service = "QSMN"
        return service

    def XVYY(self):
        service = "QWMG"
        return service

    def XVYW(self):
        service = "QWMW"
        return service

    def XVYV(self):
        service = "QWMN"
        return service

    def XYYY(self):
        service = "Q2MG"
        return service

    def XYYW(self):
        service = "QGW"
        return service

    def XYYV(self):
        service = "QGN"
        return service

    def XYWW(self):
        service = "Q2MW"
        return service

    def XYWV(self):
        service = "QWN"
        return service

    def XYVV(self):
        service = "Q2MN"
        return service

    def XZV(self):
        service = "Q+W"
        return service

    def XZW(self):
        service = "Q+S"
        return service

    def XZX(self):
        service = "Q+Q"
        return service

    def XZY(self):
        service = "QN+"
        return service

    def XVY(self):
        service = "Q-W"
        return service

    def XYYZ(self):
        service = "Q-MG"
        return service

    def XWY(self):
        service = "Q-S"
        return service

    def XXY(self):
        service = "Q-Q"
        return service

    def XYVY(self):
        service = "QMumtazWE"
        return service


class divineLiturgie():

    def __init__(self, arg):
        self.arg = arg


class firstHour():

    def __init__(self, arg):
        self.arg = arg


class thirdHour():

    def __init__(self, arg):
        self.arg = arg


class sixthHour():

    def __init__(self, arg):
        self.arg = arg


class ninethHour():

    def __init__(self, arg):
        self.arg = arg


class Midnight():

    def __init__(self, arg):
        self.arg = arg


# F = Feast("Vespers",dt.date(2020,9,9)).easter()
