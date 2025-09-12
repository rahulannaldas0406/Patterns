#Right-angled triangle of numbers 

'''n=3
for i in range(0,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

#Right-angled triangle of alphabets

n=3

for i in range(0,n+1):
    for j in range(0,i):
        print(chr(65+j),end=" ")
    print()