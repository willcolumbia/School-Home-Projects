from django.shortcuts import render

def Tickets(request):
    return render(request, "tickets.html")
