# coding=utf-8

__author__ = 'cx'
import json
import sys
import  random
from cmdb.cloud_atlas_model.data_day_api import Data_Day

class ExceptionModel(object):
    def __init__(self):
        data_day = Data_Day()
        self.bussiness_type = "exception_log"
        self.ex_time = data_day.get_cloud_time()
        self.ex_type = "0"
        self.ex_level = "21"
        self.ex_msg = ''
        self.app_ver = 'null'

    def get_data_stat_json(self, empty_param=None):
        orign_json = {
            "data":[
                {
                    "bussiness_type": self.bussiness_type,
                    "properties":
                        {
                            "ex_type": self.ex_type,
                            "ex_level": self.ex_level,
                            "ex_time": self.ex_time,
                            "ex_msg": self.ex_msg,
                            "app_ver": self.app_ver
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

    def get_ex_type(self):
        return self.ex_type

    def set_ex_type(self, ex_type):
        self.ex_type = ex_type

    def get_ex_level(self):
        return self.ex_level

    def set_ex_level(self, ex_level):
        self.ex_level = ex_level

    def get_ex_time(self):
        return self.ex_time

    def set_ex_time(self, ex_time):
        self.ex_time = ex_time

    def get_ex_msg(self):
        return self.ex_msg

    def set_ex_msg(self, ex_msg):
        self.ex_msg = ex_msg

    def get_app_ver(self):
        return  self.app_ver

    def set_app_ver(self,app_ver):
        self.app_ver = app_ver
