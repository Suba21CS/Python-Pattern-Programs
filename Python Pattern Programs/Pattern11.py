n = input("Enter no:")
length = len(n)
for i in range(length):
    for j in range(length):
        if i==j or i+j==length-1:
            print(n[i],end=" ")
        else:
            print(" ",end=" ")
    print("")

