"""from tkinter import *
root = Tk()
satir = Label(root, text="Merhaba")
satir.pack()
mainloop() """

from tkinter import *
pencere = Tk()
pencere.title("GUI")
pencere.geometry("550x150+450+50") #+dan sonraki kısımlar pencerenin ekranın neresinde açılacağını gösterir
#pencere.resizable(FALSE,FALSE)1.sağdan sola 2.yukarı aşağı pencereyi istediğimiz gibi boyutlandırmayı engeller
#pencere.minsize(100,100)pencerenin alacağı en küçük boyutu belirler
#pencere.maxsize(500,860)pencerenin alacağı en büyük boyut
#pencere.state("zoomed")pencere tam ekran olarak açılır
#pencere.state("iconic")pencere simge durumunda çalışır ekranda değil simge cubuğunda
#pencere.state("normal")
#pencere.wm_attributes("-alpha", 0.1)0-1 arası değerler yazılır 0a ne kadar yakınsa o kadar saydam olur
yazi = Label(text="Merhaba ",
             fg="red",
             bg="blue",
             width = 15, #yazı alanı 
             height = 5 ,#yazı alanı
             padx = 15,
             pady = 30, #yazı alanı iç boşluğu alttan üstten
             wraplength = 150, # yazıyı alan içine sığdırır
             justify = "left", #yazıyı secilen tarafa doğru yaslar center(ortalama)
             anchor = "se",#yazı aşağı ve sağ tarafa yaslanır, nw(yukarı ve sola)

             
             font = ("Open Sans","20", "normal"))#bold(kalın),underline,overstrike(yazının ortası çizik)
yazi.pack()





mainloop()



 
