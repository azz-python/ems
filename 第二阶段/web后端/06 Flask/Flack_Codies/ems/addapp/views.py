import os
import uuid
import json

from django.db import transaction
from django.http import JsonResponse
from django.core.paginator import Paginator


from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from django.urls import reverse


from loginapp.models import Test, User


def emplist(request):
    def mydefault(u):
        if isinstance(u, Test):
            return {'id': u.id, 'headpic': str(u.headpic), 'name': u.name, 'salary': str(u.salary), 'age': u.age}
    users = list(Test.objects.all())
    # print(users)
    # user=json.dumps(users,default=mydefault)
    # print(user)
    return JsonResponse({"users":users},json_dumps_params={'default':mydefault})
    # result = request.session.get('login')
    # n=request.GET.get('number','1')
    # print(n)
    # users=Test.objects.all()
    # print(users)
    # pagtor=Paginator(users,per_page=3)
    # try:
    #     if int(n) not in pagtor.page_range:
    #         n=1
    # except:
    #     n=1
    # page=pagtor.page(n)
    # if result:
    # return render(request, 'addapp/../static/emplist.html',
    #               {'page':page}
    #               )
    # return redirect('loginapp:login')



# def add(request):
#     return HttpResponse('ok')

def addlogic(request):
    try:
        with transaction.atomic():
            name = request.POST.get('name')
            salary = request.POST.get('salary')
            age = request.POST.get('age')
            headpic = request.FILES.get('headpic')
            ext = os.path.splitext(headpic.name)
            headpic.name = str(uuid.uuid4()) + ext[1]
            # print(name, salary, age, headpic)
            result = Test.objects.create(name=name, salary=salary, age=age, headpic=headpic)
            if result:
                # pagtor=Paginator(Test.objects.all(),per_page=3)
                # url=reverse('add:emplist')+"?number="+str(pagtor.num_pages)  #页面数
                # return redirect(url)
                return HttpResponse('ok')
    except:
        return HttpResponse('error')

def update(request):
    id=request.GET.get('id')
    # print(id)
    test=Test.objects.get(id=int(id))
    # print(test)
    if test:
        request.session['updateid']=id
        return HttpResponse('ok')
    return HttpResponse('error')

def update3(request):
    def mydefault2(u):
        if isinstance(u, Test):
            return {'id': u.id, 'headpic': str(u.headpic), 'name': u.name, 'salary': str(u.salary), 'age': u.age}
    pid=request.GET.get('pid')
    # print(pid)
    id=request.session.get(pid)
    # print(id)
    user=Test.objects.get(id=id)
    # print(user)
    return JsonResponse({"users":user},json_dumps_params={'default':mydefault2})

def updatelogic(request):
    try:
        with transaction.atomic():
            id = request.POST.get('mid2')
            # print(id)
            test=Test.objects.get(id=id)
            test.name=request.POST.get('name')
            test.salary=request.POST.get('salary')
            test.age=request.POST.get('age')
            headpic=request.FILES.get('headpic')
            if headpic:
                ext = os.path.splitext(headpic.name)
                headpic.name = str(uuid.uuid4()) + ext[1]
                test.headpic=headpic
            test.save()
            return HttpResponse('OK')
    except:
        return HttpResponse('error')

def delete(request):
    id=request.GET.get('id')
    # print(id)

    # number=request.GET.get('number')
    # print(number)
    test=Test.objects.get(id=id)
    # print(test)
    test.delete()
    # pagtor=Paginator(Test.objects.all(),per_page=3)
    # if int(number) >pagtor.num_pages:  #当number大于总页数时
    #     number=pagtor.num_pages  #等于总页数
    # url=reverse('add:emplist')+"?number="+ str(number)
    # return redirect(url)
    return HttpResponse('ok')
