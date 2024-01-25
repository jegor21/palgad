#1. function
def Lisamine(i:list,p:list,k:int):
    """Andmete lisamine listidesse
    Tagastab listud

    :param list i: Inimeste nimekiri
    :param list p: Palkage loetelu
    :param int k: Inimeste kogus
    :rtype:list, list
    """
    for x in range(k):
        nimi=input("Mis on inimese nimi? ")
        palk=int(input("Kui suur palk tal on? "))
        i.append(nimi)
        p.append(palk)
    return i,p

#2. function
def Kustutamine(i:list,p:list):
    """
    """
    nimi=input("Nimi: ")
    n=i.count(nimi)
    if n>0:
        for x in i:
            if x==nimi:
                ind=i.index(x)
                i.remove(x)
                p.pop(ind)

    return i,p



#3. function
def suurimpalk(i:list,p:list):
    """
    """
    nimi_list=[]
    max_=max(p)
    
    #kogus=p.count(max_)
    a=0
    for palk in p:
        ind=p.index(max_,a)
        nimi=i[ind]
        a+=1
        nimi_list.append(nimi)
    return max_,nimi_list



#4. function
def Sort(i:list,p:list,a:int):
    """
    """
    N=len(i)
    if a==1:
        for n in range(0,N):
            for m in range(n,N+1):
                if p[n]<p[m]:
                    kaust=p[n]
                    p[n]=p[m]
                    p[m]=kaust
                    kaust=i[n]
                    i[n]=i[m]
                    i[m]=kaust
    else:
         for n in range(0,N):
            for m in range(n,N+1):
                if p[n]>p[m]:
                    kaust=p[n]
                    p[n]=p[m]
                    p[m]=kaust
                    kaust=i[n]
                    i[n]=i[m]
                    i[m]=kaust
    return i,p

#5. function
def palkasort(data, order='asc'):
    
    sorteerimine = sorted(data.items(), key = lambda x: x[1], reverse=(order == 'desc'))
    return sorteerimine




#6. function
def saamapalk(data):
    
    palkami = {}
    
    for name, palk in data.items():
        
        if palk in palkami:
            
            palkami[palk].append(name)
        else:
            palkami[palk] = [name]

    for palk, names in palkami.items():
        if len(names) > 1:
            print(f"Inimesed palkaga {palk}: {', '.join(names)}")
    return saamapalk





#7. function
def otsipalk(data, search_name):
   
    palkad = [palk for name, palk in data.items() if name == search_name]
    return palkad






#8. function
def filter_palk(data, threshold, mode='parem'):
    
    filtreerituddata = [(name, palk) for name, palk in data.items() if (mode == 'rohkem' and palk > threshold) or (mode == 'natukem' and palk < threshold)]

    if filtreerituddata:
        print(f"Inimesed palkaga {mode} kui {threshold}:")
        for name, palk in filtreerituddata:
            print(f"{name}: {palk}")
    else:
        print(f"Ei ole inimesed palkaga {mode} kui {threshold}.")
    return filter_palk



#9. function


def Top(data):
    
    if not data:
        return None, None

    sorted_data = sorted(data.items(), key=lambda x: x[1])
    mitterikkad = sorted_data[0][0]
    rikkad = sorted_data[-1][0]

    return mitterikkad, rikkad




#10. function


def Keskmine(data):
    
    if not data:
        return None, None

    keskminepalk = sum(data.values()) / len(data)
    
    ppalk = min(data.values(), key=lambda x: abs(x - keskminepalk))
    inimenepalka = [name for name, palk in data.items() if palk == ppalk][0]

    return keskminepalk, inimenepalka




#11. function


def Tulumaks(data):
   
    maksu = {name: palk * 0.8 for name, palk in data.items()}
    return maksu



#12. function


def sortnimi(data, order='asc'):
    
    sorted_data = dict(sorted(data.items(), key=lambda x: x[0], reverse=(order == 'desc')))
    return sorted_data




#13. function


def kustutamine(data):

    if not data:
        return []

    keskminepalk = sum(data) / len(data)
    filtered_data = [palk for palk in data if palk < keskminepalk]

    return filtered_data


#14. function


def formeeri(data):
    
    formeritud = []

    for i in range(0, len(data), 2):
        nimi = data[i].capitalize()
        palk = int(data[i + 1])
        formeritud.extend([nimi, palk])

    return formeritud



#15. function


def preemia(data, aastat, tootj=None):

    if not data:
        return {}

    if tootj:
        index = data.index(tootj)
        palk = int(data[index + 1])
        aastatedasi = int(palk * (1.05 ** aastat))
        return aastatedasi
    else:
        bonusid = {}

        for i in range(0, len(data), 2):
            nimi = data[i]
            palk = int(data[i + 1])
            aastatedasi = int(palk * (1.05 ** aastat))
            bonusid[nimi] = aastatedasi

        return bonusid



#16. function


def annanimi(data):
   
    if not data:
        return {}

    updatet = data.copy()
    uusnimi = list(data.keys())[2::3]

    for old_name in uusnimi:
        new_name = input(f"Pange uus nimi {old_name}: ").capitalize()
        updatet[new_name] = updatet.pop(old_name)

    return updatet




#17. function


def RedigeeriAndmeid(andmed):
    if not andmed:
        return []

    muudetud_andmed = []
    
    while True:
        print("\nValige, mida soovite redigeerida:")
        print("1. Nimi")
        print("2. Palk")
        print("3. Redigeerimine l?petatud")

        valik = input("Sisestage valiku number (1, 2 v?i 3): ")

        if valik == '1':
            vana_nimi = input("Sisestage vana nimi redigeerimiseks: ")
            uus_nimi = input("Sisestage uus nimi: ").capitalize()
            if vana_nimi in andmed:
                andmed[uus_nimi] = andmed.pop(vana_nimi)
                print(f"Nimi edukalt muudetud: {vana_nimi} -> {uus_nimi}")
            else:
                print(f"Viga: Nime {vana_nimi} ei leitud.")
        elif valik == '2':
            nimi = input("Sisestage inimese nimi, kelle palga soovite muuta: ")
            if nimi in andmed:
                uus_palk = input(f"Sisestage uus palk {nimi} jaoks: ")
                try:
                    andmed[nimi] = int(uus_palk)
                    print(f"Palk edukalt muudetud {nimi} jaoks: {uus_palk}")
                except ValueError:
                    print("Viga: Sisestage palga jaoks korrektne number.")
            else:
                print(f"Viga: Nime {nimi} ei leitud.")
        elif valik == '3':
            break
        else:
            print("Viga: Sisestage ?ige valiku number.")

    muudetud_andmed = list(andmed.items())
    return muudetud_andmed




#18. function


def LeiaEesnimega(data):
    
    if not data:
        print("Andmed puuduvad.")
        return

    taht = input("Sisestage otsitava tahe algust?ht: ").capitalize()
    sobivad_nimed = [nimi for nimi in data.keys() if nimi.startswith(taht)]

    if not sobivad_nimed:
        print(f"Nimesid, mis algavad t?hega '{taht}', ei leitud.")
    else:
        print("\nNimed ja vastavad palgad:")
        for nimi in sobivad_nimed:
            print(f"{nimi}: {data[nimi]}")




#19. function


def kogupalka(data):
    
    if not data:
        return 0

    return sum(data.values())


