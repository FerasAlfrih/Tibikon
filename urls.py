from django.urls import path
from .views import *


urlpatterns = [
    path('home/', home.as_view(), name='home'),
    # path('home', home, name='home'),
    path('', SaintView.as_view()),
    path('saint/<int:month>/<int:day>', getSaint.as_view()),
    path('saint/<str:saint>/<int:day>/<int:month>/<int:year>/<str:weekday>',
         getService.as_view())
]
