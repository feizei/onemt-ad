# coding=utf-8

import pymysql
import datetime
import time
import requests
import random
import base64
import hashlib


from cmdb.cloud_atlas.rand import CoRand


import uuid




import  json
from hmac import new as hmac
import sys
reload(sys)
sys.setdefaultencoding("utf-8")





class ChannelCheck():



    def tearDown(self):
        pass














    def test_get_uc_tokens(self,env):
        if env =="cloud-atlas-server.sdp.101.com":
            self.username = '113322'
            self.password = '80fba977d063a6f7262a8a9c95f61140'
            uc_host = 'https://aqapi.101.com/v0.93/tokens'
        else:
            self.username = '113322'
            self.password = 'cfd89e4252f5a9d7d334ab67b9d9ef36'
            uc_host = 'http://101uccenter.beta.web.sdp.101.com/v0.93/tokens'
        json_body = {
            "login_name": self.username,
            "password": self.password,
            "org_name": "nd"

        }
        params = json.dumps(json_body)

        r = requests.post(uc_host, data=params,headers={"Content-Type":"application/json"})
        return r.json()
    def test_parse_uc_tokens(self,env):

        data_dec = self.test_get_uc_tokens(env)

        self.rand_o = CoRand()
        id = data_dec['access_token']
        mac_key = data_dec['mac_key']

        self.rand_o = CoRand()
        now = int(time.time())
        if len(str(now)) == 10:
            timestamp = str(now) + '000'
        else:
            timestamp = str(now)[0:9] + str(int(float(str(now)[9:]) * 1000))
        nonce = timestamp + ':' + self.rand_o.randomword(4) + str(random.randrange(1000, 9999))
        request_content = nonce + '\n' + "GET" + '\n' + "/tokens" + '\n' + env + '\n'
        mac = base64.b64encode(hmac(str(mac_key), str(request_content), digestmod=hashlib.sha256).digest())
        authorization = 'MAC id="' + str(id) + '",nonce="' + str(nonce) + '",mac="' + str(mac) + '"'

        return str(authorization)






    def test_parse_uc_token_2(self,app_key,begin_time,end_time,env):
        # 整体趋势鉴权
        data_dec = self.test_get_uc_tokens(env)
        self.rand_o = CoRand()
        id = data_dec['access_token']
        mac_key = data_dec['mac_key']

        self.rand_o = CoRand()
        now = int(time.time())

        if len(str(now)) == 10:
            timestamp = str(now) + '000'
        else:
            timestamp = str(now)[0:9] + str(int(float(str(now)[9:]) * 1000))
        nonce = timestamp + ':' + self.rand_o.randomword(4) + str(random.randrange(1000, 9999))

        request_content = nonce + '\n' + "GET" + '\n' + "/v0.2/kpis/"+app_key+"/detail/K0100002,K0100003,K0100004,K0100012,K0100014,K0200001/date/"+begin_time+"%20-%20"+end_time + '\n' + env + '\n'
        mac = base64.b64encode(hmac(str(mac_key), str(request_content), digestmod=hashlib.sha256).digest())
        authorization = 'MAC id="' + str(id) + '",nonce="' + str(nonce) + '",mac="' + str(mac) + '"'


        return str(authorization)

    def test_parse_uc_token_3(self, app_key, begin_time, end_time,env):
        #渠道统计鉴权
        data_dec = self.test_get_uc_tokens(env)
        self.rand_o = CoRand()
        id = data_dec['access_token']
        mac_key = data_dec['mac_key']

        self.rand_o = CoRand()
        now = int(time.time())

        if len(str(now)) == 10:
            timestamp = str(now) + '000'
        else:
            timestamp = str(now)[0:9] + str(int(float(str(now)[9:]) * 1000))
        nonce = timestamp + ':' + self.rand_o.randomword(4) + str(random.randrange(1000, 9999))

        request_content = nonce + '\n' + "GET" + '\n' + "/v0.2/channels/info?beginDate="+begin_time+"&endDate="+end_time+"&appKey="+app_key+"&showType=user" + '\n' + env + '\n'
        mac = base64.b64encode(hmac(str(mac_key), str(request_content), digestmod=hashlib.sha256).digest())
        authorization = 'MAC id="' + str(id) + '",nonce="' + str(nonce) + '",mac="' + str(mac) + '"'

        return str(authorization)

    def test_parse_uc_token_4(self, app_key, begin_time, end_time,env):
        #留存页面鉴权
        data_dec = self.test_get_uc_tokens(env)
        self.rand_o = CoRand()
        id = data_dec['access_token']
        mac_key = data_dec['mac_key']

        self.rand_o = CoRand()
        now = int(time.time())

        if len(str(now)) == 10:
            timestamp = str(now) + '000'
        else:
            timestamp = str(now)[0:9] + str(int(float(str(now)[9:]) * 1000))
        nonce = timestamp + ':' + self.rand_o.randomword(4) + str(random.randrange(1000, 9999))

        request_content = nonce + '\n' + "GET" + '\n' + "/v0.2/users/retain?productCode="+app_key+"&kpiCode=K0100016&date0="+begin_time+"&date1="+end_time+"&compareParameter=daily" + '\n' + env + '\n'
        mac = base64.b64encode(hmac(str(mac_key), str(request_content), digestmod=hashlib.sha256).digest())
        authorization = 'MAC id="' + str(id) + '",nonce="' + str(nonce) + '",mac="' + str(mac) + '"'

        return str(authorization)

    def test_parse_uc_token_5(self, app_key, begin_time,env):
        # 区域页面鉴权
        data_dec = self.test_get_uc_tokens(env)
        self.rand_o = CoRand()
        id = data_dec['access_token']
        mac_key = data_dec['mac_key']

        self.rand_o = CoRand()
        now = int(time.time())

        if len(str(now)) == 10:
            timestamp = str(now) + '000'
        else:
            timestamp = str(now)[0:9] + str(int(float(str(now)[9:]) * 1000))
        nonce = timestamp + ':' + self.rand_o.randomword(4) + str(random.randrange(1000, 9999))

        request_content = nonce + '\n' + "GET" + '\n' + "/v0.2/users/distribution?periodType=D&appId="+app_key+"&day="+begin_time+"&userType=K0300001&showType=province" + '\n' + env + '\n'
        mac = base64.b64encode(hmac(str(mac_key), str(request_content), digestmod=hashlib.sha256).digest())
        authorization = 'MAC id="' + str(id) + '",nonce="' + str(nonce) + '",mac="' + str(mac) + '"'

        return str(authorization)

    def test_parse_uc_token_7(self, app_key, begin_time, end_time,env):

        # 活跃页面鉴权
        data_dec = self.test_get_uc_tokens(env)
        self.rand_o = CoRand()
        id = data_dec['access_token']
        mac_key = data_dec['mac_key']

        self.rand_o = CoRand()
        now = int(time.time())

        if len(str(now)) == 10:
            timestamp = str(now) + '000'
        else:
            timestamp = str(now)[0:9] + str(int(float(str(now)[9:]) * 1000))
        nonce = timestamp + ':' + self.rand_o.randomword(4) + str(random.randrange(1000, 9999))

        request_content = nonce + '\n' + "GET" + '\n' + "/v0.2/users/active?date0=" + begin_time + "&date1=" + end_time + "&productCode="+app_key+"&kpiCode=K0100018&compareParameter=daily" + '\n' + env + '\n'
        mac = base64.b64encode(hmac(str(mac_key), str(request_content), digestmod=hashlib.sha256).digest())
        authorization = 'MAC id="' + str(id) + '",nonce="' + str(nonce) + '",mac="' + str(mac) + '"'


        return str(authorization)

    def test_get_cloud_token(self,env):
        #云图鉴权
        authorization = self.test_parse_uc_tokens(env)
        response=requests.get("http://"+env+"/tokens",headers={'Authorization':authorization})
        c_uuid = response.json()
        self.connectTxt = '$@$'
        self.mixTxt = ['cw', 'ky', 'yl']
        s = str(c_uuid['obj'] + self.connectTxt + "113322")
        md5 = hashlib.md5(s)
        cloud_key = md5.hexdigest()
        cloud_token = cloud_key + self.connectTxt + str(uuid.uuid1())

        for j in range(0, len(self.mixTxt)):
            string2 = ''
            for i in range(len(cloud_token)):
                if i == 0:
                    string2 += cloud_token[0]+self.mixTxt[j]
                else:
                    string2 += cloud_token[i]
            new_cloud_token = string2

            cloud_token = base64.encodestring(new_cloud_token)
            cloud_token = cloud_token.replace("\n", "")


        return cloud_token

    def test_get_server_data_1(self,app_key,begin_time ,end_time,flag,env):
        # 整体趋势页面数据
        authorization = self.test_parse_uc_token_2(app_key,begin_time,end_time,env)

        authorization_cloud = self.test_get_cloud_token(env)
        header = {"authorization": authorization,"authorization-cloud":authorization_cloud}

        r = requests.get("http://"+env+"/v0.2/kpis/"+app_key+"/detail/K0100002,K0100003,K0100004,K0100012,K0100014,K0200001/date/"+begin_time+"%20-%20"+end_time,headers=header)

        mylist = r.json()['obj']

        newlist =[]

        for index in range(len(mylist)):
           if flag == 'new':
             newlist_tmp =  mylist[index]['kpi_value_list']

             newlist_tmp_2 =int(newlist_tmp[2])

             newlist.append(newlist_tmp_2)
           elif flag =='act':
             newlist_tmp = mylist[index]['kpi_value_list']

             newlist_tmp_2 = int(newlist_tmp[0])

             newlist.append(newlist_tmp_2)
        return  newlist



    def test_get_server_data_2(self, app_key, begin_time,flag,env):
        # 渠道页面数据
        end_time= begin_time
        authorization = self.test_parse_uc_token_3(app_key, begin_time,end_time,env)

        authorization_cloud = self.test_get_cloud_token(env)
        header = {"authorization": authorization, "authorization-cloud": authorization_cloud}

        r = requests.get("http://"+env+"/v0.2/channels/info?beginDate="+begin_time+"&endDate="+begin_time+"&appKey="+app_key+"&showType=user" , headers=header)

        mylist = r.json()['obj']

        newlist = 0
        final_list =[]
        for index in range(len(mylist)):
          if flag =='new':
            newlist_tmp = mylist[index]['new_user_cnt']
            newlist +=newlist_tmp

          elif flag =='act':
            newlist_tmp = mylist[index]['active_user_cnt']
            newlist += newlist_tmp


        print newlist

        return newlist

    def test_get_server_data_3(self, app_key, begin_time,end_time,env):
        #留存页面新增数据
        authorization = self.test_parse_uc_token_4(app_key, begin_time, end_time,env)

        authorization_cloud = self.test_get_cloud_token(env)
        header = {"authorization": authorization, "authorization-cloud": authorization_cloud}

        r = requests.get(
            "http://"+env+"/v0.2/users/retain?productCode="+app_key+"&kpiCode=K0100016&date0="+begin_time+"&date1="+end_time+"&compareParameter=daily",
            headers=header)

        mylist = r.json()['obj']

        newlist = 0
        final_list = []
        for index in range(len(mylist)):

            newlist_tmp = mylist[index]['user_num']


            final_list.append(int(newlist_tmp))

        return final_list

    def test_get_server_data_4(self, app_key, begin_time,flag,env):
        #区域页面数据
        authorization = self.test_parse_uc_token_5(app_key, begin_time,env)

        authorization_cloud = self.test_get_cloud_token(env)
        header = {"authorization": authorization, "authorization-cloud": authorization_cloud}

        r = requests.get(
            "http://"+env+"/v0.2/users/distribution?periodType=D&appId="+app_key+"&day="+begin_time+"&userType=K0300001&showType=province",
            headers=header)

        mylist = r.json()['obj']


        newlist = 0
        final_list = []
        for index in range(len(mylist)):
            if flag == 'new':
                newlist_tmp = mylist[index]['new_user_cnt']
                newlist+=newlist_tmp
                final_list.append(newlist)
            elif flag=='act':
                newlist_tmp = mylist[index]['active_user_cnt']
                newlist += newlist_tmp
                final_list.append(newlist)


        return newlist

    def test_get_server_data_5(self, app_key, begin_time,end_time,env ):
        # 活跃页面数据
        authorization = self.test_parse_uc_token_7(app_key, begin_time,end_time,env)

        authorization_cloud = self.test_get_cloud_token(env)
        header = {"authorization": authorization, "authorization-cloud": authorization_cloud}

        r = requests.get(
            "http://"+env+"/v0.2/users/active?date0=" + begin_time + "&date1=" + end_time + "&productCode="+app_key+"&kpiCode=K0100018&compareParameter=daily",
            headers=header)

        mylist = r.json()['obj']

        newlist = 0
        final_list = []
        for index in range(len(mylist)):

            newlist_tmp = mylist[index]['active_user_cnt']
            final_list.append(newlist_tmp)


        return final_list

    def test_datacheck_process(self,app_key,begin_time,end_time,flag,env):


        task_tm =begin_time.replace(".","")
        task_end =end_time.replace(".","")
        task_tmp = datetime.datetime.strptime(begin_time, '%Y.%m.%d')
        task_tmp_2 = datetime.datetime.strptime(end_time, '%Y.%m.%d')
        delta =task_tmp_2-task_tmp

        delta_days = delta.days
        server_list_2=[]
        server_list_4 = []
        if task_tm != end_time:
            i = 0
            for i in range(0, delta_days + 1):
                task_tmp_3 = task_tmp + datetime.timedelta(days=i)
                task_tmp_4 = datetime.datetime.strftime(task_tmp_3, '%Y.%m.%d')
                task_tmp_5=task_tmp_4.replace(".","")

                server_list_2.append(self.test_get_server_data_2(app_key,task_tmp_5,flag,env))
                server_list_4.append(self.test_get_server_data_4(app_key,task_tmp_5,flag,env))

                i += 1
        else:
            server_list_2.append(self.test_get_server_data_2(app_key, task_tm,flag,env))
            server_list_4.append(self.test_get_server_data_4(app_key,task_tm,flag,env))


        server_list_1 =  self.test_get_server_data_1(app_key,begin_time ,end_time,flag,env)
        # server_list_3 =  self.test_get_server_data_3(app_key,task_tm ,task_end,env)
        server_list_5 =  self.test_get_server_data_5(app_key,task_tm,task_end,env)
        print server_list_1, server_list_2 ,server_list_4
        result =[]
        if flag =='new':

            for n in range(len(server_list_1)):


                 if server_list_1[n] == server_list_2[n]  and server_list_1[n] == server_list_4[n]:

                      n += 1


                 else:

                      error_date_tmp = task_tmp+datetime.timedelta(days=n)
                      error_date =datetime.datetime.strftime(error_date_tmp,'%Y-%m-%d')
                      error_info= error_date+" 数值校验(新增)存在差异，具体为 整体趋势： "+str(server_list_1[n])+" 渠道："+str(server_list_2[n])+" 留存："+str(server_list_3[n])+" 区域："+str(server_list_4[n])
                      result.append(error_info)
                      n+=1
        elif flag=='act':
            for n in range(len(server_list_1)):

                if server_list_1[n] == server_list_2[n] and server_list_1[n] == server_list_5[n] :
                    n += 1

                else:
                    error_date_tmp = task_tmp + datetime.timedelta(days=n)
                    error_date = datetime.datetime.strftime(error_date_tmp, '%Y-%m-%d')
                    error_info = error_date + " 数值校验(活跃)存在差异，具体为 整体趋势： " + str(server_list_1[n]) + " 渠道：" + str(
                        server_list_2[n])  + " 活跃分析：" + str(server_list_5[n])
                    result.append(error_info)
                    n += 1
        if result==[]:
            return None
        else:
            print app_key,(result)
            return app_key,(result)

    def test_get_applist(self ):
        #获取应用名、app_key及对应库名
        self.host = "172.24.133.135"
        self.port = 3301
        self.user = "user_qa"
        self.password = "user_qa@test007"
        self.db = "prepub_mysql_cloud_atlas_master"

        conn3 = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password,
                                db=self.db, charset='utf8')
        cur = conn3.cursor()
        query = "SELECT app_id,app_name,app_group FROM `dim_sys_app` as a JOIN  `sys_app_group_db`  b where b.app_key =a.app_id"

        cur.execute(query)
        data = cur.fetchall()


        cur.close()
        conn3.close()

        return  list(data)

    def test_get_applist_2(self,env):
        # 获取应用名、app_key及对应库名
        authorization = self.test_parse_uc_token_6(env)

        authorization_cloud = self.test_get_cloud_token(env)
        header = {"authorization": authorization, "authorization-cloud": authorization_cloud}

        r = requests.get("http://"+env+"/v0.2/apps",
            headers=header)

        appslist = r.json()['rows']

        newlist = 0
        final_list = []
        for index in range(len(appslist)):

            app_id = appslist[index]['app_id']
            app_name = appslist[index]['app_name']
            if  'ap15' in str(app_name):
                pass
            else:
                list_tmp =(app_id,app_name)
                final_list.append(list_tmp)

        return final_list


    def test_parse_uc_token_6(self, env):
        # app列表鉴权
        data_dec = self.test_get_uc_tokens(env)
        self.rand_o = CoRand()
        id = data_dec['access_token']
        mac_key = data_dec['mac_key']

        self.rand_o = CoRand()
        now = int(time.time())

        if len(str(now)) == 10:
            timestamp = str(now) + '000'
        else:
            timestamp = str(now)[0:9] + str(int(float(str(now)[9:]) * 1000))
        nonce = timestamp + ':' + self.rand_o.randomword(4) + str(random.randrange(1000, 9999))

        request_content = nonce + '\n' + "GET" + '\n' + "/v0.2/apps" + '\n' + env + '\n'
        mac = base64.b64encode(hmac(str(mac_key), str(request_content), digestmod=hashlib.sha256).digest())
        authorization = 'MAC id="' + str(id) + '",nonce="' + str(nonce) + '",mac="' + str(mac) + '"'

        return str(authorization)























