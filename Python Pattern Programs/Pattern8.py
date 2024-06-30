
for i in range(7):
    for j in range(5):
      if (i==0 or i==6 or i==3) or (j==0 and i<4) or (j==4 and i>2):
          print("*",end=" ")
      else:
            print(" ",end=" ")
    print(" ")

