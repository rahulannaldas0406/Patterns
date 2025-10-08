#Hollow number pyramid

n=5

'''
    1
   1 2
  1   3
 1     4
1       5
'''


'''for i in range(1,n+1):
    # for k in range(1,2):
    #     print(s,end=" ")
    # for s in range()
    for s in range(0,n-i):
            print(" ",end="")

    for j in range(1,n+1):
        if i==j or j==1:
            print(j,end="")
        if i!=j or j!=1:
            print(" ",end=" ")
            
    print()'''
#Checkerboard (chessboard) of 0 and 1

'''
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
'''

'''for i in range(0,n):
    if i%2==0:
        val=0
    else:
        val=1
    for j in range(0,n):
        print(val,end=" ")
        val=1-val
    

    print()'''

#Continuous alphabets in rows

n=3
i=1
res=1
while i<=n:
    j=1
    while j<=n:
        if j==1:
            print(chr(64+i),end=" ")
        else:
            res=res+n
            print(chr(64+res),end=" ")
        j+=1
    print()
        
    i+=1
    res=i