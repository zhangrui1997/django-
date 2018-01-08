from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from app01 import models
# Create your views here.



def index(request):

    return render(request, 'index.html')

def user_info(request):
    user_list = models.UserInfo.objects.all()
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        d = request.POST.get('deletename')
        if u and p:
            models.UserInfo.objects.create(username=u, password=p)
        if d:
            models.UserInfo.objects.filter(username=d).delete()

    return render(request, 'user_info.html', {'user_list':user_list})
def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/user_info/')

def user_edit(request, nid):
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {'obj':obj})
    if request.method == "POST":
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.UserInfo.objects.filter(id=nid).update( password=p, username=u)
        return redirect('/cmdb/user_info/')
def user_detail(request, nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    # models.UserInfo.objects.get(id=nid) # 查不到就出错
    return render(request, 'user_detail.html',{'obj':obj})

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == 'POST':
        # # radio
        # # v=request.POST.get('gender')
        # # print(v)
        #
        # #获取chenckbox
        # # v = request.POST.getlist('favor')
        # # print(v)
        #
        # # v = request.POST.get('fafafa')
        # # print(v)
        # # 上传功能
        # obj = request.FILES.get('fafafa')
        # print(obj)
        # import os
        # file_path = os.path.join('upload', obj.name)
        # f = open(file_path, mode='wb')
        # for i in obj.chunks():
        #     f.write(i)
        # f.close()
        # # from django.core.files.uploadedfile import InMemoryUploadedFile
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        result = models.UserInfo.objects.filter(username=u, password=p).first() #查找第一个
        # result = models.UserInfo.objects.filter(username=u, password=p).count() #获取个数
        if result:
            return redirect('/cmdb/index/')
        else:
            return render(request, 'login.html')
    else:
        return redirect('/index/')



from django.views import View



def orm(request):
    # 增加数据 三种方式
    # models.UserInfo.objects.create(username='root', password='123')

    # dic = {'username' : 'eric', 'password': '666'}
    # models.UserInfo.objects.create(**dic)

    # obj = models.UserInfo(username='alex', password='123')
    # obj.save()


    # 查
    # result = models.UserInfo.objects.all() #查所有
    # result = models.UserInfo.objects.filter(username='root') #相当于 where =
    # result = models.UserInfo.objects.filter(username='root',password='123') #相当于 where =
    # result,Queryset => Django =>列表
    # [obj, obj, obj]
    # for row in result:
    #     print(row.id, row.username, row.password)
    # print(result)

    # 删除
    # models.UserInfo.objects.all().delete() # 删除所有
    # models.UserInfo.objects.filter(id='1').delete()

    # 更新
    # models.UserInfo.objects.all().update(password='123456')
    # models.UserInfo.objects.filter(id=1).update(password='123456')
    return HttpResponse('orm')

