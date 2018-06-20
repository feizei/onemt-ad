# coding=utf-8

__author__ = 'yh'
import json
import sys
import  random
from cmdb.cloud_atlas_model.data_day_api import Data_Day

class LoginModel(object):
    def __init__(self):
        data_day = Data_Day()
        self.bussiness_type = "login"
        self.account_id = "11122233"
        self.function_id = "21"
        self.create_time = data_day.get_cloud_time()
        self.user_id = "1112321312"
        self.app_ver = "v2.1.0"
        self.flag = "1"
        self.device_id = "123"
        self.reason = 'reason'
        self.session_id = '123456'
        self.session_ip= ""

    def get_data_stat_json(self, empty_param=None):
        orign_json = {
            "data":[
                {
                    "bussiness_type": self.bussiness_type,
                    "properties":
                        {
                            "account_id": self.account_id,
                            "function_id": self.function_id,
                            "create_time": self.create_time,
                            "user_id": self.user_id,
                            "app_ver": self.app_ver,
                            "flag": self.flag,
                            "device_id": self.device_id,
                            "reason": self.reason,
                            "session_id": self.session_id,
                            "session_ip": self.session_ip
                        }
                }
            ]
        }

        if empty_param != None:
            empty_param_list = empty_param.split(',')
            for j in range(0, len(empty_param_list)):
                if orign_json.get("data")[0].has_key(empty_param_list[j]):
                    orign_json.get("data")[0].pop(empty_param_list[j])
                if orign_json.get("data")[0].get("properties").has_key(empty_param_list[j]):
                    orign_json.get("data")[0].get("properties").pop(empty_param_list[j])

        json_data = json.dumps(orign_json)

        return json_data

    def get_bussiness_type(self):
        return self.bussiness_type

    def set_bussiness_type(self, bussiness_type):
        self.bussiness_type = bussiness_type

    def get_account_id(self):
        return self.account_id

    def set_account_id(self, account_id):
        self.account_id = account_id

    def get_function_id(self):
        return self.function_id

    def set_function_id(self, function_id):
        self.function_id = function_id

    def get_create_time(self):
        return self.create_time

    def set_create_time(self, create_time):
        self.create_time = create_time

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_app_ver(self):
        return self.app_ver

    def set_app_ver(self, app_ver):
        self.app_ver = app_ver

    def get_flag(self):
        return self.flag

    def set_flag(self, flag):
        self.flag = flag

    def get_device_id(self):
        return self.device_id

    def set_device_id(self, device_id):
        self.device_id = device_id

    def get_reason(self):
        return self.reason

    def set_reason(self, reason):
        self.reason = reason

    def get_session_id(self):
        return self.session_id

    def set_session_id(self, session_id):
        self.session_id = session_id

    def get_session_ip(self):
        return self.session_ip

    def set_session_ip(self,session_ip):
        self.session_ip = session_ip