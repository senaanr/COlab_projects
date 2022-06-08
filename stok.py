stok = {}

def urun_ekle(stok):
    while True:
        print(""" 
              Ürün ID numarası 6 haneli
              Ürün Kategorisi
              Ürün İsmi
              Ürün Rengi
              Ürün Adedi
              Ürün Birim Alış Fiyatı
              Ürün Birim Satış Fiyatı
              """)
        
        urun_id = input("ürün_id: ")
        sozluk = {}
        
        if urun_id.startswith("101") == True:
            urun_kategorisi = "Telefon"
    
        elif urun_id.startswith("201") == True:
            urun_kategorisi = "Bilgisayar"
            
        elif urun_id.startswith("301") == True:
            urun_kategorisi = "Beyaz Eşya"
            
        elif urun_id.startswith("401") == True:
            urun_kategorisi = "Ev Aletleri"
        
        elif urun_id == "999":
            break

        menu = {}  
        urun_adet = input("Adet: ")
        menu["Adet"] = urun_adet
        urun_alis = float(input("Alış Fiyatı: "))
        menu["Ürün Alış Fiyatı"] = urun_alis       
        urun_satis = float(input("Satış Fiyatı: "))
        menu["Ürün Satış Fiyatı"] = urun_satis               
        urun_renk = input("Renk: ")
        menu["Renk"] = urun_renk
        urun_isim = input("İsim: ")
        menu["İsim"] = urun_isim
    

        sozluk[urun_kategorisi] = menu
        stok[urun_id] = sozluk
        print(stok)
    

def urun_cikar(stok,silinecek_urun_id):
    del stok[silinecek_urun_id]
    
    return stok

def urun_bilgi_guncelle(stok, guncellenecek_urun_id, urun_kategorisi):
    a = input("Değiştirmek istediğiniz bilgi: ")
    b = input("Güncellenecek değeri: ")
    stok[guncellenecek_urun_id][urun_kategorisi][a] = b
    # stok[guncellenecek_urun_id][urun_kategorisi][a] = a
    # stok[guncellenecek_urun_id][urun_kategorisi]["Ürün Satış Fiyatı"] = a
    

def stok_goruntule(stok):
    for i,j in stok.items():
            print(i," : ",j)

while True:
    print("""
          [1] Ürün Ekle
          [2] Ürün Çıkar
          [3] Ürün Bilgilerini Güncelle
          [4] Stok Görüntüle
          [0] Çıkış
          """)
    
    secim = int(input("işlem numarası: "))
    
    if secim == 0:
        break
    elif secim == 1:
        urun_ekle(stok)
    elif secim == 2:
        silinecek_urun_id = input("Silmek istediğiniz ürünün id'si : ")
        urun_cikar(stok,silinecek_urun_id)
    elif secim == 3:
        guncellenecek_urun_id = str(input("Ürün id'si giriniz: "))
        urun_kategorisi = str(input("Kategori adını giriniz: "))
        urun_bilgi_guncelle(stok,guncellenecek_urun_id, urun_kategorisi)
    elif secim == 4:
        stok_goruntule(stok)
        print(type(stok))
    else:
        print("yanlış işlem numarası")