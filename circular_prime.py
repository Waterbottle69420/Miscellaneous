num=int(input())
y=str(num)
v=len(y)
i=1
count=0
cprime=0
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1

if count==2:
    cprime=cprime+1

e=str(num)
d=len(e)
r=0
while r<d-1:
                j=1
                count=0
                n=0
                a=0
                b=1
                while num>0:
                        a=int(num%10)
                        num=int(num/10)
                        if num>0:
                                n=n+a*b
                        b=b*10
                num=n*10+a
                
                while j<=num:
                        if num%j==0:
                            count=count+1
                        j=j+1

                if count==2:
                        cprime=cprime+1
                r=r+1

if cprime==v:
        print("CIRCULAR PRIME")
else:
        print("NOT A CIRCULAR PRIME")
