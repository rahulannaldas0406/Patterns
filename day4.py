#Inverted right-angled triangle of *

'''n=3
for i in range(1,n+1):
    for j in range(0,n+1-i):
        print("*",end=" ")
    print()'''

#Inverted right-angled triangle of numbers 

n=4

for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(j,end=" ")
    print()