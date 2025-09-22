#Hollow triangle

'''n=6

for i in range(0,n):
    for j in range(1,2*n):
        if j==n-i or j==n+i or i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
        
    print()'''

#Floyd’s triangle (1,2,3,4…)

n=4

num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()
'''temp=1
count1=0
for i in range(1,n+1):
    for j in range(temp,n*4):
        print(j,end=" ")
        count1+=1
        if i==count1:
            count1=0
            temp=j+1
            break
    print()'''

