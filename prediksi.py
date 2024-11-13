import tkinter as tk
from tkinter import messagebox

def hasil_prediksi():
    try:
        for entry in entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100")

# 
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

# Membuat label
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 10, "bold"), bg="#ff0000")
judul_label.pack(pady=20)

# Membuat kotak input
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

# Membuat 10 kotak input untuk masing masing nilai disetiap mata pelajaran
# semua hasil input akan disimpan didalam entries buat memudahkan pengecekan di fungsi hasil prediksi nanti
entries = []
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}:", font=("Arial", 10, "bold"), bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(frame_input, width=10, font=("Arial", 10))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Membuat tombol prediksi. ketika di klik, hasil prediksi akan muncul
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 10, "bold"), bg="#f0f0f0")
prediksi_button.pack(pady=30)

# Menampilkan hasil prediksi. Kalau prediksinya berhasil, teksnya berubah tergantung hasil
hasil_label = tk.Label(root, text="", font=("Arial", 10, "italic", "bold"), fg="green", bg="#f0f0f0")
hasil_label.pack(pady=20)

# Menjalankan Aplikasi
root.mainloop()