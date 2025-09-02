#Square of *

#test cases 
'''n=4

****
****
****
****'''
'''n=4
print((("*"*n +"\n")*n).rstrip())'''

#code 

'''for i in range(0,4):
    for j in range(0,4):
        print("*",end="")
    print()'''

#using while loop

'''i,j=0,0

while i<4:
    while j<4:
        print("*",end="")
        j+=1
    print()
    i+=1
    j=0'''

#square of numbers (1s, 2s, etc.)

'''n=5
11111
22222
33333
44444
55555'''

'''for i in range(1,6):
    for j in range(1,6):
        print(i,end="")
    print()'''

#using while loop

'''i,j=1,1
while i<6:
    while j<6:
        print(i,end="")
        j+=1
    print()
    i+=1
    j=1'''

#Square of Increasing Numbers

'''n=3
123
123
123'''

'''for i in range(1,4):
    for j in range(1,4):
        print(j,end="")
    print()'''

'''i,j=1,1
while i<4:
    while j<4:
        print(j,end="")
        j+=1
    print()
    j=1
    i+=1'''

#Square of alphabets (A, B, etc.)

'''n=3
ABC
ABC
ABC'''

# a=chr(65)
# print()

'''for i in range(0,3):
    for j in range(65,68):
        print(chr(j),end="")
    print()'''

#Using three for loops

#Simple pyramid of *

'''n=4
   *
  ***
 *****
******* '''

#code
n=6
for i in range(1,n):
    # for j in range(0,n-i):
    #     print(" ",end="")
    print(" " *(n-i),end="")
    for k in range(0,2*i-1):
        print("*",end="")

    print()
