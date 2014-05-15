from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import LoginUser
from django.http.response import HttpResponse
from DjangoCaptcha import Captcha

@csrf_exempt
def signup_form(request):
    return render(request, 'signup.html')


@csrf_exempt
def signup_submit(request):
    hobby = ''
    gender = -1
    if request.method == 'POST':
        post = dict(request.POST.iterlists())
        username = post.get('username','')
        password = post.get('password','')
        gender = post.get('gender','')
        if gender:
            gender = gender[0]
        introduce = post.get('introduce','')
        if introduce:
            introduce = introduce[0]
        province = post.get('province','')
        city = post.get('city','')
        native_place = province[0] + city[0]
        if post.get('basketball',''):
            hobby += '1 '
        if post.get('soccer',''):
            hobby += '2 '
        if post.get('soccer',''):
            hobby += '3 '
        if post.get('ec',''):
            hobby += '4'
        if not post.get('photo',''):
            photo_name = unicode(username[0]) + request.FILES['photo'].name[-4:]
            photo_file = handle_upload_file(request.FILES['photo'], photo_name)
            photo_path = './photos/' + photo_name
            photo_file.close()
        else:
            photo_path = ''
        user = LoginUser.objects.create_user(username[0], gender, hobby, native_place, introduce, photo_path)
        user.set_password(password[0])
        user.save()
        
    return render(request, 'signup_success.html')

@csrf_exempt
def check_username(request):
    if request.method == 'POST':
        post = dict(request.POST.iterlists())
        username = post.get('username', '')
        if username and username[0] != 'root':
            user = LoginUser.objects.filter(username=username[0])
        else:
            exist = 0
        if user:
            exist = 1
        else:
            exist = 0
    return HttpResponse(exist)
 


def code(request):
    ca = Captcha(request)
    ca.words = ['hello', 'world', 'apple', 'orange', 'banana', 'xiaobei', 'beibei']
    ca.type =  'number'
    return ca.display()


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


def handle_upload_file(f, photo_name):
    with open('./photos/'+photo_name,'wb+') as apk:
        for chunk in f.chunks():
            apk.write(chunk)
        return f
