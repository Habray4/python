print("x1   y1")
x1 = float(input())
y1 = float(input())
print("x2   y2")
x2 = float(input())
y2 = float(input())

if(x1>0 and y1>0 and x2>0 and y2>0):
    print("Yes, I")
elif(x1<0 and y1>0 and x2<0 and y2>0):
    print("Yes, II")
elif(x1<0 and y1<0 and x2<0 and y2<0):
    print("Yes, III")
elif(x1>0 and y1<0 and x2>0 and y2<0):
    print("Yes, IV")
else:
    print("No")
