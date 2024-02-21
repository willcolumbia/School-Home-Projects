from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Home.views import Home
from Athletes import views as athleteViews

from Calendar import views as calViews
from News import views as newsViews
from Tickets import views as ticketViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",Home,name="Home"),
    path('calendar/', calViews.CalendarView.as_view(), name='calendar'),
    path('event/view/(?P<event_id>\d+)/', calViews.event, name='event_edit'),
    path('news/', newsViews.News,name="news"),
    path('tickets/',ticketViews.Tickets,name="tickets"),
    path('signin/', athleteViews.SignIn, name="signin"),
    path("signin/",include('django.contrib.auth.urls')),
    #path('Athletes/', athleteViews.Athletes,name="athletes"),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

