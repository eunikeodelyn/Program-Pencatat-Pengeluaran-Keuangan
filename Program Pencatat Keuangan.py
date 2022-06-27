import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg 

try:
    def show():
        my_string_var1.set("""Data pengeluaran makanan Anda: Rp. %s\nData pengeluaran transportasi Anda: Rp. %s
        Data pengeluaran edukasi Anda: Rp. %s\nData pengeluaran kesehatan Anda: Rp.%s\nData pengeluaran belanja Anda: Rp.%s""" 
        % (makanminum.get(),transportasi.get(), edukasi.get(),kesehatan.get(), belanja.get()))

except ValueError: 
    msg.showwarning("Warning", "Program Hanya Menerima Nilai Integer")
    
finally:
    print("TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI!")

main_window = tk.Tk()
#labels
tk.Label(main_window, text="Pencatatan Keuangan", font=('Times New Roman', 20, 'bold'), justify='center').grid(row=0, column=0)
tk.Label(main_window, text="Pilih kategori pengeluaran:", font=('Sans Serif', 14), justify='center').grid(row=1, column=0)
tk.Label(main_window, text="Masukkan data pengeluaran makanan : ").grid(row=2, column=0)
tk.Label(main_window, text="Masukkan data pengeluaran transportasi : ").grid(row=3, column=0)
tk.Label(main_window, text="Masukkan data pengeluaran edukasi : ").grid(row=4, column=0)
tk.Label(main_window, text="Masukkan data pengeluaran kesehatan : ").grid(row=5, column=0)
tk.Label(main_window, text="Masukkan data pengeluaran belanja : ").grid(row=6, column=0)
tk.Label()

makanminum = tk.Entry(main_window)
transportasi = tk.Entry(main_window)
edukasi = tk.Entry(main_window)
kesehatan = tk.Entry(main_window)
belanja = tk.Entry(main_window)

my_string_var1 = StringVar()

#text input
makanminum.grid(row=2, column=1)
transportasi.grid(row=3, column=1)
edukasi.grid(row=4, column=1)
kesehatan.grid(row=5, column=1)
belanja.grid(row=6, column=1)

tk.Button(main_window, text="Click Me", command= show).grid(row=8, column=1, pady=8)

my_label1 = Label(main_window,textvariable = my_string_var1, font=('Baskerville', 12)).grid(row=10, column = 0, pady=5)
my_string_var1.set("Data Akan Ditampilkan Disini")

main_window.mainloop()
