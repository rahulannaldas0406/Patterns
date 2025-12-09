#Reverse alphabets row-wise

'''n=3
A
C B
F E D
'''

# n=3

# a,b,c=str(input("enter three words").split())

# for i in range(0,3):
#     for j in range(len(i))

def reverse_alphabets_rowwise(n):
    for i in range(n):
        # Build the alphabet row
        row = ""
        for j in range(n):
            row += chr(65 + j)   # A, B, C, ...

        # Reverse every even row (i starts from 0)
        if i % 2 == 1:
            print(row[::-1])
        else:
            print(row)


# Test
reverse_alphabets_rowwise(5)
 
annaldas rahul 
manasa
lovers


