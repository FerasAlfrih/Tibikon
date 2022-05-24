from typing import Mapping
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from rest_framework import request, response
from .models import *
from rest_framework.views import *
from .serializers import *
from rest_framework.response import Response
from .feasts import *
from .functions import *
from .easter_calculater import Easter
import datetime as dt
from datetime import datetime
from .Celebration import Celebration
from django.views import generic
from .utils import Calendar
from django.utils.safestring import mark_safe
from babel.dates import format_date


# class home(APIView):
#     def get(self, request, year, *args, **kwargs):
#         EASTER, Ascension, Pentecost = Easter(year)
#         easter = {}
#         easter['day'] = EASTER.day
#         easter['month'] = EASTER.month
#         easter['year'] = EASTER.year
#         ascension = {}
#         ascension['day'] = Ascension.day
#         ascension['month'] = Ascension.month
#         ascension['year'] = Ascension.year
#         pentecost = {}
#         pentecost['day'] = Pentecost.day
#         pentecost['month'] = Pentecost.month
#         pentecost['year'] = Pentecost.year
#         feast = {
#             'easter': easter,
#             'ascension': ascension,
#             'pentecost': pentecost
#         }
#         return Response(feast)


# def home(request):
# today = dt.date.today() + dt.timedelta(days=129)
# cel = Celebration(today)
# context = {
#     'celebration': cel.toJSON(),
#     'calendar': calendar.calendar(today.year, 2, 1, 6),
#     'year': today.year,
#     'month': today.month,
#     'day': today.day,
#     'date': today
# }

class home(generic.ListView):
    model = Saints
    template_name = 'home.html'
    years = [str(year) for year in range(1900, 3000)]

    def get_context_data(self, **kwargs):
        self.today = self.get_day()
        context = super().get_context_data(**kwargs)
        d = self.today
        cal = Calendar(d.year, d.month)
        cal.locale = 'ar_sy'
        saints = [saint.name for saint in Saints.objects.filter(month=d.month)]
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['saints'] = mark_safe(saints)
        context['today'] = format_date(d, format='full', locale='ar_sy')
        context['celebration'] = mark_safe(self.get_celebration())
        return context

    def post(self, *args, **kwargs):

        self.today = self.get_day()
        response = HttpResponseRedirect(self.request.path_info)
        response.set_cookie('today', self.today)
        return response

    def get_day(self):
        if self.request.method == 'POST':
            print(self.request.POST)
            if self.request.POST.get('selectedDay') != None:
                d = self.request.POST.get('selectedDay')
                day = d.split('/')[2]
                month = d.split('/')[1]
                year = d.split('/')[0]

            elif self.request.POST.get('year') in self.years:
                year = self.request.POST.get('year')
                month = self.request.POST.get('month')
                try:
                    d = self.request.COOKIES.get('today')
                    day = d.split('/')[2]
                except:
                    day = datetime.today().date()

            d = str(day) + '-' + month+'-'+year
            today = datetime.strptime(d, '%d-%m-%Y').date()
        else:
            d = self.request.COOKIES.get('today')
            try:
                today = datetime.strptime(d, '%Y-%m-%d').date()
            except:
                today = datetime.today().date()

        return today

    def get_celebration(self):
        self.today = self.get_day()
        celebration = Celebration(self.today)
        return celebration.get_celebration()


class SaintView(APIView):
    def get(self, request):
        saints = Saints.objects.all()
        serializer = SaintSerializer(saints, many=True)
        return Response(serializer.data)


class getSaint(APIView):
    def get_object(self, day, month, *args, **kwargs):
        try:
            return Saints.objects.filter().get(day=day, month=month)
        except Saints.DoesNotExist:
            raise Http404

    def get(self, request, day, month, format=None):
        saint = self.get_object(day, month)
        serializer = SaintSerializer(saint)
        return Response(serializer.data)


class getService(APIView):
    def get(self, request, saint, day, month, year, weekday):
        feast = saint.replace(' ', '')
        feast = str_to_class(feast)
        scripture = feast.toJSON()
        return Response(scripture)
