from .models import Saints
from .utils import Calendar
from django.utils.safestring import mark_safe
from babel.dates import format_date
from datetime import datetime


def extras(request):
    context = {}
    d = datetime.today().date()
    cal = Calendar(d.year, d.month)
    cal.locale = 'ar_sy'
    saints = [saint.name for saint in Saints.objects.filter(month=d.month)]
    html_cal = cal.formatmonth(withyear=True)
    context['calendar'] = mark_safe(html_cal)
    context['saints'] = mark_safe(saints)
    context['today'] = format_date(d, format='full', locale='ar_sy')
    return context
