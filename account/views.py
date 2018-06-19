# -*- coding: GB2312 -*-
from django.shortcuts import render, redirect
from django.contrib import auth
from system.models import User_System, Host, System
from .models import *
from django.core import urlresolvers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def sign_in_page(request):
    return render(request, "account/sign_in.html", context={})

def sign_up_page(request):
    return render(request, "account/sign_up.html", context={})

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username)
    print(password)
    user = auth.authenticate(username=username, password=password)
    print(user)
    if user is not None:
        auth.login(request, user)
        return redirect(urlresolvers.reverse("front_page")) 
    return redirect(urlresolvers.reverse("sign_in"))

@csrf_exempt
def crud_user(request):
    if request.POST['action'] == 'EDIT':
        username = request.POST['username']
        tel = request.POST['tel']
        mobile = request.POST['mobile']
        office = request.POST['office']
        num = request.POST['num']
        user = IMPUser.objects.get(username = username)
        user.tel = tel
        user.mobile = mobile
        user.office = office
        user.num = num
        user.save()
        return redirect(urlresolvers.reverse("address_page"))
    #print(request.POST['tel'])
    #username = request.POST['username']
    #password = request.POST['password']
    #password1 = request.POST['password1']
    #tel = request.POST['tel']
    #try:
    #    #if password.equals(password1)
    #    User.objects.all().get(username = username)       
    #    return render(request, "account/sign_up.html", context={"errmsg":"Duplicated User!"})
    #except:
    #    print("NO USER!")
    #    IMPUser.objects.create_user(username = username, password = password, tel=tel)
    return redirect(urlresolvers.reverse("sign_in"))

def edit_user(request, username):
    context = {}
    detail = IMPUser.objects.all().filter(username = username)
    if detail:
        context = {'username':username,
                   'display_name':detail[0].display_name,
                   'tel':detail[0].tel,
                   'mobile':detail[0].mobile,
                   'office':detail[0].office,
                   'num':detail[0].num}
    return render(request, "account/edit_user.html", context)

def get_detail(request, username):
    detail = IMPUser.objects.all().filter(username = username)
    if detail:
        context = {'username':username,
                   'display_name':detail[0].display_name,
                   'tel':detail[0].tel,
                   'mobile':detail[0].mobile,
                   'office':detail[0].office,
                   'num':detail[0].num}
        user = IMPUser.objects.get(username = username)
        sys_array = User_System.objects.filter(user = user)
        host_context = []
        for sys in sys_array:
            host_array = Host.objects.filter(system = sys.sys)
            for host in host_array:
                host_context.append({'system':sys.sys.full_name, 'host':host.IP, 'role':sys.role})
        context['host'] = host_context
        print(context)
        return render(request, "account/user_detail.html", context)
    return HttpResponse("hehehe")

