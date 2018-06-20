# -*-coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django import forms
from cmdb.cloud_atlas import test_run
from cmdb.cloud_atlas import channel_check
from cmdb.cloud_atlas import datamanager
from django.shortcuts import redirect
from django.core import  serializers
from django.contrib import auth
from cmdb import  models
from django.conf import settings
from cmdb.cloud_atlas import test_run
from cmdb.adtest import AdTest
import os
import shutil

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.models import User
import  time
import  sys
import json
reload(sys)
sys.setdefaultencoding("utf8")





# Create your views here.

# conn = http.client.HTTPConnection("www.baidu.com")
# conn.request("GET","/")
# r1=conn.getresponse()
# print(r1.status,r1.reason

class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)

@login_required
def index(request):


    Testlist=[{},]
    result=[]
    if request.method=="POST":
        app_key = request.POST.get("app_key",None)
        proctime = request.POST.get("proctime",None)
        datanum = request.POST.get("datanum",None)
        env = request.POST.get("env", None)
        mode = request.POST.get("checkbox1",None)
        sqlorder = request.POST.get("checkbox2",None)
        print mode
        nowtime =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))



        models.HistoryInfo8.objects.create(app_key=app_key,proctime= proctime,datanum = datanum,env =env,nowtime = nowtime)

        case = test_run.SimulateCloudTest()
        result = case.test_autorun(app_key, proctime,datanum,env,mode,sqlorder)
    TestList = models.HistoryInfo8.objects.all()

    print TestList
    return  render(request, "index.html", {"App_key":TestList,"result":result})
@login_required
def datacheck(request):

    dt =[]


    info ="\n"
    if request.method == "GET":
        app_info = datamanager.DataManager().test_get_applist()
        dt=[]
        # print app_info
        for (m,n,z) in app_info:
            temp = {}
            temp["key"] = m
            temp["value"] = n
            # temp[m] = n
            dt.append(temp)
            # dt.setdefault(m,[]).append(n.decode("utf-8"))
    elif request.method == "POST":
        type = request.POST.get("task_type",None)

        begin_time = request.POST.get("begtime",None)
        end_time = request.POST.get("endtime",None)

        if type== "2":
            app_key = request.POST.get("app_key", None)
            print app_key
            app_list = datamanager.DataManager().test_get_applist()

            result_o = datamanager.DataManager().test_datacheck_process(app_key,begin_time,end_time)
            result ="\n".join(result_o)


            models.HistoryInfo8.objects.create(app_key=app_key,result=result)
        else:
            app_list = datamanager.DataManager().test_get_applist()
            app_key =[]
            for (m, n, z) in app_list:

                temp = n
                app_key.append(temp)
            for app_key in  app_key:
                result_o = datamanager.DataManager().test_datacheck_process(app_key,begin_time,end_time)
                result = "\n".join(result_o)
                print result
                models.HistoryInfo8.objects.create(app_key=app_key, result=result)


    history = models.HistoryInfo8.objects.all()



    return render(request, "datacheck.html", {"dt": dt,"history":history}, )

#注册

def register(request):
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #获得表单数据
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # 判断用户是否存在
            user = auth.authenticate(username = username,password = password)
            if user:
                context['userExit']=True
                return render(request, 'register.html', context)


            #添加到数据库（还可以加一些字段的处理）
            user = User.objects.create_user(username=username, password=password)
            user.save()

            #添加到session
            request.session['username'] = username
            #调用auth登录
            auth.login(request, user)
            #重定向到首页
            return redirect('/home')
    else:
        context = {'isLogin':False}
    #将req 、页面 、以及context{}（要传入html文件中的内容包含在字典里）返回
    return  render(request,'register.html',context)
