from .models import Saints
from datetime import datetime, timedelta
from calendar import LocaleHTMLCalendar
import calendar


class Calendar(LocaleHTMLCalendar):
    def __init__(self, year=None, month=None, firstweekday=calendar.SATURDAY, locale=None):
        self.year = year
        self.month = month
        self.firstweekday = firstweekday
        self.locale = locale
        self.cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        self.years = [year for year in range(1900, 3000)]
        self.months = [month for month in range(1, 13)]
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, weekday, events):
        is_today = False
        events_per_day = events.filter(day=day)
        d = ''
        for event in events_per_day:
            if event.feast.strip() != "Feast":
                img = "<img src='/static/img/" + \
                    event.feast.strip() + ".png' width='15' height='15'>"
            else:
                img = ''
            d += f'{event.name}'
        if day == datetime.today().day:
            is_today = True
        s = "getElementById('my_form')"
        if day != 0:
            if is_today:
                return f'<td class="today"><input name="selectedDay" id="{day}" value="{self.year}/{self.month}/{day}" disabled="true" hidden><a name={day} onclick="tdSubmit({day});"><div class="top">{day}</div><div class="bottom">{img} {d} </div></a></td>'
            else:
                return f'<td class="%s"><input name="selectedDay" id="{day}" value="{self.year}/{self.month}/{day}" disabled="true" hidden><a name={day} onclick="tdSubmit({day});"><div class="top">{day}</div><div class="bottom">{img} {d} </div></a></td>' % (self.cssclasses[weekday])
        return '<td class="noday"></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, weekday, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        events = Saints.objects.filter(month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        cal += f'</table>'
        cal += f'<label>السنة</label>'
        cal += f'<select name="year" onChange="form.submit();">'
        for year in self.years:
            if year == self.year:
                cal += f'<option  selected>{year}</option>'
            else:
                cal += f'<option >{year}</option>'
        cal += f'</select>'
        cal += f'<label>الشهر</label>'
        cal += f'<select name="month" onChange="form.submit();">'
        n = 1
        for month in self.months:
            if month == self.month:
                cal += f'<option value={n} selected>{month}</option>'
                n += 1
            else:
                cal += f'<option value={n} >{month}</option>'
                n += 1
        cal += f'</select>'
        return cal
