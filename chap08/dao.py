import pymysql
from vo import User
class UserDAO:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='wl112454', db='mydb', charset='utf8')
        
    def show_users(self):
        sql = "SELECT * FROM user"
        userlist = []
        with self.conn.cursor() as curs:
            curs.execute(sql)
            rows =  curs.fetchall()
            for (num,name,phone,email) in rows:
                userlist.append(User(num,name,phone,email))
        #Connection 닫기
        self.conn.close()
        return userlist
    
    def add_user(self,user):
        sql = "INSERT INTO user VALUES(null,%s,%s,%s)"
        add = False 
        with self.conn.cursor() as curs:
            n = curs.execute(sql,(user.name, user.phone, user.email))
            if n == 1:
                self.conn.commit()
                add = True
        self.conn.close()
        return add
    
    def find_by_num(self, num):
        sql = 'SELECT * FROM user WHERE num=%s'
        user = None
        with self.conn.cursor() as curs:
            curs.execute(sql, num)
            rows = curs.fetchall()
            num,name,phone,email = rows[0]
            user = User(num,name,phone,email)
        self.conn.close()
        return user
    
    def find_by_name(self, name):
        sql = 'SELECT * FROM user WHERE name=%s'
        user = None
        with self.conn.cursor() as curs:
            curs.execute(sql, name)
            rows = curs.fetchall()
            num,name,phone,email = rows[0]
            user = User(num,name,phone,email)
        self.conn.close()
        return user
        
    def update_user(self, num, phone, email):
        sql = "UPDATE user SET phone = %s ,email = %s  WHERE num = %s"
        updated = False
        with self.conn.cursor() as curs:
            n = curs.execute(sql,(phone,email,num))
            if n == 1:
                self.conn.commit()
                updated = True
        self.conn.close()                
        return updated
    
    def delete_user(self,num):
        deleted = False
        sql = "DELETE FROM user WHERE num = %s"
        with self.conn.cursor() as curs:
            n = curs.execute(sql,num)
            if n == 1:
                self.conn.commit()
                deleted = True
        self.conn.close()
        return deleted
        
    
    
    
    
    
    
    
    
    