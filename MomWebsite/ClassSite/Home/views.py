from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm

def Home(request):
    if request.method == 'POST':
        studentform = StudentForm(request.POST)
        
        if studentform.is_valid():
            studentform.save()
            return HttpResponseRedirect(reverse('thanks'))
        
    else:
        studentform = StudentForm()
    return render(request, 'home.html',{'studentform' : studentform})
def Thanks(request):
    return render(request, 'thankyou.html')
