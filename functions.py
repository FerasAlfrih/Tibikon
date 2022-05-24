from .feasts import *
import datetime as dt
from bs4 import BeautifulSoup
import re
from .models import *


def str_to_class(classname):
    FEASTS = {'Feast': Feast(), 'Circle': Circle(),
              'Star': Star(), 'Flake': Flake(), 'celticCross': celticCross(), 'germanCross': germanCross(), 'outlineCross': outlineCross()}
    feast = FEASTS[classname]
    return feast


def str_to_method(module, service):
    SERVICES = {'Vispers': module.vispers,
                'Morning': module.morning, 'Liturgy': module.liturgy}
    service = SERVICES[service]
    return service


def saints_xml():

    soup = BeautifulSoup(
        open('static/files/calendar.xml', encoding='utf8'), "lxml")
    root = soup.find('year')
    months = root.find_all('month')

    Saints.objects.all().delete()
    for mon in months:
        month = mon['id']
        days = mon.find_all('a')
        for d in days:
            day = d['id']
            saint = d.find('feast').text
            saint = re.sub(r'\s+', ' ', saint)
            saint = saint.replace('"', '')
            feast = d.find('l').text
            feast = re.sub(r'\s+', ' ', feast)
            feast = feast.replace('"', '')
            name = d.find('name').text
            name = re.sub(r'\s+', ' ', name)
            name = name.replace('"', '')
            if Saints.objects.filter(saint=saint, day=day, month=month, feast=feast):
                Saints.objects.filter(
                    saint=saint, day=day, month=month, feast=feast).update(name=name)
            else:
                celebration = Saints(saint=saint, day=day,
                                     month=month, feast=feast, name=name)
                celebration.save()


def toJSON(object):
    return object.__dict__
