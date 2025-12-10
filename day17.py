#Palindrome number pyramid

'''n=3

1
121
12321'''

# 1) start where to number 1 stop where to end using row Index
# 2) 

n = 3

for i in range(1, n + 1):
    # Increasing part: 1 to i
    for j in range(1, i + 1):
        print(j, end="")
        
    # Decreasing part: i-1 to 1
    for j in range(i - 1, 0, -1):
        print(j, end="")
        
    print()


#Continuous numbers pyramid


'''n=5
count=0
for i in range(1,n+1):
    for j in range(i):
        count+=1
        print(count,end=" ")
        
    print()'''


