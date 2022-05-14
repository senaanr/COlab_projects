from tkinter import *
root = Tk()
root.title("GUI")
root.geometry("800x950")
root.minsize(550,600)
root.wm_attributes("-alpha", 0.3)
satir = Label(text = "Arayüz Programlama Arayüz Programlama Arayüz Programlama Arayüz Programlama", 
             fg = "white", 
             bg="black",
             padx = 20,
             pady = 5,
             wraplenght = 200 ,
             font = ("Open Sans", "25","overstrike"))
satir.pack()
mainloop()     
