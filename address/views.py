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
        #address = json.dumps(response) #ע�⣬Ҫ���س�����ʱ���ܼ����д��룬
        #���򷵻ص���һ����string��֮��ѧϰ��Ϊʲô
        #return JsonResponse({'address':response})
        return JsonResponse(response, safe=False)
        #safe����Ĭ��ΪTrue��ΪTrueʱ��ֻ�ܷ���dict��ʽ������
    return HttpResponse("hehehe")
