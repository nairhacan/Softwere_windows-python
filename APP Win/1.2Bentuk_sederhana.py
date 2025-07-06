

# dari Tkinter import ke * 
# yang artinya TKniter ini memekai nama asli untuk menggunakan wiegdet nya jadi lebih sederhana 
# yang asal nya pakai nama alias (as) menjadi langsung cetak
from tkinter import *

# langusng panggil widget nya 
jendela = Tk()
jendela.title("nairha")
jendela.geometry("200x300")
# di ini anda tidak perlu variabel untuk mencetaj hello world cukup dengan
label = Label(jendela, text="Halo Dunia!").pack()

jendela.mainloop()