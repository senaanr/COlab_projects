from tkinter import *
root = Tk()
root.title("GUI")
root.geometry("550x350")
root.wm_attributes("-alpha",0.99)

def verileri_al():
    etiket ["text"] = yazi.get()
   

yazi = Entry()
yazi.pack()

buton = Button(text="Verileri al", command = verileri_al)
buton.pack()

etiket = Label(text = "Veriler buraya yazılacak")
etiket.pack()





mainloop()
