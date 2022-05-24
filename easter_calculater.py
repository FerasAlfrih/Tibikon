import datetime as dt


def Easter(year):
    year = year
    silver = year % 19
    pfm = 21+(19*silver+15) % 30
    dow = (pfm+year+year//4) % 7
    easter = pfm+7-dow
    if easter > 31:
        e = easter - 31
        easter = str(year) + ',' + '4' + ',' + str(e)
    else:
        easter = str(year) + ',' + '3' + ',' + str(easter)
    EASTER = dt.datetime.strptime(easter, '%Y,%m,%d').date()
    if year < 2100:
        EASTER = EASTER + dt.timedelta(days=13)
    else:
        EASTER = EASTER + dt.timedelta(days=14)
    Ascension = EASTER + dt.timedelta(days=39)
    Pentecost = EASTER + dt.timedelta(days=49)
    return EASTER, Ascension, Pentecost


# years = []
# for i in range(1000, 3000):
#     e = easter(i)
#     y = str(e.day)+"/" + str(e.month)+"/" + str(e.year)
#     years.append(dt.datetime.strptime(y, '%d/%m/%Y'))
# print(sorted(years))
