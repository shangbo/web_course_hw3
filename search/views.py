from django.shortcuts import render
from django.http.response import HttpResponse
from signup.models import LoginUser
from django.utils import simplejson

def search(request):
    return render(request, 'search.html')


def search_submit(request):
    if request.method == 'GET':
        get = dict(request.GET.iterlists())
        username = get.get('username','')[0]
        user = LoginUser.objects.filter(username=username)[0]
        hobby = user.hobby
        gender = user.gender
        introduce = user.introduce
        native_place = user.native_place
        photo_path = user.photo_path
        data = {"hobby":hobby,'gender':gender,'introduce':introduce,'native_place':native_place,'photo_path':photo_path}
        return HttpResponse(simplejson.dumps(data, ensure_ascii=False))

