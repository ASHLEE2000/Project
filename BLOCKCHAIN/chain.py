import hashlib
import QR_gen

class block:

    block_no = 0
    ID : str
    name : str
    price : float
    prev_hash : str
    current_hash : str 


    def __init__(self,ID, name,price) -> None:
        self.ID = ID
        self.name = name
        self.price = price
        self.cal_block_no()
        self.prev_Hash()
        self.cal_hash()
        l1.add_block(self)
        QR_gen.QR_co(self.ID,self.name,self.prev_hash,self.current_hash,self.block_no)
        

    def cal_block_no(self):
        if(len(l1.list1)==0):
            self.block_no= 0
        else:
            self.block_no= len(l1.list1)

    
    def prev_Hash(self):
        a = (self.block_no -1)
        if (a<=0):
            self.prev_hash = "0"
        else:
            prev_block = l1.find_prev_hash(l1, self.block_no)
            self.prev_hash = prev_block.current_hash 

    def cal_hash(self):
        self.current_hash = len(self.ID)**2 +len(self.name)**3 + ((self.price/40)**3) 
        hashlib.sha256(str(self.current_hash).encode()).hexdigest()

    
class list_of_blocks:
    list1 = []

    def add_block(b = block):
        l1.list1.append(b)
        print(block.block_no)
        file = open('chain.txt','w')
        for i in l1.list1:
            file.write("**************************-block ")
            file.write(str((i.block_no)+1))
            file.write("-*************************\n")
            file.write("ID: ")
            file.write(str(i.ID))
            file.write("\n")
            file.write("name: ")
            file.write(str(i.name))
            file.write("\n")
            file.write("price: ")
            file.write(str(i.price))
            file.write("\n")
            file.write("prev_hash: ")
            file.write( str(i.prev_hash))
            file.write("\n")
            file.write("current_hash: ")
            file.write(str(i.current_hash))
            file.write("\n ")
            file.write("************************************************************\n\n")
        file.close()
    
    def find_prev_hash(self,block_no):
        a = (block_no-1)
        return self.list1[a]
    



l1 = list_of_blocks

#b1 = block("1135g7","is", 8000)
#b2 = block("a2","name2", 40)
#print(b1.block_no)
#print(b1.prev_hash)
#print(b1.current_hash)
#print(l1.list1[0].block_no)
#print(b1.cal_hash())