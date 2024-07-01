n = (input("Enter no:"))
length =len(n)
for i in range(length):
    for j in range(length):
        if i==0 or j==0 or i==length//2 :
            print(n[i],end=" ")
        else:
            print(" ",end=" ")
    print(" ")
