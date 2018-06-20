import  pymysql


class Analyze_api(object):



    def queryforgroup(self,app_key):
        self.host = "172.24.133.135"
        self.port = 3301
        self.user = "user_qa"
        self.password = "user_qa@test007"
        self.db = "prepub_mysql_cloud_atlas_master"
        conn= pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password,
                                        db=self.db, charset='utf8')
        cur=conn.cursor()
        code="SELECT app_group FROM sys_app_group_db WHERE app_key="+"\""+app_key+"\""
        i=cur.execute(code)
        b= cur.fetchone()
        if b==None :
            return ([3])
        else:
            return (b)
