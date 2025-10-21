import string

p = input()
nad = 1
ss = '*-#'

if(len(p)<8):
    print("Длина Меньше 8")
    nad = 0;

buf = p.lower()
if(p==buf):
    print("Нет Заглавных Букв")
    nad = 0;

buf = p.upper()
if(p==buf):
    print("Нет Строчных Букв")
    nad = 0;

if(not (any(symbol.isdigit() for symbol in p))):
    print("Нет Цифор")
    nad = 0;

buf = 0
for i in p:
    for j in ss:
        if(i==j):
            buf = 1
if(buf==0):
    print("Нет Специальных Символов")
    nad = 0;

ss = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
buf = 1
for i in p:
    buf2 = 0
    for j in ss:
        if(i==j):
            buf2 = 1
    if(buf2==0):
        buf = 0
if(buf==0):
    print("Используется Недопустимые Символы")
    nad = 0

if(nad==1):
    print("Надёжный Пароль")
