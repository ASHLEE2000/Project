import pandas as pd
import usedproduct

class starting:
    
    def print_testing(self):
        df = pd.read_csv("Usedproducts.csv")
        p_h = df['prev_hash']
        id = df['ID']
        hash = df['current_hash']
        pow = df['proof_of_work']
        price = df['block_no']
        date = df['date']
        usedproduct.l1.list1.clear()
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        for i in p_h:
            a.append(str(i))    
        for j in id:
            b.append(str(j))
        for k in price:
            c.append(str(k))
        for l in date:
            d.append(str(l))
        for y in pow:
            e.append(str(y))
        for ze in hash:
            f.append(str(ze))
        
        objs = []
        for m in range(len(a)):
            objs.append(usedproduct(b[m],a[m],d[m],e[m],f[m]))
        
        