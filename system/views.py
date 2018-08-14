# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core import urlresolvers
from django.views.decorators.csrf import csrf_exempt
from .models import System, Host, User_System
from account.models import IMPUser
from document.models import Document
#from address.models import Address
from django.http import JsonResponse, HttpResponse

# Create your views here.
def system_page(request):
    """
    Show default page of System. All Systems are displayed.
    """
    response = []
    system_array = System.objects.all()
    for sys in system_array:
        a_role = ''
        b_role = ''
        a_role_user = ''
        b_role_user = ''
        if User_System.objects.filter(sys = sys, role = 'A').exists():
            a_role = User_System.objects.filter(sys = sys, role = 'A')[0].user.display_name
            a_role_user = User_System.objects.filter(sys = sys, role = 'A')[0].user.username
        if User_System.objects.filter(sys = sys, role = 'B').exists():    
            b_role = User_System.objects.filter(sys = sys, role = 'B')[0].user.display_name
            b_role_user = User_System.objects.filter(sys = sys, role = 'B')[0].user.username
        host_array = Host.objects.all().filter(system = sys)
        ip = []
        for host in host_array:
            ip.append(host.IP)
        response.append({'full_name':sys.full_name,
                         'short_name':sys.short_name,
                         'A_role':a_role,
                         'A_username':a_role_user,
                         'B_role':b_role,
                         'B_username':b_role_user,
                         'ip':ip})
    return render(request, "system/system.html",context={"system":response})

def system_detail(request, system):
    """
    Show detail page of specific System identified by system(which is short_name
    comes from front end), including detail and docs of System. Triggered by button.
    """
    context = {}
    hosts = []
    full_name = ''
    short_name = ''
    try:
        sys = System.objects.get(short_name = system)
        host_array = Host.objects.filter(system = sys)
        full_name = sys.full_name
        short_name = sys.short_name
        for host in host_array:
            hosts.append({"ip":host.IP})
    except:
        pass
    try:
        A_role = User_System.objects.get(sys = sys, role = 'A').user.display_name
    except:
        A_role = ""
    try:
        B_role = User_System.objects.get(sys = sys, role = 'B').user.display_name
    except:
        B_role = ""
        
    response = []
    if short_name != '':      
        doc = Document.objects.all().filter(tag = short_name)
        for each in doc:
            response.append({"doc_name":each.doc_name, "doc_id":each.id})
    context = {"full_name":full_name,
               "short_name":short_name,
               "A_role":A_role,
               "B_role":B_role,
               "ip":hosts,
               "doc":response}
    return render(request, "system/system_detail.html", context)
    

def add_system(request):
    """
    Show add page of new System. 
    """
    return render(request, "system/add_system.html", context={})

def edit_system(request, system):
    """
    Show edit page of System.
    """
    context = {}
    hosts = []
    full_name = ''
    short_name = ''
    try:
        sys = System.objects.get(short_name = system)
        host_array = Host.objects.filter(system = sys)
        full_name = sys.full_name
        short_name = sys.short_name
        for host in host_array:
            hosts.append({"ip":host.IP})
    except:
        pass
    try:
        A_role = User_System.objects.get(sys = sys, role = 'A').user.display_name
    except:
        A_role = ""
    try:
        B_role = User_System.objects.get(sys = sys, role = 'B').user.display_name
    except:
        B_role = ""  
    context = {"full_name":full_name,
               "short_name":short_name,
               "A_role":A_role,
               "B_role":B_role,
               "ip":hosts}
    return render(request, "system/edit_system.html", context)

