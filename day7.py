#Inverted half pyramid with alphabets

'''n=4

for i in range(0,n+1):
    for j in range(n-i):
        print(chr(65+j),end=" ")
    print()'''

#Rectangle of * (m x n)

'''m=3
n=4

for i in range(0,m):
    for j in range(0,n):
        print("*",end="")
    print()'''

#Right Pascal’s triangle

n=3
#count=1

for i in range(1,n*2):
    if i>n:
        for j in range(0,2*n-i):
            print("*",end=" ")
        #count+=1
        
    else:
        for k in range(0,i):
            print("*",end=" ")
    print()
    