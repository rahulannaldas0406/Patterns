#Two for loop

#Right-angled triangle of *
'''for i in range(0,5):
    for j in range(0,i):
        print("*",end="")
    print()'''

#using while loop 

'''i=0
j=0
while i<5:
    #j=i
    while j<=i:
        print("*",end="")
        j+=1
    print()   
    i+=1
    j=0'''

#Right-angled triangle of numbers

'''for i in range(1,4):
    for j in range(1,i+1):
        print(j,end="")
    print()'''

#using while loop

'''i=1
j=1
while i<=4:
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1
    j=1'''

#Right-angled triangle of alphabets

'''for i in range(0,4):
    for j in range(0,i):
        print(chr(65+j),end="")
    print()'''

#using while loop

'''i=0
j=0
while i<=4:
    while j<=i:
        print(chr(65+j),end="")
        j+=1
    print()
    i+=1
    j=0'''

#Three for loop 


n=5
for i in range(n,0,-1):
    for k in range(0,n-i):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    
    
    print()




