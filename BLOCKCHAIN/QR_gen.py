import qrcode
import shutil
import os

class QR_co:
    block_no : str

    def __init__(self,id,name,prev_hash,hash,block_no):
        features = qrcode.QRCode(version=1, box_size=10, border=3)
        url = "http://localhost/8000/verify"
        url2 = "https://aa9a-106-77-49-40.in.ngrok.io"
        a= (f"url:{url}\nhash: {hash}\nprev_hash: {prev_hash}\nid: {id}")
        features.add_data(a)
        features.make_image(fit=True)
        b = features.make_image(fill_color = "blue", back_color = "black")
        c= ("BLOCK-"+str(block_no)+".jpg")
        b.save(c)
        shutil.move(c, "C:/Users/Ashley/Desktop/BLOCKCHAIN/qrcodesImgs/")
        self.block_no=c


    def get_qr_name(self):
        return self.block_no
