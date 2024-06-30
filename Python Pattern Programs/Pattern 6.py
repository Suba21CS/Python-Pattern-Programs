n = int(input("Enter no:"))
for i in range(n):
    for j in range(n):
        if i==0 or i+j==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
