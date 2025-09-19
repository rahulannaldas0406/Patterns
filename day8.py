#Hollow rectangle of *

'''m=4
n=5

for i in range(0,m):
    for j in range(0,n):
        if i==0 or i==m-1:
            print("*",end=" ")
        elif j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    
    print()'''

#Hollow square *



n=4

for i in range(0,n):
    for j in range(0,n):
        if i==0 or i==n-1:
            print("*",end=" ")
        elif j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    
    print()












#Left Pascal’s triangle

'''n=4

for i in range(1,2*n):
    if i<n:
        for j in range(0,n):
            if j==n-i:
                print(" ",end=" ")
            else:
                print("*",end=" ")
    else:
        for k in range(0,n):
            if k==i-n:
                print(" ",end=" ")
            else:
                print("*",end=" ")
    print()'''
            