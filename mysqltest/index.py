import pymssql


class MSSQL:
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise(NameError, "没有设置相关数据库信息")
        self.conn = pymssql.connect(
                    host =self.host,
                    user =self.user,
                    password = self.pwd,
                    database = self.db,
                    charset ='utf-8')
        cur = self.conn.cursor()
        if not cur:
            raise(NameError, "链接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)

        reslist = cur.fetchall()
        self.conn.close()
        return reslist


ms = MSSQL(host='local', user='sa', pwd='P@ssw0rd', db='PythonTestDb')
reslist = ms.ExecQuery("select * from Config")
for i in reslist:
    print(i)