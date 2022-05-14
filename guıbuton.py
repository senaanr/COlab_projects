from tkinter import *
root = Tk()
root.title("GUI")
root.geometry("550x350")
root.wm_attributes("-alpha",0.99)
def mesaj():
    print("merhaba")



buton = Button(text ="Tıkla",
               command = mesaj)#komut oluşturma


buton.pack()





mainloop()
