import qrcode
import shutil
import os

class QR_co:
    block_no : str
    path_1 : str
    def __init__(self,id,date,name,prev_hash,hash,block_no):
        features = qrcode.QRCode(version=1, box_size=10, border=3)
        url = "http://localhost/8000/verify"
        #url2 = "https://aa9a-106-77-49-40.in.ngrok.io"
        a= (f"url:{url}\n date: {date}\n hash: {hash}\n prev_hash: {prev_hash}\n id: {id}")
        features.add_data(a)
        features.make_image(fit=True)
        b = features.make_image(fill_color = "black", back_color = "white")
        c= ("BLOCK-"+str(block_no)+".jpg")
        b.save(c)
        shutil.move(c, "C:/Users/Ashley/Desktop/BLOCKCHAIN/qrcodesImgs/")
        self.block_no=c


class user_qr:
    def __init__(self,u_n,id,password,key) -> None:
        features = qrcode.QRCode(version=1, box_size=10, border=3)
        a= (f"user name: {u_n}\n ID: {id}\n password: {password}\n key: {key}")
        features.add_data(a)
        features.make_image(fit=True)
        b = features.make_image(fill_color = "black", back_color = "white")
        c= ("USER-"+str(u_n)+key+".jpg")
        b.save(c)
        shutil.move(c, "C:/Users/Ashley/Desktop/BLOCKCHAIN/user_qr/")
        self.block_no=c
        self.path_1= ("C:/Users/Ashley/Desktop/BLOCKCHAIN/user_qr/"+str(c))
    
    def get_path(self):
        return self.path_1