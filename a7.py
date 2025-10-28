x0 = int(input())
y0 = int(input())
x1 = int(input())
y1 = int(input())
g0 = (x0+y0)%2 #0-wiht 1-blak
g1 = (x1+y1)%2
if g0 == g1:
    print("YES")
    if g0 == 0:
        print("White")
    else:
        print("Black")
else:
    print("NO")
