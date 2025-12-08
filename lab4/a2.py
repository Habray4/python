print('size n & m')
n0 = int(input())
m0 = int(input())
print()

print('ПРЯМОУГОЛЬНИК ' + str(n0) + 'x' + str(m0) + ':')
n = n0
while n > 0:
    m = m0
    while m > 0:
        print('#', end='')
        m = m-1
    print()
    n = n-1
print()

print('ПРАВЕЛЬНЫЙ ТРЕУГОЛЬНИК ' + str(n0) + 'x' + str(n0) + ':')
n = 1
while n <= n0:
    m = n
    while m > 0:
        print('#', end='')
        m = m-1
    print()
    n = n+1
print()

print('РАМКА ' + str(n0) + 'x' + str(m0) + ':')
if n0 >= 2 and m0 >= 2:
    m = m0
    while m > 0:
        print('#', end='')
        m = m-1
    print()
    n = n0-2
    while n > 0:
        print('#', end='')
        m = m0-2
        while m > 0:
            print(' ', end='')
            m = m-1
        print('#')
        n = n-1
    m = m0
    while m > 0:
        print('#', end='')
        m = m-1
    print()
        
elif n0 == 0 or m0 == 0:
    n = n0
elif n0 == 1:
    m = m0
    while m > 0:
        print('#', end='')
        m = m-1
    print()
elif m0 == 1:
    n = n0
    while n > 0:
        print('#')
        n = n-1
print()










