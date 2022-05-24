from django.db import models
from django.utils.translation import gettext as _
import datetime as dt


class Saints(models.Model):
    saint = models.CharField(_("saint"), max_length=255)
    day = models.IntegerField(_("day"))
    month = models.IntegerField(_("month"))
    feast = models.CharField(_("feast"), max_length=50)
    name = models.CharField(_("name"), max_length=255, default='none')

    def __str__(self):
        return self.saint


# class Year(models.Model):
#     year = models.IntegerField(_('year'))

#     def __str__(self):
#         return self.year


# class Month(models.Model):
#     year = models.ForeignKey(Year, verbose_name=_(
#         "year"), on_delete=models.CASCADE)
#     month = models.IntegerField(_('month'))

#     def __str__(self):
#         return self.month + '/' + self.year.year


# class Sunday(models.Model):
#     year = models.ForeignKey(Year, verbose_name=_(
#         "year"), on_delete=models.CASCADE)
#     month = models.ForeignKey(Month, verbose_name=_(
#         "month"), on_delete=models.CASCADE)
#     day = models.IntegerField(_('day'))
#     iotheana = models.CharField(_("iotheana"), max_length=50)
#     tone = models.CharField(_("tone"), max_length=50)


# class PaschalNetwork(models.Model):
#     year = models.ForeignKey(Year, verbose_name=_(
#         "year"), on_delete=models.CASCADE)
#     month = models.ForeignKey(Month, verbose_name=_(
#         "month"), on_delete=models.CASCADE)
#     day = models.ForeignKey(Day, verbose_name=_(
#         "day"), on_delete=models.CASCADE)
#     easter = models.DateField(_("easter"), auto_now=False, auto_now_add=False)
#     ascension = models.DateField(
#         _("ascension"), auto_now=False, auto_now_add=False)
#     pentecost = models.DateField(
#         _("pentecost"), auto_now=False, auto_now_add=False)

#     Zacchaeus = models.DateField(
#         _("easter"), auto_now=False, auto_now_add=False)
#     PnPH = models.DateField(auto_now=False, auto_now_add=False)
#     PS = models.DateField(auto_now=False, auto_now_add=False)
#     LD = models.DateField(auto_now=False, auto_now_add=False)
#     SF = models.DateField(auto_now=False, auto_now_add=False)
#     lent = models.DateField(auto_now=False, auto_now_add=False)
#     orthodoxy = models.DateField(auto_now=False, auto_now_add=False)
#     GP = models.DateField(auto_now=False, auto_now_add=False)
#     cross = models.DateField(auto_now=False, auto_now_add=False)
#     ladder = models.DateField(auto_now=False, auto_now_add=False)
#     egypt = models.DateField(auto_now=False, auto_now_add=False)
#     lazarus = models.DateField(auto_now=False, auto_now_add=False)
#     palms = models.DateField(auto_now=False, auto_now_add=False)
#     GM = models.DateField(auto_now=False, auto_now_add=False)
#     GT = models.DateField(auto_now=False, auto_now_add=False)
#     GW = models.DateField(auto_now=False, auto_now_add=False)
#     GTH = models.DateField(auto_now=False, auto_now_add=False)
#     GF = models.DateField(auto_now=False, auto_now_add=False)
#     GS = models.DateField(auto_now=False, auto_now_add=False)
#     toma = models.DateField(auto_now=False, auto_now_add=False)
#     perf = models.DateField(auto_now=False, auto_now_add=False)
#     mokh = models.DateField(auto_now=False, auto_now_add=False)
#     sam = models.DateField(auto_now=False, auto_now_add=False)
#     blond = models.DateField(auto_now=False, auto_now_add=False)
#     fef = models.DateField(auto_now=False, auto_now_add=False)
#     saints = models.DateField(auto_now=False, auto_now_add=False)
#     aps = models.DateField(auto_now=False, auto_now_add=False)
#     apsfast = models.DateField(auto_now=False, auto_now_add=False)

#     def paschalion(self):
#         easter = self.easter
#         self.Zacchaeus = easter - dt.timedelta(days=77)
#         self.PnPH = easter - dt.timedelta(days=70)
#         self.PS = easter - dt.timedelta(days=63)
#         self.LD = easter - dt.timedelta(days=56)
#         self.SF = easter - dt.timedelta(days=49)
#         self.lent = easter - dt.timedelta(days=48)
#         self.orthodoxy = easter - dt.timedelta(days=42)
#         self.GP = easter - dt.timedelta(days=35)
#         self.cross = easter - dt.timedelta(days=28)
#         self.ladder = easter - dt.timedelta(days=21)
#         self.egypt = easter - dt.timedelta(days=14)
#         self.lazarus = easter - dt.timedelta(days=8)
#         self.palms = easter - dt.timedelta(days=7)
#         self.GM = easter - dt.timedelta(days=6)
#         self.GT = easter - dt.timedelta(days=5)
#         self.GW = easter - dt.timedelta(days=4)
#         self.GTH = easter - dt.timedelta(days=3)
#         self.GF = easter - dt.timedelta(days=2)
#         self.GS = easter - dt.timedelta(days=1)
#         self.toma = easter + dt.timedelta(days=7)
#         self.perf = self.toma + dt.timedelta(days=7)
#         self.mokh = self.perf + dt.timedelta(days=7)
#         self.sam = self. mokh + dt.timedelta(days=7)
#         self.blond = self.sam + dt.timedelta(days=7)
#         self.fef = self.blond + dt.timedelta(days=7)
#         self.saints = self.Pentecost + dt.timedelta(days=7)
#         self.aps = self.saints + dt.timedelta(days=1)
#         if (dt.date(self.year, 6, 29) - self.aps).days > 0:
#             self.apsfast = self.aps
#         else:
#             self.apsfast = "لا يوجد"

#     def easter(self, year):
#         silver = year % 19
#         pfm = 21+(19*silver+15) % 30
#         dow = (pfm+year+year//4) % 7
#         easter = pfm+7-dow
#         if easter > 31:
#             e = easter - 31
#             easter = str(year) + ',' + '4' + ',' + str(e)
#         else:
#             easter = str(year) + ',' + '3' + ',' + str(easter)
#         Easter = dt.datetime.strptime(easter, '%Y,%m,%d').date()
#         if year < 2100:
#             Easter = Easter + dt.timedelta(days=13)
#         else:
#             Easter = Easter + dt.timedelta(days=14)
#         Ascension = Easter + dt.timedelta(days=39)
#         Pentecost = Easter + dt.timedelta(days=49)
#         self.easter = Easter
#         self.ascension = Ascension
#         self.pentecost = Pentecost

#     def save(self):
#         self.easter(self.year)
#         self.paschalion()
#         return super().save()


# class Calendar(models.Model):
#     year = models.ForeignKey(Year, verbose_name=_(
#         "year"), on_delete=models.CASCADE)
#     month = models.ForeignKey(Month, verbose_name=_(
#         "month"), on_delete=models.CASCADE)
#     day = models.ForeignKey(Day, verbose_name=_(
#         "day"), on_delete=models.CASCADE)

#     def get_easter(self):
#         pass

#     def get_saint():
#         pass
