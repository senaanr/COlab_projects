#faktöriyel fonk oluşturup gelen değer için hata mesajları verin
#tür dönüşümü, negatif değer 

"""def faktoriyel(x):
    x = int(x)
    if x<0:
        raise ValueError("negatif değer")
    
    sonuc = 1
    for i in range(1,x+1):
        sonuc *= i
        
    return sonuc

for i in [5,7,"a",2,-4,"10a"]:
    try:
        x = faktoriyel(i)
    except ValueError as e:
        print(e)
        continue
    else:
        print(x)
        
        
#girilen parola içinde türkçe karakter hatası veriniz
def parolakontrol(parola):
    turkce_karakterler="şçğüöıİ"
    
    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("parola türkçe karakter içeremez.")
    print("geçerli parola")
    
parola = input("parola: ")
try:
    parolakontrol(parola)
except TypeError as e:
    print("hata:", e)"""
        
        
def bolme(sayi1, sayi2):
    assert (sayi2>0), "İkinci sayı sıfırdan farklı olmalı" #olabilecek ihtimal ve hata metni
    sonuc = sayi1 / sayi2
    return sonuc
bolme(12,0)