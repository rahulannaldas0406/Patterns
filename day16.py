#Alternating 0 and 1 in rows
'''0101
   1010
   0101
   1010'''

n=4

'''for i in range(0,n):
    for j in range(0,n):
        if i%2==0:
            even=1
            odd=0
            if j%2==0:
                print(even,end="")
            else:
                print(odd,end="")
        else:
            even=0
            odd=1
            if j%2==0:
                print(even,end="")
            else:
                print(odd,end="")
    print()'''

'''n = 4

for i in range(n):
    for j in range(n):
        print((i + j+1) % 2, end="")  #i=0 j=0 %2 
    print()'''

#Continuous alphabets in rows

'''n=3
count=0
for i in range(n):
    for j in range(n):
        print(chr(65+count),end="")
        count+=1
        
    print()'''

