l=[]
tokens=eval(input())
for i in tokens:
        if(i=='+' or i=='-' or i=='*' or i=='/'):
            a=l.pop(-1)
            b=l.pop(-1)
            g=b+i+a
            w=eval(g)
            e=int(w)
            l.append(str(e))
        else:
            l.append(i)
print(int(l[0]))
