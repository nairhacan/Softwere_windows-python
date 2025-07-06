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
    tombol_lanjut.pack(pady=10)



btn_kirim = aps.Button(jendela, text="Kirim", command=belakang)
btn_kirim.pack(pady=10)

hasil = aps.Label(jendela, text="", font=("Arial", 12))
hasil.pack(pady=10)

# Tombol untuk lanjut ke halaman 2 (minuman dan jumlah)
tombol_lanjut = aps.Button(jendela, text="Lanjut Proses Pizza?", command=lambda: buka_halaman_dua())
tombol_lanjut.pack_forget()  # disembunyikan dulu




def buka_halaman_dua():
    # Sembunyikan semua widget di halaman 1
    for widget in jendela.winfo_children():  #for widget in jendela.winfo_children():  //untuk widget di jendela ambil semua
        widget.pack_forget()      # semua widget di hilangkan

    # Halaman 2
    label2 = aps.Label(jendela, text="Halaman Minuman dan Jumlah Pizza", font=("Arial", 14))
    label2.pack(pady=10)

    label_jumlah = aps.Label(jendela, text="Masukkan Jumlah Pizza:")
    label_jumlah.pack()
    spin_jumlah = aps.Spinbox(jendela, from_=1, to=20)  #from_=1, to=20 berarti membatasi pilihan type number dari 1 - 20 pilihan 
    spin_jumlah.pack(pady=5)

    label_minum = aps.Label(jendela, text="Pilih Minuman:")
    label_minum.pack()
    minuman = aps.StringVar()
    minuman.set("Air Mineral")
    aps.OptionMenu(jendela, minuman, "Air Mineral", "Cola", "Jus Mangga").pack(pady=5)

    def selesai():
        hasil2 = aps.Label(jendela, text=f"Pemesanan Selesai!\nJumlah Pizza: {spin_jumlah.get()}\nMinuman: {minuman.get()}", fg="green")
        hasil2.pack(pady=10)

    aps.Button(jendela, text="Selesai Pesan", command=selesai).pack(pady=10)



jendela.mainloop()

