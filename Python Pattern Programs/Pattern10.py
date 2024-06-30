n = int(input("Enter no:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or i==n-3:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print(" ")