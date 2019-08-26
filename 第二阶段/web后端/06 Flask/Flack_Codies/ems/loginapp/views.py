import os,uuid,string,random

from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, HttpResponse, redirect
from loginapp.captcha.image import ImageCaptcha
from loginapp.models import User, Test
# Create your views here.

# def regist(request):
#     return render(request, 'loginapp/../static/regist.html')

def registlogic(request):
    try:
        with transaction.atomic():
            name = request.POST.get('name')
            if not name:
                raise
            pwd = request.POST.get('pwd2')
            sex = request.POST.get('sex')
            codes = request.POST.get('captcha')
            # print(name, pwd, sex, codes)
            codes2 = request.session.get('codes')
            print(codes2)
            if codes.lower() == codes2.lower():
                result = User.objects.create(name=name, pwd=pwd, sex=sex)
                if result:
                    return HttpResponse('ok')
    except:
        return HttpResponse('error')

def login(request):
    name=request.COOKIES.get('name')
    if name:
        name=name.encode('latin-1').decode('utf-8')
    pwd=request.COOKIES.get('pwd')
    result = User.objects.filter(name=name, pwd=pwd)
    if result:
        request.session['login'] = 'ok'
        # return redirect('add:emplist')
    return HttpResponse('ok')

def loginlogic(request):
    name=request.POST.get('name')
    pwd=request.POST.get('pwd')
    r=request.POST.get('rem')
    result=User.objects.filter(name=name,pwd=pwd)
    if result:
        request.session['login']='ok'
        response = HttpResponse("ok")
        if r:
            response.set_cookie('name', name.encode("utf-8").decode("latin-1"), max_age=7 * 24 * 3600)
            response.set_cookie('pwd', pwd, max_age=7 * 24 * 3600)
        return response
    return HttpResponse('error')


def captcha(request):
    image=ImageCaptcha()
    codes=random.sample(string.ascii_letters+string.digits,4)
    codes=''.join(codes)
    print(codes)
    request.session['codes'] = codes
    data=image.generate(codes)
    return HttpResponse(data,'image/png')

def checkname(request):
    name=request.POST.get('uname')
    # print(name)
    result=User.objects.filter(name=name)
    if result:
        return HttpResponse('error')
    return HttpResponse('ok')

def checkpwd(request):
    pwd2=request.POST.get('upwd1')
    pwd=request.POST.get('upwd')
    if pwd==pwd2:
        return HttpResponse('ok')
    return HttpResponse('error')


def changecode(request):
    changecode=request.POST.get('ucaptcha')
    # print(changecode)
    result=request.session.get('codes')
    # print(result)
    if result.lower() == changecode.lower():
        # print('aaa')
        return HttpResponse('ok')
    return HttpResponse('error')



