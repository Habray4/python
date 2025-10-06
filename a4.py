a = int(input())
b = int(input())
r = a - b
m = (r >> 31) & 1 #bit
print(a-(m*r))
