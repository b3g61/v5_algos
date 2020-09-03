n = int(input("Enter the length of the sequence: ")) # Do not change this line

l = [1,2,3]
for x in range(0,n):
    if x < 3:
        print(l[x], end=" ")
    else:
        a = sum(l)
        l = l[1:] + [a]
        print(a, end=" ")