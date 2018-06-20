# coding=utf-8

import pymysql
import datetime
import time
import requests
import  unittest
import random
import base64
import hashlib


from cmdb.cloud_atlas.rand import CoRand
import math


import uuid


from datetime import datetime as dt
from bs4 import  BeautifulSoup


import  json
from hmac import new as hmac
import  lxml
import sys
reload(sys)
sys.setdefaultencoding("utf-8")





class DataManager():



    def tearDown(self):
        pass







    def test_get_mysql_data(self,app_key,task_time,group="0"):
        self.host = "172.24.133.135"
        self.port = 3301
        self.user = "user_qa"
        self.password = "user_qa@test007"
        self.db = "production_mysql_collection_"+group
        task_time_a = datetime.datetime.strptime(task_time,'%Y.%m.%d')
        task_time_n = datetime.datetime.strftime(task_time_a,'%Y%m%d')
        delta_a = datetime.timedelta(days=-1)
        delta_b = datetime.timedelta(days=1)
        task_time_c = task_time_a+delta_a
        task_time_y = datetime.datetime.strftime(task_time_c, '%Y%m%d')
        task_time_d = task_time_a+delta_b
        task_time_f = datetime.datetime.strftime(task_time_d, '%Y%m%d')
        create_time = datetime.datetime.strftime(task_time_a,'%Y-%m-%d')
        create_time_f = datetime.datetime.strftime(task_time_d,'%Y-%m-%d')
        conn3 = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password,
                                db=self.db, charset='utf8mb4')
        cur = conn3.cursor()
        query = "SELECT count(distinct c.device_id) from (select * from prepub_mysql_cloud_atlas_collection_0.login_"+task_time_y+" where app_key ='"+app_key+"' and create_time>='"+create_time+"'and create_time<insert_time and insert_time>='"+create_time+"' union select * from prepub_mysql_cloud_atlas_collection_0.login_"+task_time_n+" where app_key ='"+app_key+"' and create_time>='"+create_time+"' and create_time< '"+create_time_f+"'union select * from prepub_mysql_cloud_atlas_collection_0.login_"+task_time_f+" where app_key ='"+app_key+"' and create_time>='"+create_time+"' and create_time<'"+create_time_f+"' and insert_time<'"+create_time_f+"')as c"

        cur.execute(query)
        data = cur.fetchone()

        cur.close()
        conn3.close()



        return (data)[0]



