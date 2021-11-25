n=int(input())
a={}
d={}
for i in range(n):
    g=input()
    g=g.split(" ")
    print(g)

    d={str(g[0]):[str(g[1]),str(g[2])]}
    print(d)
    a.update(d)
print(a)