@login_required
def channel(request):
    username = request.session['username']
    dt1 =[]
    env = request.POST.get("env",None)

    dt2 = []
    info ="\n"
    if request.method == "GET":
        # # app_info_1 = channel_check.ChannelCheck().test_get_applist_2(env='cloud-atlas-server.sdp.101.com')
        # # app_info_2 = channel_check.ChannelCheck().test_get_applist_2(env='cloud-atlas-server.pre1.web.nd')
        # dt1=[]
        # dt2=[]
        # # print app_info
        # for (m,n) in app_info_1:
        #     temp = {}
        #     temp["key"] = m
        #     temp["value"] = n
        #     # temp[m] = n
        #     dt1.append(temp)
        #     # dt.setdefault(m,[]).append(n.decode("utf-8"))
        # for (m, n) in app_info_2:
        #     temp = {}
        #     temp["key"] = m
        #     temp["value"] = n
        #     # temp[m] = n
        #     dt2.append(temp)
        #     # dt.setdefault(m,[]).append(n.decode("utf-8"))
        pass
    elif request.method == "POST":
        type = request.POST.get("task_type",None)
        flag =request.POST.get("hidLI",None)
        env = request.POST.get("env", None)

        begin_time = request.POST.get("begtime",None)
        end_time = request.POST.get("endtime",None)

        if type== "2":
            if env =='cloud-atlas-server.sdp.101.com':
                app_key = request.POST.get("app_key", None)
            else:
                app_key = request.POST.get("app_key_2", None)
            result_o = channel_check.ChannelCheck().test_datacheck_process(app_key,begin_time,end_time,flag,env)
            if result_o==None:
                pass
            else:
                result = "<br/>".join(result_o[1])
                app_key_e = (result_o[0])
                app_list = channel_check.ChannelCheck().test_get_applist_2(env)
                for (m, n) in app_list:
                    if m==app_key_e:
                        app_name=n
                        models.HistoryInfo10.objects.create(app_key=app_name,result=result)
        else:

            app_list = channel_check.ChannelCheck().test_get_applist_2(env)
            app_keys =[]
            for (m, n) in app_list:

                temp = m
                app_keys.append(temp)
            for app_key in  app_keys:
                result_o = channel_check.ChannelCheck().test_datacheck_process(app_key,begin_time,end_time,flag,env)
                if result_o == None:
                    pass
                else:
                    result = "<br/>".join(result_o[1])
                    app_key_e = (result_o[0])
                    for (m, n) in app_list:
                        if m == app_key_e:
                            app_name = n
                            models.HistoryInfo10.objects.create(app_key=app_name, result=result)



    # history_tmp = models.HistoryInfo10.objects.all()
    # history =  serializers.serialize("json",history_tmp)



    return render(request, "channel.html", {"dt1": dt1,"dt2":dt2}, )
@login_required
def home(request):
    username = request.session['username']
    # print username
    return render(request, "home.html", {"username": username})

def login(request):

    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # 获取表单用户密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print username,password

            # 获取的表单数据与数据库进行比较
            user = authenticate(username=username, password=password)
            if user:
                # 比较成功，跳转index
                print ('success')
                auth.login(request, user)
                request.session['username'] = username
                request.session.set_expiry(600)
                return redirect('/home')
            else:
                print('failed')
                context = {'isLogin': False, 'pawd': False}
                return render(request, 'login.html', context)
    else:
        context = {'isLogin': False, 'pswd': True}
    return render(request, 'login.html', context)

def logout(request):
    #清理cookie里保存username
    auth.logout(request)
    return redirect('/')
def upload(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        file_name = '%s/%s' % (settings.APP_ROOT, file_obj.name)
        with open(file_name, 'wb') as f:
            for filepeace in file_obj.chunks():
                f.write(filepeace)


    return render(request,'adtest.html')
def adtest(request):
    if request.method == 'POST':
        type= request.POST.get("hidLI")
        type_collect = {
            "1": "ROKTest",
            "2": "DKTest",
            "3": "KOHTest",
            "4": "ROSTest",

        }
        appname = type_collect[type]
        try:
            dir = os.getcwd() + '\\app'
            for i in os.listdir(dir):
                oldname = os.path.splitext(i)[0]
                newfile = i.replace(oldname, appname)
                oldname_tmp = dir+'\\'+str(i)
                newname_tmp = dir+'\\'+str(newfile)
                shutil.move(oldname_tmp,newname_tmp)

        except KeyError as e:
            pass
        result = AdTest.AdTest(info=appname).test_login(appname)
        models.HistoryInfo11.objects.create(result=result)
    msg = models.HistoryInfo11.objects.raw('select * from cmdb_historyinfo11  order by id  DESC limit 5')

    return render(request, 'adtest.html', {"msg": msg})
