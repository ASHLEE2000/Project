import QR_gen
import connecting_to_mongo
import secrets
import pandas as pd


class users:
    user_name: str
    pass_word : str
    id: int
    key2= str

    def __init__(self,username:str,password:str, key:str):
        if(True):
            self.user_name=username
            self.pass_word= password
            self.key2 = secrets.token_hex(6)
            u.add_user(self)
            self.id=users.user_ID()
            QR_gen.user_qr(username,password,self.id,self.key2)
            connecting_to_mongo.enter_user_to_mongo(username,password,self.id,self.key2)
            QR_gen.U_csv.print_to_file(QR_gen.U_csv)

    def get_key2(self):
        return self.key2
        
        
    def user_ID():
        return (u.id)

class list_of_users:

    user = []
    id = len(user)
    
    def add_user(user=users):
        u.user.append(user)
        file = open('users.txt','w')
        j= 0
        for i in u.user:
            j=(j+1)
            file.write("user id:")
            file.write(str(j))
            file.write("\n")
            file.write("user name:")
            file.write(i.user_name)
            file.write("\n")
            file.write("password:")
            file.write(i.pass_word)
            file.write("\n")
            file.write("secret key 2:")
            file.write(i.key2)
            file.write("\n")
        file.close()

    def verify_user(id,user_name,password,key):
        
        df2 = pd.read_csv("users.csv")
        name = df2['user_name']
        pwd = df2['password']
        key_s = df2['key']
        c=False
        d=False
        l=False
        
        for Val1 in name:
            if(Val1==user_name):
                c=True
        for Val2 in pwd:
            if(str(Val2)==str(password)):
                l=True
        for Val3 in key_s:
            if(Val3==key):
                d=True
        print(c)
        print(l)
        print(d)
        if(c and d and l):
            return True
        else:
            False


u = list_of_users
#u1 = users("ASH","1234","ff5877")
#u.verify_user(1,"ASH","1234")
