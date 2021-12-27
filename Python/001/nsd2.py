a = int(input('Zadejte číslo a:'))
b = int(input('Zadejte číslo b:'))

if (a < 1 or b < 1):
    print('Obě čísla pro NSD musí být alespoň 1')
    quit()

while a != b:
    if (a > b):
        a -= b
    else:
        b -= a
    if (a == 1 or b == 1):
        a = b = 1
        break

print(a)