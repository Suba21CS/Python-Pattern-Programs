n = int(input("Enter no:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==n-3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(" ")