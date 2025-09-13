#Right-angled triangle of numbers 

'''n=3
for i in range(0,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

#Right-angled triangle of alphabets

'''n=3

for i in range(0,n+1):
    for j in range(0,i):
        print(chr(65+j),end=" ")
    print()'''

#Diamond of *

n = 4

for i in range(1, 2*n):              # single loop controls both halves
    if i <= n:
        stars = 2*i - 1              # increasing stars
        spaces = n - i
    else:
        stars = 2*(2*n - i) - 1      # decreasing stars
        spaces = i - n

    for j in range(spaces):          # 1st loop → spaces
        print(" ", end=" ")
    for k in range(stars):           # 2nd loop → stars
        print("*", end=" ")
    print()                          # 3rd loop → new line
