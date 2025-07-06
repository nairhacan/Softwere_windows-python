import tkinter as aps

aplikasi = aps.Tk()
aplikasi.title("Aplikasi GUI Nairha")
aplikasi.geometry("400x300")
aplikasi.resizable(True, True)

label = aps.Label(
    aplikasi,
    text="Halo Nairha!",
    font=("Arial", 14),
    fg="white",
    bg="purple"
)
label.pack(pady=20)

label2 = aps.Label(
    aplikasi,
    text="Selamat datang di aplikasi GUI",
    font=("Arial", 12),
    fg="black",
    bg="lightgray"
    )
label2.place(x=50, y=100)




aplikasi.mainloop()
