lu = int(input())
pu = int(input())
u = pu - lu
if(u < 0):
    u = u + 10000
m = 21
h = u
if(h>800):
    m = m + ((h-800) * 0.025)
    h = 800
if(h>600):
    m = m + ((h-600) * 0.04)
    h = 600
if(h>300):
    m = m + ((h-300) * 0.06)
    
print("Предыдущее")
print("  ", lu)

print("Текущее")
print("  ", pu)

print("Использовано")
print("  ", u)

print("К оплате")
print("  ", round(m, 2))

print("Ср. цена за m^3")
print("  ", round(m/u, 2))
