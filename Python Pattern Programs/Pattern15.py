n=int(input("Enter no:"))
size=n*2-1
val=n
min =0
max=size-1
mat=[[0 for i in range(size)] for j in range(size)]
#top
for i in range(n):
    for j in range(min,max+1):
        mat[i][j]=val
 #left
    for j in range(min+1,max+1):
        mat[j][i] =val
#bottom
    for j in range(min+1,max+1):
        mat[max][j] = val
#right
    for j in range(min+1,max):
        mat[j][max]=val


    min+=1
    max-=1
    val-=1
for i in range(size):
    for j in range(size):
        print(mat[i][j],end=" ")
    print(" ")