#     def get_server_data(self):
#
#         r = requests.get("http://cloud-atlas-server.sdp.101.com/v0.2/kpis/product/report?date0=2017.11.05%20-%20+2017.12.05&kpiCode=K0100002,K0100003,K0100004,K0100012,K0100014,K0200001&productCode=im&userId=113322")
# #/v0.2/kpis/product/report?&date0='2017.11.05'%20-%20'+2017.12.05+'&kpiCode=K0100002,K0100003,K0100004,K0100012,K0100014,K0200001&productCode='im'&userId='+userId
#         book = xlrd.open_workbook("pytest.xls")
#         sheet = book.sheet_by_name("sheet0")
#         data ="20170701"
#         data_2 = data[0:4]+'-'+data[4:6]+'-'+data[-2:]
#         nrows = sheet.nrows
#         for i in range(1,nrows):
#             cell_0 = sheet.row(i)[1].value
#             if cell_0 == data_2:
#                 active_cnt = sheet.row(i)[2]
#                 new_cnt = sheet.row(i)[4]
#                 sur_cnt = sheet.row(i)[3]
#                 return active_cnt,new_cnt,sur_cnt
#         return
    def queryforgroup(self, app_key):
        self.host = "172.24.133.135"
        self.port = 3301
        self.user = "user_qa"
        self.password = "user_qa@test007"
        self.db = "prepub_mysql_cloud_atlas_master"
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password,
                               db=self.db, charset='utf8')
        cur = conn.cursor()
        code = "SELECT app_group FROM sys_app_group_db WHERE app_key=" + "\"" + app_key + "\""

        i = cur.execute(code)
        b = cur.fetchone()

        if b == None:
            return ([3])
        else:
            return (b)


    def test_get_uc_tokens(self,):

        self.username = '113322'
        self.password = '80fba977d063a6f7262a8a9c95f61140'
        json_body = {
            "login_name": self.username,
            "password": self.password,
            "org_name": "nd"

        }
        params = json.dumps(json_body)
        r = requests.post("https://aqapi.101.com/v0.93/tokens", data=params,headers={"Content-Type":"application/json"})

        return r.json()
    def test_parse_uc_tokens(self):

        data_dec = self.test_get_uc_tokens()
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
        request_content = nonce + '\n' + "GET" + '\n' + "/tokens" + '\n' + "cloud-atlas-server.sdp.101.com" + '\n'
        mac = base64.b64encode(hmac(str(mac_key), str(request_content), digestmod=hashlib.sha256).digest())
        authorization = 'MAC id="' + str(id) + '",nonce="' + str(nonce) + '",mac="' + str(mac) + '"'

        return str(authorization)




    def test_parse_uc_token_2(self,app_key,begin_time,end_time):

        data_dec = self.test_get_uc_tokens()
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
        # print nonce
        request_content = nonce + '\n' + "GET" + '\n' + "/v0.2/kpis/"+app_key+"/detail/K0100002,K0100003,K0100004,K0100012,K0100014,K0200001/date/"+begin_time+"%20-%20"+end_time + '\n' + "cloud-atlas-server.sdp.101.com" + '\n'
        mac = base64.b64encode(hmac(str(mac_key), str(request_content), digestmod=hashlib.sha256).digest())
        authorization = 'MAC id="' + str(id) + '",nonce="' + str(nonce) + '",mac="' + str(mac) + '"'


        return str(authorization)

    def test_get_cloud_token(self):

        authorization = self.test_parse_uc_tokens()
        response=requests.get("http://cloud-atlas-server.sdp.101.com/tokens",headers={'Authorization':authorization})
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

    def test_get_server_data(self,app_key,begin_time ,end_time):

        authorization = self.test_parse_uc_token_2(app_key,begin_time,end_time)

        authorization_cloud = self.test_get_cloud_token()
        header = {"authorization": authorization,"authorization-cloud":authorization_cloud}

        r = requests.get("http://cloud-atlas-server.sdp.101.com/v0.2/kpis/"+app_key+"/detail/K0100002,K0100003,K0100004,K0100012,K0100014,K0200001/date/"+begin_time+"%20-%20"+end_time,headers=header)

        mylist = r.json()['obj']

        newlist =[]

        for index in range(len(mylist)):
             newlist_tmp =  mylist[index]['kpi_value_list']

             newlist_tmp_2 =int(newlist_tmp[0])

             newlist.append(newlist_tmp_2)

        return  newlist

    def test_datacheck_process(self,app_key,begin_time,end_time):
        sql_list = []

        task_tm =begin_time
        task_tmp = datetime.datetime.strptime(begin_time, '%Y.%m.%d')
        task_tmp_2 = datetime.datetime.strptime(end_time, '%Y.%m.%d')
        delta =task_tmp_2-task_tmp

        delta_days = delta.days
        if task_tm != end_time:
            i=0
            for i in range(0,delta_days+1):
             task_tmp_3 =task_tmp+ datetime.timedelta(days=i)
             task_tmp_4 =datetime.datetime.strftime(task_tmp_3,'%Y.%m.%d')
             sql_list.append(self.test_get_mysql_data(app_key,task_tmp_4))
             i+=1
        else:
            sql_list.append(self.test_get_mysql_data(app_key, task_tm))

        server_list =  self.test_get_server_data(app_key,begin_time ,end_time)


        n = 0
        result =[]
        for i in range(len(sql_list)):
             if sql_list[n] ==server_list[n]:

                 print "数字校验通过"
                 n=n+1
             else:
                 error_date_tmp = task_tmp+datetime.timedelta(days=i)
                 error_date =datetime.datetime.strftime(error_date_tmp,'%Y-%m-%d')
                 error_info= "数值校验存在差异，具体日期为 "+error_date+" 实际为 "+str(sql_list[i])
                 result.append(error_info)

        return (result)

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























