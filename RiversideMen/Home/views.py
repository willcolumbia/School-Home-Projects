from django.shortcuts import render
from Calendar.models import Event
from django.shortcuts import render,get_object_or_404
def Home(request):
    instance = Event.objects.all().first()
    return render(request, 'home.html', {'all': instance})