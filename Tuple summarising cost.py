n=int(input())
L=[]
for i in range (n-1):
    for k in range(n-1):
        i1=int(input())
        l=[]
        sum1=0
        c=input()
        l.append(c)
        for j in range(i1-1):
            a=input()
            if a.isdigit()==True:
                sum1=sum1+int(a)
                continue
            if a.isalpha()==True:
                continue
        
        l.append(sum1)
        l=tuple(l)
        L.append(l)

T=tuple(L)    
print(T)
