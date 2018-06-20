# coding=utf-8
_author_ = 'yh'

import json
import time
import datetime
import random


class Data_Day():

    def get_current_time(self):
        """
        获取当前时间前一天
        """
        current_time = datetime.date.today()
        test_time = current_time + datetime.timedelta(-1)
        str_ime = test_time.strftime("%Y-%m-%d")

        return str_ime

    def get_begin_time(self):
        """
        获取当前时间前5天
        """
        current_time = datetime.date.today()
        test_time = current_time + datetime.timedelta(-8)
        str_ime = test_time.strftime("%Y-%m-%d")

        return str_ime

    def get_cloud_time(self, deltaday=0):
        """
        获取云图时间的时间格式
        @return:
        """
        microsecond = str(datetime.datetime.now().microsecond/1000)[:3]
        now_time = datetime.datetime.now()
        yes_time = now_time + datetime.timedelta(days=deltaday)
        #BJtime = yes_time + datetime.timedelta(hours=-8)
        yes_time_nyr = yes_time.strftime('%Y-%m-%dT%H:%M:%S')
        time1=yes_time_nyr + '.' + microsecond + '+08:00'


        return time1

    def get_cloud_time_later(self, deltaday=0):
        """
        获取云图时间的时间格式
        @return:
        """
        microsecond = str(datetime.datetime.now().microsecond / 1000)[:3]
        now_time = datetime.datetime.now()
        yes_time = now_time + datetime.timedelta(days=deltaday)
        # BJtime = yes_time + datetime.timedelta(hours=-8)
        yes_time_nyr = yes_time.strftime('%Y-%m-%dT%H:%M:%S')
        time2=yes_time_nyr + '.' + microsecond + '+07:00'

        return time2

    def get_cloud_time_h(self,deltaday=0):
         """
             获取云图时间时刻点
             @return:
             """

         now_time = datetime.datetime.now()
         yes_time = now_time + datetime.timedelta(days=deltaday)

         yes_time_nyr = yes_time.strftime('%Y%m%d%H')

         return yes_time_nyr

    def get_cloud_time_assign(self,assign_time):
        """
            获取云图指定时刻点
            @return:
            """

        test_time = assign_time+"T18:00:00.706+08:00"


        return test_time

    def get_cloud_time_assign_later(self, assign_time):
        """
            获取云图指定时刻点
            @return:
            """

        test_time = assign_time + "T18:00:00.706+07:30"

        return test_time

    def get_cloud_time_assign_h(self, proctime):
        """
        获取云图时间的时间格式
        @return:
        """
        microsecond = str(datetime.datetime.now().microsecond / 1000)[:3]
        now_time = datetime.datetime.now()

        yes_time_nyr = now_time.strftime('%H')
        time2 = proctime + yes_time_nyr

        return time2