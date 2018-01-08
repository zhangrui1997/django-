from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from app01 import models
# Create your views here.

USER_DICT = {
    '1': {'name': 'root1', 'email': 'root@live.com'},
    '2': {'name': 'root2', 'email': 'root@live.com'},
    '3': {'name': 'root3', 'email': 'root@live.com'},
    '4': {'name': 'root4', 'email': 'root@live.com'},
    '5': {'name': 'root5', 'email': 'root@live.com'},
}



def index(request):
    
    return render(request, 'index.html', {'user_dict':USER_DICT})



def detail(request, nid):
    # nid = request.GET.get('nid')
    detail_info = USER_DICT[nid]
    return render(request, 'detail.html', {'detail_info': detail_info})

'''
def login(request):
    if request.method=="GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        if u == 'alex' and p == '123':
            return redirect('/index/')

    else:
        return redirect('/index/')'''

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


# def home(request):
#     return HttpResponse('home')

from django.views import View
class Home(View):

    def get(self, request):
        print(request.method)
        return render(request, 'home.html')

    def post(self, request):
        print(request.method)
        return render(request, 'home.html')



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

