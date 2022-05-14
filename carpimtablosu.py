for i in range(1,11):
    print("**************")
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))

sayi = int(input("sayı: "))
asal = True

if sayi==1:
    asal= False

    
for i in range(2,sayi):
    if sayi%i==0:
        asal = False
        break
if asal==True:
    print("asal sayı")
else:
    print("sayı asal değil")
