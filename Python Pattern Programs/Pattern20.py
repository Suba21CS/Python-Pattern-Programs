n = int((input("Enter no:")))

for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(" * ",end=" ")
    print()
for i in range(n):
    for j in range(i+2-1):
        print(" ",end=" ")
    for j in range(n-i-1):
        print(" * ",end=" ")
    print()