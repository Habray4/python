n = int(input())
h = n//3600
n = n % 3600
m = n//60
s = n%60
print(h, end="")
print(":", end="")
if m < 10:
    print("0", end="")
print(m, end="")
print(":", end="")
if s < 10:
    print("0", end="")
print(s)
