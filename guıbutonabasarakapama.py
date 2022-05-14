from tkinter import *
root = Tk()
root.title("GUI")
root.geometry("550x350")
root.wm_attributes("-alpha",0.99)



def degistir():
    etiket ["text"] = "merhaba dünya" #etiketin içine değiştirmek istenen şey yazılır
    etiket ["bg"] = "yellow"


def kapat():
    quit()


    
etiket = Label(text ="Hello World", bg ="blue")
etiket.pack()
 


buton = Button(text ="ceviri",
               command = degistir)#komut oluşturma


buton.pack()

buton2 = Button(text="kapat", command=kapat)
buton2.pack()



mainloop()
