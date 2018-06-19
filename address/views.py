# -*- coding: GB2312 -*-
from django.shortcuts import render
from django.http import HttpResponse
from account.models import IMPUser
#from address.models import Address
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def show_page(request):
    response = []
    #display_id = 0
    for user in IMPUser.objects.all():
        #display_id = display_id + 1
        response.append({'username':user.username,
                         'tel':user.tel,
                         'mobile':user.mobile,
                        # 'display_id':display_id,
                         'display_name':user.display_name})
    return render(request, "address/address.html", context={'address':response})


def get_address(request):
    if IMPUser.objects.all() is not None:
        response = []
        for user in IMPUser.objects.all():
            response.append({'user':user.username, 'display_name':user.display_name})
        #address = json.dumps(response) #注意，要返回成数组时不能加这行代码，
        #否则返回的是一个长string，之后学习下为什么
        #return JsonResponse({'address':response})
        return JsonResponse(response, safe=False)
        #safe参数默认为True，为True时，只能返回dict格式的数据
    return HttpResponse("hehehe")
