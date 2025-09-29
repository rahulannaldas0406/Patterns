#Pyramid of numbers (centered)
#three for loops

'''n=5


for i in range(1,n+1):
    for k in range(0,n-i):
        print(" ",end="")

    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

#Continuous numbers in columns

n=3
i=1
res=1
while i<=n:
    j=1
    while j<=n:
        if j==1:
            print(i,end=" ")
        else:
            res=res+n
            print(res,end=" ")
        j+=1
    print()
        
    i+=1
    res=i


    