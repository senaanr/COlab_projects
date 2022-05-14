liste = ["1","2","5a","10b","abc","10","50"]
 #Liste elemanları içindeki sayısal değerleri bulunuz.
for x in liste:
    try:
        sonuc = int(x)
        print(sonuc)
    except ValueError:
        continue

#kullanıcı "quit(q)" girmedikçe alınan her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın
"""while True:
    x = input("sayı: ")
    if x == "q":
        break
    try:
        sonuc = float(x)
        print("girilen sayı: ", x)
        
    except ValueError:
        print("geçersiz sayı")
        continue
"""
# dictionary ve key bilgilerini parametre olarak alan get(d,key) fonk hazırlayın
urun = {"urunadi":"samsung s10"}

def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
print(get(urun, "fiyat")) 
print(get(urun, "urunadi"))   