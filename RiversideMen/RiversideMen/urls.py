from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Home.views import Home
from Calendar import views as calViews
from News import views as newsViews
from Tickets import views as ticketViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",Home,name="Home"),
    path('calendar/', calViews.CalendarView.as_view(), name='calendar'),
    path('news/', newsViews.News,name="news"),
    path('tickets/',ticketViews.Tickets,name="tickets"),
    
]

