from django.shortcuts import render
from Calendar.models import Event
from .models import SlideShow
from django.shortcuts import render,get_object_or_404
def Home(request):
    date = Event.end_time
    instance = Event.objects.all().first()
    return render(request, 'home.html', {'all': instance})
