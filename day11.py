#Inverted pyramid of numbers

#n=5

'''
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
'''

'''for i in range(0,n):
    for k in range(0,i):
        print(" ",end="")
    for j in range(1,n+1-i):
        print(j,end=" ")

    print()'''

#Increasing numbers row-wise
#n=5
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
'''for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

#Decreasing numbers row-wise
n=5
'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

for i in range(0,n):
    for j in range(1,n-i+1):
        print(j,end=" ")
    print()