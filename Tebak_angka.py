from tkinter import *
from tkinter import messagebox
from random import *

root = Tk()
root.resizable(0,0)
root.title("Tebang V2.0")

jawaban = randrange(1,10)
kesempatan = 3

def cek(angka):
	global jawaban	
	global kesempatan
	user = int(angka)
	try:
		if user == jawaban:
			messagebox.showinfo("Selamat", "Anda Menang!")
			root.destroy()
		elif user < jawaban:
			messagebox.showwarning("Salah", "Jawaban yang Anda Masukkan Lebih Kecil dari Angka yang Ditentukan.")
			kesempatan -= 1
			if kesempatan == 0:
				messagebox.showerror("Gagal", "Kesempatan yang Anda Miliki Telah Habis.")
				root.destroy()
			pilihan.delete(0, END)
		elif user > jawaban:
			messagebox.showwarning("Salah", "Jawaban yang Anda Masukkan Lebih Besar dari Angka yang Ditentukan.")
			kesempatan -= 1
			if kesempatan == 0:
				messagebox.showerror("Gagal", "Kesempatan yang Anda Miliki Telah Habis.")
				root.destroy()
			pilihan.delete(0,END)
		Label(root, text="Kesempatan Anda tersisa: {}".format(kesempatan)).grid(row=7, pady=5)
	except Exception:
		pass

Label(root, text="Tebak Angka 2.0").grid(row=0)

Label(root, text=" ").grid(row=1)

Label(root, text="Peraturan:\n1. Pemain harus menebak Angka yang telah ditentukan secara acak oleh komputer.\n2. Angka yang dipilih dimulai dari angka 1-9\n3. Pemain memiliki kesempatan sebanyak 3 kali.\n4. Apabila kesempatan telah habis, permainan akan berakhir.").grid(row=2)

Label(root, text=" ").grid(row=3, pady=3)

pilihan = Spinbox(root, from_=1, to=9, borderwidth=5, state='readonly', exportselection=True, width=25, justify=CENTER)
pilihan.grid(row=4)

Label(root, text=" ").grid(row=5, pady=3)

Label(root, text="Kesempatan Anda tersisa: {}".format(kesempatan)).grid(row=7, pady=5)

btn = Button(root, text="Cek Jawaban", width=15, command=lambda: cek(pilihan.get())).grid(row=6, pady=10)

root.mainloop()