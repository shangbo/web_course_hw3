# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from DjangoCaptcha import Captcha
from django.views.decorators.csrf import csrf_exempt
from signup.models import LoginUser
from django.contrib.auth import login as auth_login, logout
USERNAME = ''
def login(request):
    return render(request, 'login.html')

def code(request):
    ca = Captcha(request)
    ca.words = ['hello', 'world', 'apple', 'orange', 'banana', 'xiaobei', 'beibei']
    ca.type =  'number'
    return ca.display()

@csrf_exempt
def decode(request):
    if request.method == 'GET':
        _code = request.GET.get('code') or ''
        if not _code:
            return HttpResponse('0')

        ca = Captcha(request)

        if ca.check(_code):
            return HttpResponse('1')
        else:
            return HttpResponse('0')    

@csrf_exempt
def login_submit(request):
    reason = []
    if request.method == 'POST':
        post = dict(request.POST.iterlists())
        username = post.get('username', '')
        global USERNAME
        USERNAME = username[0]
        password = post.get('password', '')
        user = LoginUser.objects.filter(username=username[0])
        hobby = []
        h = user[0].hobby
        h = h.split(' ')
        for i in h:
            if i == '1':
                hobby.append('篮球')
            if i == '2':
                hobby.append('足球')
            if i == '3':
                hobby.append('音乐')
            if i == '4':
                hobby.append('电子竞技')
        if user:
            if user[0].check_password(password[0]):
                # auth_login(request, user[0])
                return render(request, 'login_success.html',{'user':user[0],'hobby':hobby})
                # return HttpResponse('shang')
            else:
                reason.append("密码错误")
        else:
            reason.append("用户名错误")
        return render(request, 'login_failed.html',{'reason':reason})


def modified(request):
    return render(request,'modified_info.html',{'username':USERNAME})

@csrf_exempt
def modified_submit(request):
    post = dict(request.POST.iterlists())
    hobby = ''
    print post
    
    username = post.get('username','')
    if username:
        username = username[0]
    else:
        username = ''
    user = LoginUser.objects.filter(username=username)    
    user0 = user[0]

    password = post.get('password','')
    if password[0]:
        user0.set_password(password[0])

    gender = post.get('gender','')
    if gender:
        gender = gender[0]
    else:
        gender = ''
    if gender:
        user0.gender = gender

    province = post.get("province")
    if province and province[0]!= u'无':
        province = province[0]
    else:
        province = ''
    city = post.get('city')
    if city and city[0]!= u'无':
        city = city[0]
    else:
        city = ''
    if province and city:
        native_place = province+' '+city
        user0.native_place = native_place

    if post.get('basketball',''):
        hobby += '1 '
    if post.get('soccer',''):
        hobby += '2 '
    if post.get('music',''):
        hobby += '3 '
    if post.get('ec',''):
        hobby += '4'
    if hobby:
        user0.hobby = hobby

    introduce = post.get('introduce','')
    if introduce[0]:
        introduce = introduce[0]
    else:
        introduce = ''
    if introduce:
        user0.introduce = introduce
    
    photo_path = post.get('photo','')
    if not photo_path:
        photo_name = unicode(username) + request.FILES['photo'].name[-4:]
        photo_file = handle_upload_file(request.FILES['photo'], photo_name)
        photo_path = './photos/' + photo_name
        photo_file.close()
    else:
        photo_path = ''
    if photo_path:
        user0.photo_path = photo_path
    user0.save()
    return HttpResponse('dsad')



def handle_upload_file(f, photo_name):
    with open('./photos/'+photo_name,'wb+') as apk:
        for chunk in f.chunks():
            apk.write(chunk)
        return f