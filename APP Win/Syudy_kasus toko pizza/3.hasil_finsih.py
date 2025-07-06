from tkinter import *

# Membuat jendela utama
jendela = Tk()
jendela.title("Toko Pizza Nairha")
jendela.geometry("400x500")

# Halaman 1 - Pilih Pizza
def halaman_utama():
    for widget in jendela.winfo_children():
        widget.pack_forget()

    Label(jendela, text="Selamat datang di Toko Pizza Nairha", font=("Arial", 14)).pack(pady=10)

    Label(jendela, text="Masukkan Nama Anda:").pack()
    nama_entry = Entry(jendela)
    nama_entry.pack(pady=5)

    Label(jendela, text="Pilih Menu Pizza:").pack()

    var_pizza = StringVar(value="Pizza Merah")
    Radiobutton(jendela, text="Pizza Merah - 50.000", variable=var_pizza, value="Pizza Merah").pack()
    Radiobutton(jendela, text="Peperoni - 65.000", variable=var_pizza, value="Peperoni").pack()
    Radiobutton(jendela, text="Super Wenak Pol - 80.000", variable=var_pizza, value="Super Wenak Pol").pack()

    def lanjut_halaman2():
        nama = nama_entry.get()
        pizza = var_pizza.get()
        harga = 50000 if pizza == "Pizza Merah" else 65000 if pizza == "Peperoni" else 80000
        halaman_minuman(nama, pizza, harga)

    Button(jendela, text="Lanjut", command=lanjut_halaman2).pack(pady=10)

# Halaman 2 - Minuman dan Jumlah
def halaman_minuman(nama, pizza, harga_pizza):
    for widget in jendela.winfo_children():
        widget.pack_forget()

    Label(jendela, text="Halaman Minuman & Jumlah Pizza", font=("Arial", 14)).pack(pady=10)

    Label(jendela, text="Masukkan Jumlah Pizza:").pack()
    jumlah_spin = Spinbox(jendela, from_=1, to=20)
    jumlah_spin.pack()

    Label(jendela, text="Pilih Minuman:").pack()
    var_minum = StringVar(value="Air Mineral")
    minuman_dropdown = OptionMenu(jendela, var_minum, "Air Mineral", "Cola", "Jus Mangga")
    minuman_dropdown.pack(pady=5)

    def lanjut_halaman3():
        jumlah = int(jumlah_spin.get())
        minum = var_minum.get()
        harga_minum = 5000 if minum == "Air Mineral" else 8000 if minum == "Cola" else 10000
        total = (harga_pizza * jumlah) + harga_minum
        halaman_pembayaran(nama, pizza, jumlah, minum, total)

    Button(jendela, text="Lanjut ke Pembayaran", command=lanjut_halaman3).pack(pady=10)

# Halaman 3 - Pembayaran
def halaman_pembayaran(nama_user, menu_pizza, jumlah_pizza, minuman_user, total):
    for widget in jendela.winfo_children():
        widget.pack_forget()

    Label(jendela, text="Halaman Pembayaran", font=("Arial", 14)).pack(pady=10)
    Label(jendela, text=f"Total yang harus dibayar: Rp{total:,}", font=("Arial", 12)).pack(pady=5)

    metode = StringVar(value="Tunai")

    Label(jendela, text="Pilih Metode Pembayaran:").pack()
    Radiobutton(jendela, text="Tunai", variable=metode, value="Tunai", command=lambda: tampil_input_uang()).pack()
    Radiobutton(jendela, text="Transfer Bank", variable=metode, value="Transfer", command=lambda: tampil_input_uang()).pack()
    Radiobutton(jendela, text="QRIS", variable=metode, value="QRIS", command=lambda: tampil_input_uang()).pack()

    label_metode = Label(jendela, text="", font=("Arial", 12))
    input_uang = Entry(jendela)
    hasil_label = Label(jendela, text="", font=("Arial", 11))
    bayar_button = Button(jendela, text="Bayar Sekarang")
    donasi_button = None

    def tampil_input_uang():
        nonlocal donasi_button
        label_metode.config(text=f"Bayar dengan {metode.get()}")
        label_metode.pack(pady=5)
        input_uang.pack()
        bayar_button.config(command=cek_uang)
        bayar_button.pack(pady=5)
        hasil_label.pack(pady=10)
        if donasi_button:
            donasi_button.destroy()

    def cek_uang():
        nonlocal donasi_button
        try:
            uang = int(input_uang.get())
            if uang < total:
                hasil_label.config(text="Uang anda kurang cepat bayar 😡", fg="red")
                if donasi_button:
                    donasi_button.destroy()
                    donasi_button = None
            elif uang == total:
                hasil_label.config(
                    text=f"Wah terimakasih {nama_user},\nAnda telah memesan {menu_pizza} x{jumlah_pizza}\nMinuman: {minuman_user}",
                    fg="green"
                )
                if donasi_button:
                    donasi_button.destroy()
                    donasi_button = None
            else:
                kembalian = uang - total
                hasil_label.config(text=f"Uang anda kembalian Rp{kembalian:,}", fg="blue")
                if not donasi_button:
                    def donasi():
                        hasil_label.config(text="Terima kasih atas donasinya 🙏", fg="purple")
                        donasi_button.destroy()

                    donasi_button = Button(jendela, text="Mau Donasi?", command=donasi)
                    donasi_button.pack(pady=5)
        except:
            hasil_label.config(text="Masukkan angka yang valid!", fg="orange")

    # Mulai tampilkan input
    tampil_input_uang()

# Jalankan dari halaman pertama
halaman_utama()
jendela.mainloop()