#--------------------------------------------------
#--------------------------------------------------
def init_adderss(request):
    try:
        '''
        IMPUser.objects.create_user(username = 'kuangliyan', password = '123456',display_name = u'邝丽燕' ,     tel='82973380' ,mobile='13701365769')
        IMPUser.objects.create_user(username = 'hexin', password = '123456',display_name = u'何鑫' ,     tel='82973381' ,mobile='13522207275')
        IMPUser.objects.create_user(username = 'zouxin', password = '123456',display_name = u'邹欣' ,     tel='82973382' ,mobile='13051535444')
        IMPUser.objects.create_user(username = 'luyunyi', password = '123456',display_name = u'陆云屹' ,     tel='82973383' ,mobile='13681421319')
        IMPUser.objects.create_user(username = 'zhujin', password = '123456',display_name = u'朱进' ,     tel='82973384' ,mobile='13161283736')
        IMPUser.objects.create_user(username = 'yuankongwei', password = '123456',display_name = u'袁宏伟' ,     tel='82973385' ,mobile='13126604123')
        IMPUser.objects.create_user(username = 'wuweimin', password = '123456',display_name = u'吴为民' ,     tel='82973386' ,mobile='13718165715')
        IMPUser.objects.create_user(username = 'fengli', password = '123456',display_name = u'冯莉' ,     tel='82973389' ,mobile='13910992857')
        IMPUser.objects.create_user(username = 'wangxuedong', password = '123456',display_name = u'王学东' ,     tel='82973390' ,mobile='18911006195')
        IMPUser.objects.create_user(username = 'xulizhe', password = '123456',display_name = u'许历哲' ,     tel='82973391' ,mobile='18600560239')
        IMPUser.objects.create_user(username = 'chengzhiqiang', password = '123456',display_name = u'程志强' ,     tel='82973392' ,mobile='18601180769')
        IMPUser.objects.create_user(username = 'jiangpihui', password = '123456',display_name = u'姜丕辉' ,     tel='82973394' ,mobile='13522668756')
        IMPUser.objects.create_user(username = 'songboyang', password = '123456',display_name = u'宋博洋' ,     tel='82973395' ,mobile='18519665605')
        IMPUser.objects.create_user(username = 'yangxia', password = '123456',display_name = u'杨霞' ,     tel='82973396' ,mobile='13691166263')
        IMPUser.objects.create_user(username = 'liuqiang', password = '123456',display_name = u'刘强' ,     tel='82973397' ,mobile='13910852448')
        IMPUser.objects.create_user(username = 'dumin', password = '123456',display_name = u'杜敏' ,     tel='82973399' ,mobile='13651101282')
        IMPUser.objects.create_user(username = 'fantao', password = '123456',display_name = u'樊涛' ,     tel='82973176' ,mobile='13366756699')
        IMPUser.objects.create_user(username = 'guyuanjun', password = '123456',display_name = u'顾元军' ,     tel='82973181' ,mobile='13811910682')
        IMPUser.objects.create_user(username = 'diaolei', password = '123456',display_name = u'刁磊' ,     tel='82973717' ,mobile='13521666611')
        IMPUser.objects.create_user(username = 'juying', password = '123456',display_name = u'巨颖' ,     tel='82973776' ,mobile='13699271750')
        IMPUser.objects.create_user(username = 'huangfei', password = '123456',display_name = u'黄飞' ,     tel='82973777' ,mobile='18201412639')
        IMPUser.objects.create_user(username = 'lijinxue', password = '123456',display_name = u'李进学' ,     tel='82973775' ,mobile='13426150531')
        IMPUser.objects.create_user(username = 'zhudongji', password = '123456',display_name = u'朱冬吉' ,     tel='82975041' ,mobile='15210502624')
        IMPUser.objects.create_user(username = 'liheng', password = '123456',display_name = u'李珩' ,     tel='82975120' ,mobile='18601105056')
        IMPUser.objects.create_user(username = 'liupu', password = '123456',display_name = u'刘璞' ,     tel='82975424' ,mobile='13070166508')
        IMPUser.objects.create_user(username = 'wangjieru', password = '123456',display_name = u'王洁茹' ,     tel='82975423' ,mobile='13910570212')
        IMPUser.objects.create_user(username = 'yandawei', password = '123456',display_name = u'阎大伟' ,     tel='82976415' ,mobile='15001240247')
        IMPUser.objects.create_user(username = 'liangmiao', password = '123456',display_name = u'梁淼' ,     tel='82977037' ,mobile='18513178610')
        IMPUser.objects.create_user(username = 'mengchijie', password = '123456',display_name = u'孟池洁' ,     tel='82977046' ,mobile='13552104910')
        IMPUser.objects.create_user(username = 'wuchufan', password = '123456',display_name = u'吴楚凡',     tel='82977487' ,mobile='18302245037')
        IMPUser.objects.create_user(username = 'luogan', password = '123456',display_name = u'罗干',  tel='82975460',     mobile='13269373256')
    	IMPUser.objects.create_user(username = 'wangruixue', password = '123456',display_name = u'王瑞雪',     tel='82974490',     mobile='15801202262')
	IMPUser.objects.create_user(username = 'zourui', password = '123456',display_name = u'邹锐', tel='82974324',     mobile='13681337610')
	IMPUser.objects.create_user(username = 'yinzhiwei', password = '123456',display_name = u'尹志伟',     tel='82974536',     mobile='15210012010')
	IMPUser.objects.create_user(username = 'shijinpeng', password = '123456',display_name = u'师锦鹏',     tel='',     mobile='18210257509')
	IMPUser.objects.create_user(username = 'liuyan', password = '123456',display_name = u'刘艳',     tel='82974473',     mobile='18801388700')
	IMPUser.objects.create_user(username = 'liuzhi', password = '123456',display_name = u'刘志',     tel='82974359',     mobile='18701392961')
	IMPUser.objects.create_user(username = 'cuienming', password = '123456',display_name = u'崔恩铭',     tel='',     mobile='18910007540')
	'''
	IMPUser.objects.create_user(username = 'guohaibo', password = '123456',display_name = u'郭海波',     tel='82973408',     mobile='15801429196')
    except:
        print('ERROR')
        return HttpResponse("ERR0R")
    #if err_flg:
    #    return HttpResponse("DUPICATED USER")
    return HttpResponse("SUCCEED")
    '''
    new_address = [
    {'display_name':u'罗干','tel':'82975460','mobile':'13269373256'}, 
    {'display_name':u'王瑞雪','tel':'82974490','mobile':'15801202262'},
    {'display_name':u'邹锐','tel':'82974324','mobile':'13681337610'},  
    {'display_name':u'尹志伟','tel':'82974536','mobile':'15210012010'},
    {'display_name':u'师锦鹏','tel':'','mobile':'18210257509'},        
    {'display_name':u'刘艳','tel':'82974473','mobile':'18801388700'},  
    {'display_name':u'刘志','tel':'82974359','mobile':'18701392961'},  
    {'display_name':u'崔恩铭','tel':'','mobile':'18910007540'},        
    {'display_name':u'于晏浩','tel':'82976877','mobile':'18600262209'}
    ]
    err_flg = False
    for addr in new_address:
        if Address.objects.all().filter(display_name = addr['display_name']).exists():
            err_flg = True
            continue
        else:
            Address.objects.create(display_name = addr['display_name'] ,tel=addr['tel'] ,mobile=addr['mobile'])
            
    #--------------------------------------------------------------------------------------
    '''
