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
#6. function
#7. function
#8. function
#9. function
#10. function
#11. function
#12. function
#13. function
#14. function
#15. function
#16. function
#17. function
#18. function
#19. function







