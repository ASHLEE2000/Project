import pandas as pd
import chain

class starting:
    
    def print_testing(self):
        df = pd.read_csv("products.csv")
        name = df['name']
        id = df['ID']
        price = df['price']
        date = df['date']
        chain.l1.list1.clear()
        a=[]
        b=[]
        c=[]
        d=[]
        print(name)
        for i in name:
            a.append(i)    
        for j in id:
            b.append(j)
        for k in price:
            c.append(k)
        for l in date:
            d.append(str(l))
        
        objs = []
        for m in range(len(a)):
            objs.append(chain.block(a[m],b[m],c[m],d[m]))
        
        