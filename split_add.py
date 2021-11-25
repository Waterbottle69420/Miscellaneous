a=int(input())
L=[]
for i in range(a):
    b=int(input())
    L.append(b)

index=int(input())

left=0
right=0

for i in range(index):
    e=int(L[i])
    left=left+e

for i in range(index+1,a):
    f=int(L[i])
    right=right+f

print(index)
print(L[index])
if left==right:
    print(left)
else:
    print("Not equal")
    

    
