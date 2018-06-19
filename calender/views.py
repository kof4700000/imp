from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Event

# Create your views here.
def calender_page(request):
    return render(request, "calender/calender.html", context={})

@csrf_exempt
def add_event(request):
    #print(request.POST['date'].split(" - "))
    #print(request.POST['title'])
    #print(request.POST['color'])
    start_date = request.POST['date'].split(" - ")[0]
    end_date = request.POST['date'].split(" - ")[1]
    title = request.POST['title']
    color = request.POST['color']
    start_y = start_date.split("/")[2]
    start_m = start_date.split("/")[0]
    start_d = start_date.split("/")[1]
    end_y = end_date.split("/")[2]
    end_m = end_date.split("/")[0]
    end_d = end_date.split("/")[1]
    print(start_date)
    print(start_y)
    print(start_m)
    print(start_d)
    Event.objects.create(title = title, backgroundColor = color, borderColor = color,
                         start_y = start_y,
                         start_m = start_m,
                         start_d = start_d,
                         end_y = end_y,
                         end_m = end_m,
                         end_d = end_d)
    return render(request, "calender/calender.html", context={})

def get_event(request):
    response = []
    for event in Event.objects.all():
        response.append({
            "title":event.title,
            "backgroundColor":event.backgroundColor,
            "borderColor":event.borderColor,
            "start_y":event.start_y,
            "start_m":event.start_m,
            "start_d":event.start_d,
            "end_y":event.end_y,
            "end_m":event.end_m,
            "end_d":event.end_d
            })
    #response = [{"test1":"test1","test2":"test2","test3":"test3"}]
    return JsonResponse(response, safe = False)
