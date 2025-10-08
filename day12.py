#Alternating 0 and 1 in rows

#n=6

'''
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
'''

'''for i in range(0,n):
    for j in range(0,n):
        if j%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()'''


'''for i in range(0,n):
    val=1
    for j in range(0,n):
        print(val,end=" ")
        val=1-val  #bit manipulation technique
    print()'''

# Alternating 0 and 1 in columns

'''
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1
'''

'''m=4
for i in range(0,n):
    if i%2==0:
        val=0
    else:
        val=1
    for j in range(0,m):
        print(val,end=" ")
        val=1-val
    

    print()'''

#Diamond of numbers

n=6

'''
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
'''

for i in range(1,n*2):
    if i<=n:
        for s in range(0,n-i):
            print(" ",end="")
        for j in range(1,i+1):
            print(j,end=" ")
    else:
        for s in range(0,i-n):
            print(" ",end="")
        for j in range(1,n*2-i+1):
            print(j,end=" ")

    print()
    
