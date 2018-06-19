from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def front(request):
    #print(request)
    return render(request, "front/front.html", context = {})
