def func(N):
    startnum=[1,11,21,31,6]
    for start in startnum:
        s=list(range(start,start+N))
        print(" ".join(f"{num:2}" for num in s))
N = int(input("Enter no:"))
func(N)