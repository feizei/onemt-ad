# coding=utf-8
__author__ = 'cx'
import sys
import chardet

reload(sys)
sys.setdefaultencoding('utf-8')
import unittest
from appium import webdriver
import pymysql
import logging
import os
import time
from hamcrest import *
import sys
from cmdb.cof.conf import MyCfg
import logging
import datetime

PATH = lambda p: os.path.abspath(

    os.path.join(os.path.dirname(__file__), p)

)


class AdTest(object):

    def __init__(self, info=""):
        self.my_cfg = MyCfg('cfg.ini')
        self.info_collect = {
            "ROKTest": "rok_info",
            "DKTest": "dk_info",
            "KOHTest": "koh_info",
            "ROSTest": "ros_info",

        }
        self.my_cfg.set_section(self.info_collect[info])
        self.dbname = self.my_cfg.get('dbname')
        self.host = self.my_cfg.get('host')
        self.user = self.my_cfg.get('user')
        self.passwd = self.my_cfg.get('passwd')
        self.coo = self.my_cfg.get('coo')
        self.params = self.my_cfg.get('params').split(',')
        self.c_table = self.my_cfg.get('check_table').split(',')
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.INFO)
        nowtime = datetime.datetime.now().strftime("%Y-%m-%d%H%M")
        handler = logging.FileHandler(os.getcwd() + "\\log\\AdTest" + nowtime + ".txt")
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def clearUp(self, ):
        """
        清空数据库对应记录
        :return:
        """
        conn = pymysql.connect(host=self.host, port=3306, user=self.user, passwd=self.passwd, db=self.dbname,
                               charset='utf8')
        cursor = conn.cursor()
        for table in self.c_table:
            sql = "Delete from " + table + " where deviceid = \"3F6F5A52-B35B-4646-9B91-06127323F152\""
            cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def parseData(self):
        """
         初步校验:
        """
        conn = pymysql.connect(host=self.host, port=3306, user=self.user, passwd=self.passwd, db=self.dbname,
                               charset='utf8')
        cursor = conn.cursor()
        for table in self.c_table:
            sql = "select * from " + table + " where deviceid=\"3F6F5A52-B35B-4646-9B91-06127323F152\""
            cursor.execute(sql)
            index = cursor.description
            result = []
            for res in cursor.fetchall():
                row = {}
                for i in range(len(index) - 1):
                    row[index[i][0]] = res[i]
                result.append(row)
            if result:
                self.assertParams(result)
            else:
                self.logger.error("<em style=\"color:red\">" + table + "为空</em>")
            self.logger.info(table + "校验完成")
        conn.commit()
        cursor.close()
        conn.close()

    def test_login(self, appname):

        self.clearUp()

        self.logger.info(("_____" + appname + "___清除完成"))
        self.logger.info(("_____" + appname + "_begin____"))

        desired_caps = {}
        desired_caps['device'] = 'android'
        desired_caps['platformName'] = 'android'
        desired_caps['version'] = '4.4.4'
        desired_caps['deviceName'] = '3100f48828a63400'
        path = os.getcwd()
        desired_caps['app'] = PATH(path + '\\app\\' + appname + '.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.logger.info(("_____启动应用中，请稍后_____"))
        time.sleep(15)
        os.system("adb shell input tap " + self.coo)
        time.sleep(20)
        self.parseData()
        self.assertUa()
        os.remove(os.getcwd() + '\\app\\' + appname + '.apk')
        self.driver.quit()
        return self.getResult()

    def assertUa(self):
        """
        断言ua
        """
        conn = pymysql.connect(host=self.host, port=3306, user=self.user, passwd=self.passwd, db=self.dbname,
                               charset='utf8')
        cursor = conn.cursor()

        sql = "select ua from l_login where deviceid=\"3F6F5A52-B35B-4646-9B91-06127323F152\""
        cursor.execute(sql)
        ua = cursor.fetchall()
        if ua:
            if ua[0][0].startswith("Android"):
                self.logger.info("ua 校验通过")
            else:
                pass
        else:
            self.logger.error("<em style=\"color:red\">" + "ua 校验失败")
        cursor.close()
        conn.close()

    def assertParams(self, result):
        """
        断言字段
        :return:
        """

        for (m, n) in result[0].items():
            if m in self.params:
                try:
                    assert_that(n, is_not(""), m + "字段为空")

                except AssertionError, e:
                    self.logger.error("<em style=\"color:red\">" + e)
                    pass
            # if m =="deviceid":

    def getResult(self):
        """
        获取最新结果
        :return:
        """
        lists = os.listdir(os.getcwd() + "\\log")

        lists.sort(key=lambda fn: os.path.getmtime(os.getcwd() + "\\log" + "\\" + fn))
        file_new = os.path.join(os.getcwd() + "\\log", lists[-1])
        with open(file_new, "r") as f:
            text = f.read()
            type = chardet.detect(text)
            # text1 = text.decode(type["encoding"])
            text2 = "".join(text)
        return text2
