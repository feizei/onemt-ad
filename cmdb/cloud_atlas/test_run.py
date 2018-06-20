# coding=utf-8
__author__ = 'cx'

import unittest
import requests
import time
import paramiko
import pymysql




from cmdb.cloud_atlas_model.event_model import EventModel
from cmdb.cloud_atlas_model.login_model import LoginModel
from cmdb.cloud_atlas_model.device_model import DeviceModel
from cmdb.cloud_atlas_model.exception_model import ExceptionModel
from cmdb.cloud_atlas_model.data_day_api import Data_Day
from cmdb.cloud_atlas_model.analyze_api import Analyze_api




import random



class SimulateCloudTest():

    # def __init__(self):
    #
    #     self.login_model = LoginModel()
    #     self.event_model = EventModel()
    #     self.device_model = DeviceModel()
    #     self.exception_model = ExceptionModel()
    #
    #




    def tearDown(self):
        pass




    def test_login2insight(self,app_key,proctime,datanum,env):
        """
        增加会话数据
        """
        self.login_model = LoginModel()
        self.event_model = EventModel()
        self.device_model = DeviceModel()
        self.exception_model = ExceptionModel()
        self.data_day = Data_Day()
        time_y = proctime[0:4]
        time_m = proctime[4:6]
        time_d = proctime[-2:]
        assign_time = time_y+'-'+ time_m+ '-'+time_d
        assign_time_h =self.data_day.get_cloud_time_assign_h(proctime)
        print(assign_time_h)

        id = 200000
        for user_id in range(id, id + int(datanum)):
            create_time = (self.data_day.get_cloud_time_assign(assign_time))
            print(create_time)
            self.login_model.set_user_id(user_id)
            self.login_model.set_device_id(user_id)
            self.login_model.set_session_id(user_id)
            self.login_model.set_function_id(21)
            self.login_model.set_app_ver(random.choice(["1.4", "1.5", "V2.1", "V2.6","V2.5.6.7","V3.5.6.7","version_0.1"]))
            self.login_model.set_session_ip(random.choice(["58.30.15.255", "193.54.67.0", "43.238.0.1", "2.6.190.56"]))
            self.login_model.set_create_time(create_time)

            datademo =self.login_model.get_data_stat_json()
            r=requests.post(env+"/v0.1/"+app_key+"/action/collect",data=datademo)
            self.login_model.set_function_id(22)
            create_time = (self.data_day.get_cloud_time_assign_later(assign_time))
            self.login_model.set_create_time(create_time)
            datademo = self.login_model.get_data_stat_json()
            r = requests.post(env+"/v0.1/"+app_key+"/action/collect", data=datademo)





    def test_device2insight(self,app_key,proctime,datanum,env,):
        """
        增加设备测试数据\

        """
        time_y = proctime[0:4]
        time_m = proctime[4:6]
        time_d = proctime[-2:]
        assign_time = time_y + '-' + time_m + '-' + time_d
        id = 200000
        for device_id in range(id, id + int(datanum)):

            create_time = (self.data_day.get_cloud_time_assign(assign_time))

            self.device_model.set_channel_id(random.choice(["91市场", "百度", "360", "QQ"]))
            self.device_model.set_create_time(create_time)
            self.device_model.set_device_id(device_id)
            self.device_model.set_model(random.choice(["小米", "华为", "魅族", "一加"]))
            self.device_model.set_system_version(random.choice(["4.3", "4.1", "5.0", "6.0"]))

            datademo = self.device_model.get_data_stat_json()
            r = requests.post(env+"/v0.1/"+app_key+"/action/collect", data=datademo)

    def test_event2insight(self,app_key,proctime,datanum,env,):
        """
        增加自定义事件数据
        """
        time_y = proctime[0:4]
        time_m = proctime[4:6]
        time_d = proctime[-2:]
        assign_time = time_y + '-' + time_m + '-' + time_d
        id = 20000
        self.ext_pro_model = {'登录方式': 'app', '登录设备': '魅族', '方式': 'wifi'}
        for user_id in range(id, id + int(datanum)):
            tag = "test_tag_%d" % (user_id)
            # self.event_model.set_event_tag(
            #     random.choice(["IM_home_news01", "IM_home_news02", "IM_home_news03", "IM_home_news04"]))
            self.event_model.set_event_tag(tag)
            self.event_model.set_event_label("online")
            self.event_model.set_event_value("10")
            self.event_model.set_event_time(self.data_day.get_cloud_time_assign(assign_time))
            self.event_model.set_user_id(user_id)
            self.event_model.set_app_ver("V0.1")
            self.event_model.set_coustoms("测试二")
            self.event_model.set_app("测试二")
            datademo = self.event_model.get_data_stat_json()
            r = requests.post(env+"/v0.1/"+app_key+"/action/collect", data=datademo)


    def test_exception2insight(self,app_key,proctime,datanum,env,):
        """
        模拟异常数据
        @return:
        """
        time_y = proctime[0:4]
        time_m = proctime[4:6]
        time_d = proctime[-2:]
        assign_time = time_y + '-' + time_m + '-' + time_d
        id = 10000
        for user_id in range(id, id + int(datanum)):
            self.exception_model.set_ex_msg(
                "java.lang.RuntimeException: Could not invoke NdDefaultModule.invokeWithPromise<ca_ret>	at com.facebook.react.bridge.BaseJavaModule$JavaMethod.invoke(Unknown Source)<ca_ret>	at com.facebook.react.cxxbridge.JavaModuleWrapper.invoke(Unknown Source)<ca_ret>	at com.facebook.react.bridge.queue.NativeRunnable.run(Native Method)<ca_ret>	at android.os.Handler.handleCallback(Handler.java:742)<ca_ret>	at android.os.Handler.dispatchMessage(Handler.java:95)<ca_ret>	at com.facebook.react.bridge.queue.MessageQueueThreadHandler.dispatchMessage(Unknown Source)<ca_ret>	at android.os.Looper.loop(Looper.java:154)<ca_ret>	at com.facebook.react.bridge.queue.MessageQueueThreadImpl$3.run(Unknown Source)<ca_ret>	at java.lang.Thread.run(Thread.java:818)<ca_ret>Caused by: java.lang.reflect.InvocationTargetException<ca_ret>	at java.lang.reflect.Method.invoke(Native Method)<ca_ret>	... 9 more<ca_ret>Caused by: java.lang.AssertionError<ca_ret>	at com.facebook.infer.annotation.Assertions.assertNotNull(Unknown Source)<ca_ret>	at com.nd.andr")
            self.exception_model.set_ex_level(3)
            self.exception_model.set_ex_time(self.data_day.get_cloud_time_assign(assign_time))
            datademo = self.exception_model.get_data_stat_json()
            r = requests.post(env+"/v0.1/"+app_key+"/action/collect", data=datademo)

    def test_autorun(self,app_key,proctime,datanum,env,mode,sqlorder,):
        print mode
        if mode == "on" :
            self.hostname = '192.168.237.127'
            self.port = 22
            self.username = 'root'
            self.password = 'cx123'

            group = Analyze_api().queryforgroup(app_key)
            self.execmd = " /home/bigdata/test"+group[0]+"-ex.sh "
            paramiko.util.log_to_file("paramiko.log")
            s = paramiko.SSHClient()
            s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            s.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)
            stdin, stdout, stderr = s.exec_command(self.execmd)
            stdin.write("Y")

            print(stdout.read())
            s.close()
            time.sleep(10)
            self.data_day = Data_Day()
            self.login_model = LoginModel()
            self.event_model = EventModel()
            self.device_model = DeviceModel()
            self.exception_model = ExceptionModel()
            self.analyze_api = Analyze_api()
            self.test_device2insight(app_key, proctime, datanum, env)
            self.test_event2insight(app_key, proctime, datanum, env)
            self.test_exception2insight(app_key, proctime, datanum, env)
            self.test_login2insight(app_key, proctime, datanum, env)

            if sqlorder =="on":
                time.sleep(60)
                self.hostname = '192.168.237.127'
                self.port = 22
                self.username = 'bigdata'
                self.password = 'bigdata.com'
                result = Analyze_api().queryforgroup(app_key)
                self.execmd2 = " /home/bigdata/test" + result[0] + ".sh " + proctime
                print (self.execmd2)
                paramiko.util.log_to_file("paramiko.log")
                s = paramiko.SSHClient()
                s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                s.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)
                stdin, stdout, stderr = s.exec_command(self.execmd2)
                stdin.write("Y")
                print(stdout.read())
                s.close()
            else:
                pass

        elif mode == None:
            self.data_day = Data_Day()
            self.login_model = LoginModel()
            self.event_model = EventModel()
            self.device_model = DeviceModel()
            self.exception_model = ExceptionModel()
            self.analyze_api = Analyze_api()
            self.test_device2insight(app_key, proctime, datanum, env)
            self.test_event2insight(app_key, proctime, datanum, env)
            self.test_exception2insight(app_key, proctime, datanum, env)
            self.test_login2insight(app_key, proctime, datanum, env)
            if sqlorder =="on":
                self.hostname = '192.168.237.127'
                self.port = 22
                self.username = 'bigdata'
                self.password = 'bigdata.com'
                result = Analyze_api().queryforgroup(app_key)
                self.execmd2 = " /home/bigdata/test" + result[0] + ".sh" + proctime
                print (self.execmd2)
                paramiko.util.log_to_file("paramiko.log")
                s = paramiko.SSHClient()
                s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                s.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)
                stdin, stdout, stderr = s.exec_command(self.execmd2)
                stdin.write("Y")
            else:
                pass

        else:

            return "app_key错误"



if __name__ == "__main__":
    unittest.main()