n = int(input("Enter no:"))
for i in range(n):
    for  j in range(n):
        if  (i%2==1 and j%2==1) or (i%2==0 and j%2==0):
            print(1,end=" ")
        else:
            print(0,end=" ")
    print(" ")