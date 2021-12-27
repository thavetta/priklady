import mymath as m 

# Pomocné funkce pro otestování napsaných funkcí
def VypisPrvocisel():
    max = int(input('Zadej max pro prvočísla: '))
    vysledek = m.vratPrvocisla(max)
    m.VypisCisel(vysledek)


def TestNSD():
    a = int(input('Zadejte číslo a: '))
    b = int(input('Zadejte číslo b: '))

    nsd = m.nsd(a,b)
    nsn = m.nsn(a,b)
    # ukázka různých způsobů výpisu
    print('NSD(',a,',',b,')=',nsd,sep='')
    print(f'NSN({a},{b})={nsn}')

def TestPrvocisla():
    x = int(input('Zadejte číslo pro test prvočísla: '))

    prvocislo = m.jePrvocislo(x)

    if prvocislo:
        print("Číslo",x,"je prvočíslo!")
    else:
        print("Číslo",x,"není prvočíslo!")
    return

# Kód programu, tady to začne
while True:
    print('Vyber jednu z voleb a stiskni Enter')
    print('\ta - Výpis prvočísel do X')
    print('\tb - Test zda je číslo prvočíslo')
    print('\tc - Výpočet NSD a NSN')
    print('\tq - Konec')
    
    znak = input()
    # Jazyk Python nezná příkaz switch, proto se používá zřetězení příkazů if pomocí elif
    if znak == 'q':
        quit()
    elif znak == 'a':
        VypisPrvocisel()
    elif znak == 'b':
        TestPrvocisla()
    elif znak == 'c':
        TestNSD()
    else:
        print('Neznámý pokyn')
    