n = int(input("Enter no:"))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    else:
        print(" ", end=" ")
    print(" ")
print("_________________________________")
for i in range(1,n+1):
    print(" * "*i)

