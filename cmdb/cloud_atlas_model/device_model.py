# coding=utf-8

__author__ = 'cx'
import json
from cmdb.cloud_atlas_model.data_day_api import Data_Day


class DeviceModel(object):
    def __init__(self):
        data_day=Data_Day()
        self.create_time = data_day.get_cloud_time()
        self.bussiness_type = 'device'
        self.device_id = '113322'
        self.model = 'huawei'
        self.os_system = 'Android'
        self.system_version = '5.0'
        self.screen_height = '800'
        self.screen_width = '1024'
        self.coustome = 'value0'
        self.app = 'value'
        self.channel_id = 'default'

    def get_data_stat_json(self,empty_param=None):
         orign_json = {
           "data":[
            {
                "bussiness_type": self.bussiness_type,
                "properties":
                {
                    "device_id": self.device_id,
                    "model": self.model,
                    "os_system": self.os_system,
                    "system_version": self.system_version,
                    "screen_height": self.screen_height,
                    "screen_width": self.screen_width,
                    "channel_id": self.channel_id,
                    "create_time": self.create_time
                },
                "ext_properties":{
                    "coustome" : self.coustome,
                    "app" : self.app,
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

    def set_bussiness_type(self,bussiness_type):

        self.bussiness_type = bussiness_type

    def get_device_id (self):

        return self.device_id

    def set_device_id(self,device_id):

        self.device_id = device_id

    def get_model(self):
        return self.model

    def set_model(self,model):

        self.model=model

    def get_os_system(self):

        return self.os_system

    def set_os_system(self,os_system):
        self.os_system = os_system

    def get_system_version(self):

        return  self.system_version
    def set_system_version(self,system_version):

        self.system_version = system_version
    def get_screen_height(self):

        return  self.screen_height

    def set_screen_height(self,screen_height):

        self.screen_height= screen_height

    def get_screen_width(self):

        return  self.screen_width

    def set_screen_width(self,screen_width):

        self.screen_width= screen_width

    def get_create_time(self):

        return  self.create_time

    def set_create_time(self,create_time):

        self.create_time = create_time

    def get_cousome(self):

        return  self.coustome

    def set_coustome(self,coustome):

        self.coustome = coustome

    def get_app(self):

        return  self.app

    def set_app(self,app):

        self.app= app

    def get_channel_id(self):
        return self.channel_id

    def set_channel_id(self, channel_id):

        self.channel_id = channel_id










