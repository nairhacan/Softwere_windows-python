import tkinter as aps

aplikasi = aps.Tk()
aplikasi.title("Form Nama Sederhana")
aplikasi.geometry("300x150")

# Kolom input nama
input_nama = aps.Entry(aplikasi)
input_nama.pack(pady=10)

# Label untuk menampilkan hasil
hasil = aps.Label(aplikasi, text="")
hasil.pack()


# Fungsi kirim_data (akan dipanggil saat tombol ditekan)
def kirim_data():
    nama = input_nama.get()
    # di bagian ini
    hasil.config(text=f"Halo {nama}!")
    # variabel Hasil akan di di ubah atau di isi istilah nya dengan widget config
    # yang jika di baca hasil.ubah(teks=f"Halo {nama}!")
    # {nama} ini adalah tempat di mana variabel nama akan di masukkan dan di tampilkan 
    # f adalah format string yang memungkinkan kita untuk memasukkan variabel ke dalam string


    



# Tombol untuk memicu fungsi kirim_data
tombol = aps.Button(aplikasi, text="Kirim", command=kirim_data)
tombol.pack(pady=10)

# command adalah perintah yang dikasih ke tombol, supaya tombol tahu harus ngapain waktu diklik.

aplikasi.mainloop()
