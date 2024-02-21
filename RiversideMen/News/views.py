from django.shortcuts import render

def News(request):
    return render(request, "news.html")