@csrf_exempt
def crud_system(request):
    """
    function of add system and edit system.
    """
    full_name = request.POST['full_name']
    short_name = request.POST['short_name']
    role_A = request.POST['A']
    role_B = request.POST['B']
    #注意前端传来的数组使用getlist获取，且参数后面需要加[]，否则获取不到
    hosts = request.POST.getlist('hosts[]')
    action = request.POST['action']
    if action == 'EDIT':
        sys = System.objects.get(full_name = full_name)
        sys.short_name = short_name
        sys.save()
        try:
            A_role = User_System.objects.get(sys = sys, role = role_A)
            A_role.user = IMPUser.objects.get(display_name = role_A)
            A_role.save()
        except:
            pass
        try:
            B_role = User_System.objects.get(sys = sys, role = role_B)
            B_role.user = IMPUser.objects.get(display_name = role_B)
            B_role.save()
        except:
            pass
        org_hosts = Host.objects.filter(system = sys)
        org_hosts.delete()
        if hosts:
            for host in hosts:
                Host.objects.create(IP = host, system = sys)
        #return HttpResponse({"status":"success"})
        return JsonResponse({"success":1})

    if action == 'ADD':
        if full_name == '' or short_name == '':
            print("EMPTY name!")
            return HttpResponse('{"status":"failed"}')
        if System.objects.all().filter(full_name = full_name).exists() or \
           System.objects.all().filter(short_name = short_name).exists():
            print("Exist!")
            return HttpResponse('{"status":"failed"}')
        sys = System.objects.create(full_name = full_name, short_name = short_name)
        if role_A:
            user_A = IMPUser.objects.get(display_name=role_A)
            User_System.objects.create(role = 'A', user = user_A, sys = sys)
            if role_B:
                user_B = IMPUser.objects.get(display_name=role_B)
                User_System.objects.create(role = 'B', user = user_B, sys = sys)
        if hosts:
            for host in hosts:
                if host:
                    print(host)
                    Host.objects.create(IP = host, system = sys)
        return JsonResponse({"success":1})
    
    #return HttpResponse('{"status":"success"}')
    #return render(request, "system/system.html", context={})

def get_system(request, system):
    """
    brief detail of system in table modal
    """
    context = {}
    hosts = []
    full_name = ''
    short_name = ''
    try:
        sys = System.objects.get(short_name = system)
        host_array = Host.objects.filter(system = sys)
        full_name = sys.full_name
        short_name = sys.short_name
        for host in host_array:
            hosts.append({"ip":host.IP})
    except:
        pass
    context = {"full_name":full_name,
               "short_name":short_name,
               "ip":hosts}
    try:
        A_role = User_System.objects.get(sys = sys, role = 'A').user.display_name
        context['A_role'] = A_role
    except:
        pass
    try:
        B_role = User_System.objects.get(sys = sys, role = 'B').user.display_name
        context['B_role'] = B_role
    except:
        pass 

    return JsonResponse(context)

    '''
def get_system(request):
    page_num = int(request.GET['page_num'])
    page_size = int(request.GET['page_size'])
    system_array = System.objects.all()
    begin_pos = (page_num - 1) * page_size
    end_pos = page_num * page_size - 1
    if (end_pos > len(system_array)):
        end_pos = len(system_array) - 1
    response = []
    display_id = 0
    for i in range(begin_pos, end_pos + 1):
        display_id = i
        sys = system_array[i]
        a_role = ''
        b_role = ''
        if User_System.objects.filter(sys = sys, role = 'A').exists():
            a_role = User_System.objects.filter(sys = sys, role = 'A')[0].user.display_name
        if User_System.objects.filter(sys = sys, role = 'B').exists():    
            b_role = User_System.objects.filter(sys = sys, role = 'B')[0].user.display_name
        host_array = Host.objects.all().filter(system = sys)
        ip = []
        for host in host_array:
            ip.append(host.IP)
        response.append({'full_name':sys.full_name,
                         'short_name':sys.short_name,
                         'A_role':a_role,
                         'B_role':b_role,
                         'ip':ip})
    return JsonResponse(response, safe=False)
    
def get_system_count(request):
    response = {'max_count':len(System.objects.all())}
    return JsonResponse(response, safe=False)
    '''

def get_host(request):
    host_array = Host.objects.all()
    response = []
    a_role = ''
    b_role = ''
    for host in host_array:
        sys = host.system
        if User_System.objects.filter(sys = sys, role = 'A').exists():
            a_role = User_system.objects.filter(sys = sys, role = 'A')[0].user.display_name
        if User_System.objects.filter(sys = sys, role = 'B').exists():    
            b_role = User_System.objects.filter(sys = sys, role = 'B')[0].user.display_name
        response.append({'ip':host.IP,
                         'sys_name':sys.short_name,
                         'A_role':a_role,
                         'B_role':b_role
            })
    return JsonResponse(response, safe=False)

def host_page(request):
    host_array = Host.objects.all()
    response = []
    for host in host_array:
        a_role = ''
        b_role = ''
        sys = host.system
        if User_System.objects.filter(sys = sys, role = 'A').exists():
            a_role = User_System.objects.filter(sys = sys, role = 'A')[0].user.display_name
        if User_System.objects.filter(sys = sys, role = 'B').exists():    
            b_role = User_System.objects.filter(sys = sys, role = 'B')[0].user.display_name
        response.append({'ip':host.IP,
                         'sys_name':sys.short_name,
                         'A_role':a_role,
                         'B_role':b_role
            })

    return render(request, "system/host.html", context={"hosts":response})
