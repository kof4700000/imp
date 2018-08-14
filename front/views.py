from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from django.core import urlresolvers

# Create your views here.
#@login_required(login_url = urlresolvers.reverse("sign_up"))
#@login_required(redirect_field_name = 'sign_in')
@login_required
def front(request):
    #print(request)
    return render(request, "front/front.html", context = {})
