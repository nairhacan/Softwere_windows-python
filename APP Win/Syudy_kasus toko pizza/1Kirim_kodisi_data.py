import tkinter as aps

# membuat jendela utama
jendela = aps.Tk()
jendela.title("Toko pizza Nairha")
jendela.geometry("400x300")

# tampilan label
label = aps.Label(jendela, text="Selamat datang di Toko pizza Nairha", font=("Arial", 16))
label.pack(pady=20)

label_nama = aps.Label(jendela, text="Masukkan Nama Anda:", font=("Arial", 12))
label_nama.pack(pady=5)

masukan_nama = aps.Entry(jendela , width=30)
masukan_nama.pack(pady=10)

label_pilihan_menu = aps.Label(jendela, text="Pilih Menu Pizza:", font=("Arial", 12))
label_pilihan_menu.pack(pady=5)

# Logika
# akan ada 3 pilihan menu pizza dengan nama dan harga berbeda di karena kan hanya ada 3 pilihan maka 
# saya akan pakai menu bernama pizza merah sebagai main menu jika pizaa merah di pilih maka akan di tampilkan harga pizza merah
# jika pizza merah tidak di pilih makaa akan di tampilkan pilihan peperoni 
# jika keuda pizza tidak ada pilihan maka tampilkan pizza super wenak pol


pilihan_pizza = aps.StringVar()
pilihan_pizza.set("Pizza Merah")

aps.Radiobutton(jendela, text="pizza merah : 50.000" , variable=pilihan_pizza, value="Pizza Merah").pack()
aps.Radiobutton(jendela, text="peperoni : 65.000", variable=pilihan_pizza, value="Peperoni").pack()
aps.Radiobutton(jendela, text="super wenak pol : 80.000", variable=pilihan_pizza, value="Super Wenak Pol").pack()

# ====== Fungsi untuk mengirim data =====
def belakang():
    nama = masukan_nama.get()
    menu = pilihan_pizza.get()
    if menu == "Pizza merah":
        harga = 50000
    elif menu == "Peperoni":
        harga = 65000
    else:
        harga = 80000  # yang else ini adalah untuk menampilkan pizza super wenak pol jika pizza merah dan peperoni tidak di pilih
    
    hasil.config(text=f"Terima kasih {nama}, Anda telah memesan {menu} dengan harga Rp{harga:,}")
  



btn_kirim = aps.Button(jendela, text="Kirim", command=belakang)
btn_kirim.pack(pady=10)

hasil = aps.Label(jendela, text="", font=("Arial", 12))
hasil.pack(pady=10)



jendela.mainloop()

