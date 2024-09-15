res=[]

def y():
    j=int(input("Digite valor:"))
    
    res.append(j)
    
    if(j==0):
        pass
    else:
        y()

y()
res.remove(0)
print(res)
input()