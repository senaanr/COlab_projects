def kimlikNo(veri):
    veri = str(veri)
    tümToplam=0
    kosulTüm=0
    tekToplam=0
    ciftToplam=0
    kosulTekCift=0
    kosulTek=0

    
    if veri[0] == "0":
        return False
    
    if not len(veri) == 11:
        return False

    if len(veri)==11:

        for i in range(0,10):  #10. indis 11. rakam olur
            a=veri[i]
            a=int(a)
            tümToplam+=a
        kosulTüm = tümToplam%10


        for i in range(0,9,2):
             a=veri[i]
             a=int(a)
             tekToplam+=a

        for i in range(1,9,2):
             a=veri[i]
             a=int(a)
             ciftToplam+=a
             

        kosulTekCift=(tekToplam*7+ciftToplam*9)%10
        kosulTek=(tekToplam*8)%10


        if kosulTüm==int(veri[10]) and kosulTekCift == int(veri[9])and kosulTek==int(veri[10]):
             return True
            


veri = int(input("lütfen TC kimlik no girin: "))
a = kimlikNo(veri)
print(a)
    
