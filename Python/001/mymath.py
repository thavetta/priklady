import math

def nsdPrvni(a,b):
    assert (a > 0 and b > 0 and 
        type(a) == int and 
        type(b) == int),'Obě čísla pro NSD musí být alespoň 1'
        
    while a != b:
        if (a > b):
            a -= b
        else:
            b -= a
        if (a == 1 or b == 1):
            a = b = 1
            break

    return a

# Euklidův algoritmus využívající výpočet zbytku při dělení        
def nsd(a,b):
    assert (a > 0 and b > 0 and 
        type(a) == int and 
        type(b) == int),'Obě čísla pro NSD musí být alespoň 1'

    while True:
        zbytek = a % b
        if zbytek == 0:
            break
        a = b
        b = zbytek

    return b


def nsn(a,b):
    assert (a > 0 and b > 0 and 
        type(a) == int and 
        type(b) == int),'Obě čísla pro NSN musí být alespoň 1'

    return a*b // nsd(a,b)

def faktorial(n):
    assert (n > 0 and 
        type(n) == int), 'n musí být kladné celé číslo větší než nula'

    if n == 1:
        return 1
    
    return n * faktorial(n - 1)

def jePrvocislo(n):
    assert (n > 1 and 
        type(n) == int), 'n musí být kladné celé číslo větší než jedna'
# Dvojka je jediné sudé prvočíslo a proto je potřeba ho extra otestovat
    if n == 2:
        return True

# Pomocí bitového end testuji nultý bit, který je u všech sudých čísel nula    
    if (n & 1) == 0:
        return False
    
# Číslo n je liché a budeme ho zkoušet dělit všemi lichými čísly až do odmocniny z n    
    limit = int(math.sqrt(n)) + 1

    for delitel in range(3,limit,2):
        if (n % delitel) == 0:
            return False
# Žádného dělitele jsme nenašli, tak je číslo prvočíslo    
    return True

# Tato funkce využívá k nalezení prvočísel algoritmus Eratostenovo sito
def vratPrvocisla(max):
    assert (max > 1 and 
        type(max) == int), 'max musí být kladné celé číslo větší než jedna'

# posun o 1 bit je identický s celočíselnou operací dělení dvěma
# tento algoritmus pracuje pouze s lichými čísly, sudé rovnou vyřadí
# využívá princip, že index i odpovídá číslu i*2 + 1 (tedy 1 => 3, 2=> 5, 3 => 7, atd.)
    konec = max >> 1
# False odpovídá v algoritmu neškrtnutou položku
    data = [False]*konec
# rovnou vyřadíme index 0 odpovídající 1, protože 1 není prvočíslo
    data[0] = True
    
# škrtat stačí do odmocniny z cílové hodnoty, opět dělíme dvojkou, abychom našli správný index pro odpovídající liché číslo
# a pro jistotu přičteme 1, ať neztratíme nic zaokrouhlením
    limit = (math.isqrt(max) >> 1) + 1

    for cislo in range(1,limit):
        # škrtnuté číslo můžeme ignorovat
        if data[cislo]:
            continue
        # pro neškrtnuté potřebujeme určit odpovídající krok
        krok = cislo * 2 + 1

        # tento cyklus proškrtá násobky objeveného prvočísla
        for cistim in range(cislo + krok,konec,krok):
            data[cistim] = True
    
    # připravíme si výsledek, do kterého rovnou vložíme první prvočíslo
    vysledek = [2]

    # přidáme postupně všechna neškrtnutá prvočísla
    for index in range(1,konec):
        if not data[index]:
            vysledek.append(index * 2 + 1)
    
    return vysledek



