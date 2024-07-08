def myfunc(s):
    n=len(s)
    for i in range(n):
        rotated=s[i:]+s[:i]
        print(rotated)
n= input(" ")
myfunc(n)

