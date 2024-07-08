n=int(input("Enter no:"))
list =[]
for i in range(n):
    temp_list=[]
    for j in range(i+1):
        if j==0 or j==i:
            temp_list.append(1)
        else:
            temp_list.append(list[i-1][j-1]+list[i-1][j])
    list.append(temp_list)
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(list[i][j],end="   ")
    print(" ")
