from tkinter import *
root = Tk()
root.title("GUI")
root.geometry("550x350")
root.wm_attributes("-alpha",0.99)

yazi = Entry()
yazi.pack()

yazi.insert(0, "Test Yazısı")
yazi.delete(0, "end")
"""Yazı Alanındaki Veriyi Silmek
delete(0, "end")

Sadece Fare İmlecinin Seçildiği Alanı Silmek
delete("sel.first", "sel.last")

Yanıp Sönen İmlecten Yazının Sonuna Kadar olan kısmı Silmek
delete("insert", "end")"""




mainloop()
