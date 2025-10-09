#Same alphabet per row

n=5

'''A
B B
C C C
D D D D
E E E E E'''


'''for i in range(0,n):
    for j in range(0,i+1):
        print(chr(65+i),end=" ")
    print()'''

#Same alphabet per column

#n=4
#m=4

'''
A B C D
A B C D
A B C D
A B C D
'''

'''for i in range(0,n):
    for j in range(0,m):
        print(chr(65+j),end=" ")
    print()'''

#Floyd’s triangle in pyramid form

n=4

'''
      1
    2 3
  4 5 6
7 8 9 10
'''

j=1
for i in range(1,n+1):
    for k in range(0,n-i+1):
        print(" ",end=" ")
    c=1
    while c<=i:
        print(j,end=" ")
        c+=1
        j+=1
    
    print()