# coding=utf-8

__author__ = 'cx'
import json
import sys
import  random
from cmdb.cloud_atlas_model.data_day_api import Data_Day

class EventModel(object):
    def __init__(self):
        data_day = Data_Day()
        self.bussiness_type = "custom_event_log"
        self.event_time = data_day.get_cloud_time()
        self.event_tag = "test001"
        self.event_label = "21"
        self.event_value = '1'
        self.device_id = 'E629C01483FB73EC9ECE58FEAAD3A49-99803f94-a577-4737-8e31-e5aea7b2d2b2'
        self.user_id = '113322'
        self.app_ver = 'v1.0'
        self.coustoms='values0'
        self.app='values1'

    def get_data_stat_json(self,empty_param=None):
        orign_json = {
            "data":[
                {
                    "bussiness_type": self.bussiness_type,
                    "properties":
                        {
                            "event_tag": self.event_tag,
                            "event_label": self.event_label,
                            "event_time": self.event_time,
                            "event_value": self.event_value,
                            "device_id": self.device_id,
                            "user_id":self.user_id,
                            "app_ver":self.app_ver
                        },
                    "ext_properties":{
                        "coustoms":self.coustoms,
                        "app":self.app

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

    def get_data_stat_json_event(self, empty_param=None):
        orign_json = {
            "data": [
                {
                    "bussiness_type": self.bussiness_type,
                    "properties":
                        {
                            "event_tag": self.event_tag,
                            "event_label": self.event_label,
                            "event_time": self.event_time,
                            "event_value": self.event_value,
                            "device_id": self.device_id,
                            "user_id": self.user_id,
                            "app_ver": self.app_ver
                        },
                    "ext_properties": {
                        "coustoms": self.coustoms,
                        "app": self.app

                    }

                }
            ]
        }


        for index in range(0, 10):
            tags ="x_new_tag_%d" % (index)
            self.set_event_tag(tags)
            dataJs = {
                "bussiness_type": self.bussiness_type,
                "properties":
                    {
                        "event_tag": self.event_tag,
                        "event_label": self.event_label,
                        "event_time": self.event_time,
                        "event_value": self.event_value,
                        "device_id": self.device_id,
                        "user_id": self.user_id,
                        "app_ver": self.app_ver
                    },
                "ext_properties": {
                    "coustoms": self.coustoms,
                    "app": self.app

                }
            }
            orign_json.get("data").append(dataJs)

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

    def get_event_tag(self):
        return self.event_tag

    def set_event_tag(self, event_tag):
        self.event_tag = event_tag

    def get_event_label(self):
        return self.event_label

    def set_event_label(self, event_label):
        self.event_label = event_label

    def get_event_time(self):
        return self.event_time

    def set_event_time(self, event_time):
        self.event_time = event_time

    def get_event_value(self):
        return self.event_value

    def set_event_value(self, event_value):
        self.event_value = event_value

    def get_device_id(self):
        return  self.device_id

    def set_device_id(self,device_id):
        self.device_id = device_id

    def get_user_id(self):
        return self.user_id

    def set_user_id(self,user_id):
        self.user_id = user_id

    def get_app_ver(self):
        return self.app_ver

    def set_app_ver(self,app_ver):
        self.app_ver = app_ver

    def set_coustoms(self,coustoms):
        self.coustoms=coustoms

    def get_counstoms(self):
        return self.coustoms

    def set_app(self,app):
        self.app = app