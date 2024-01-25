from functionsww import *

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("Lisamine-1\nKustutamine-2\nSuurimPalk-3\nKes saab suurem palka-4\nSort-5\nKes saab saama palka-6\nOtsimine-7\nNimekiri-8\nTop-9\nKeskmine-10\nTulumaks-11\nNimi sorteerimine-12\nKes saab alla keskmiselt-13\nRedigeerimine-14\nPreemia-15\nUus nimi-16\nData Redigeerimine-17\nNimi ja taht ostimine-18\nOma function-19")
    
    v=int(input())

    if v==1:
        k=int(input("Mitu inimest lisame? "))
        inimesed,palgad=Lisamine(inimesed,palgad,k)
        for i in range(len(palgad)):
            print(inimesed[i]," saab kätte",palgad[i])

    elif v==2:
        inimesed,palgad=Kustutamine(inimesed,palgad)
        print(inimesed)
        print(palgad)
    elif v==3:
        maxpalk,nimi=suurimpalk(inimesed,palgad)
        print(nimi,"saab kätte",maxpalk,"Eur")
    
    # elif v == 4:
    #     i = int(input("Kasvab-0, kahaneb-1: "))
    #     inimesed, palgad = Sort(inimesed, palgad, i)
    #     for i in range(len(palgad)):
    #         print(palgad[i], "on", inimesed[i], "-")
 
    elif v==5:
        i=int(input("Kasvab-0,kahaneb-1"))
        inimesed,palgad=Sort(inimesed,palgad,i)
        for i in range(len(palgad)):
            print(palgad[i],"on",inimesed[i],"-")
            

    elif v == 6:
        saamapalktt = saamapalk(dict(zip(inimesed, palgad)))
        print(saamapalktt)



    elif v == 7:
        leiaaaaa = input("Sisestage otsitava nime: ")
        palkad_result = otsipalk(dict(zip(inimesed, palgad)), leiaaaaa)

        print(palkad_result)

# ...

    elif v == 8:
        threshold = int(input("Sisestage lävendi väärtus: "))
        mode = input("Sisestage režiim ('rohkem' või 'natukem'): ")
        filtered_result = filter_palk(dict(zip(inimesed, palgad)), threshold, mode)

        print(filtered_result)



    elif v == 9:
        mitterikkad, rikkad = Top(dict(zip(inimesed, palgad)))
        print(f"Mitterikkaim inimene: {mitterikkad}")
        print(f"Rikkaim inimene: {rikkad}")

    elif v == 10:
        keskmine_palk, inimene = Keskmine(dict(zip(inimesed, palgad)))
        print(f"Keskmine palk: {keskmine_palk}, Inimene: {inimene}")

    elif v == 11:
        maksu_andmed = Tulumaks(inimesed, palgad)
        print("Tulumaksu andmed:")
        for i in range(len(inimesed)):
            print(f"{inimesed[i]}: {maksu_andmed[i]}")

    elif v == 12:
        sorted_names = sortnimi(inimesed)
        print("Nimed tähestikulises järjekorras:")
        for name in sorted_names:
            print(name)
            
    elif v == 13:
        kustutatud_palgad = kustutamine(palgad)
        print("Palgad pärast kustutamist:")
        for i in range(len(kustutatud_palgad)):
            print(inimesed[i], " saab kätte", kustutatud_palgad[i], "Eur")
            
    elif v == 14:
        andmed = formeeri(inimesed + palgad)
        print("Formeeritud andmed:")
        for i in range(0, len(andmed), 2):
            print(andmed[i], " saab kätte", andmed[i + 1], "Eur")
            
    elif v == 15:
        aastat = int(input("Mitu aastat on möödunud? "))
        tetete = input("Kellele soovite preemiat arvutada (jätke tühi, et arvutada kõigile)? ")
        bonusid = preemia(inimesed + palgad, aastat, tetete)

        if tetete and not bonusid:
            print(f"Viga: Nime {tetete} ei leitud.")
        elif tetete:
            print(f"{tetete} preemia pärast {aastat} aastat: {bonusid}Eur")
        else:
            print("Preemiad pärast", aastat, "aastat:")
            for nimi, preemia in bonusid.items():
                print(nimi, "saab preemiat", preemia, "Eur")
                

    elif v == 16:
        updated_data = annanimi(dict(zip(inimesed, palgad)))
        print("Uuendatud andmed:")
        for name, salary in updated_data.items():
            print(f"{name}: {salary}")

    elif v == 17:
        muudetud_andmed = RedigeeriAndmeid(dict(zip(inimesed, palgad)))
        print("Uuendatud andmed:")
        for name, salary in muudetud_andmed:
            print(f"{name}: {salary}")



    elif v == 18:
        LeiaEesnimega(dict(zip(inimesed, palgad)))



    elif v == 19:
        summa = kogupalka(dict(zip(inimesed, palgad)))
        print(f"Kogu palk: {summa}")
