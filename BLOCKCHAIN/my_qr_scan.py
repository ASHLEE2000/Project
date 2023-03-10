import cv2

class d_data:
    hash: str
    prev: str
    date : str
    proof_of_work: str
    id: str
    a:str

    
    def __init__(self) -> None:
        pass
        
    def data(self):
        detector= cv2.QRCodeDetector()
        reval,points,s_qr= detector.detectAndDecode(cv2.imread('name.jpg'))
        return reval

class verif:
    hash: str
    prev: str
    date : str
    proof_of_work: str
    id: str
    a =False

    def __init__(self,hash,prev,date,proof_of_work,id):
        self.hash=("current_hash: "+hash)
        self.prev=("prev_hash: "+prev)
        self.proof_of_work=( "proof of work: "+proof_of_work)
        self.date=("date of manufacturing: "+date)
        self.id=("ID: "+id)
        #print(self.hash,self.prev,self.proof_of_work,self.date,self.id)
        self.find_block()

    def veri(self):
        return self.a

    def find_block(self):
        f = open('chain.txt','r')
        f_content= f.readlines()
        #print(f_content)
        c=False
        d=False
        l=False
        m=False
        n=False
        e=0
        
        for i in f_content:
            e=(e+1)
            if(e>2000):
                print("block not found...")
                break
            else:
                data1 = i.split("\n")
                #print(data2,self.hash)
                for data2 in data1:
                    if(data2==self.hash):
                        l= True
                        print("hash found...")

        e=0
        for i in f_content:
            e=(e+1)
            if(e>2000):
                print("proof of work not found...")
                break
            else:
                data1 = i.split("\n")
                for data2 in data1:
                    if(data2==self.proof_of_work):
                        c= True
                        print("proof of work found...")
        e=0
        for i in f_content:
            e=(e+1)
            if(e>2000):
                print("date not found...")
                break
            else:
                data1 = i.split("\n")
                for data2 in data1:
                    if(data2==self.date):
                        print("date found...")
                        d= True

        e=0
        for i in f_content:
            e=(e+1)
            if(e>2000):
                print("block not found...")
                break
            else:
                data1 = i.split("\n")
                for data2 in data1:
                    if(data2==self.prev):
                        n= True
                        print("previous hash found...")

        e=0
        for i in f_content:
            e=(e+1)
            if(e>2000):
                print("block not found...")
                break
            else:
                data1 = i.split("\n")
                for data2 in data1:
                    if(data2==self.id):
                        m= True
                        print("id found...")

        f.close()
        if(c and d and l and m and n):
            self.a=True


#abc = verif("00002a1ed4e1d1fb4562628271c21ff2e9b18b28f1edd073dcf623d329eda792","0","27-11-2020","817435.0","i5")
#print(abc.a)