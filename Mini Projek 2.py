# Data login
akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

# Fungsi login dengan pengulangan dan error handling
def login():
    print("\nLogin Sistem Pengeluaran Mahasiswa")
    while True:
        try:
            username = input("Username: ")
            password = input("Password: ")

            if username in akun:
                if akun[username]["password"] == password:
                    role = akun[username]["role"]
                    print(f"Login berhasil sebagai {role.title()} ({username})")
                    return {"status": True, "username": username, "role": role}
                else:
                    print("Yah.. Password salah. Silakan coba lagi.\n")
            else:
                print("Username tidak ditemukan. Silakan coba lagi.\n")

        except KeyboardInterrupt:
            print("jangan tekan CTRL + C.")
            return {"status": False, "username": None, "role": None}

# Fungsi tampil pengeluaran
def hitung_pengeluaran(data, uang_awal):
    if not data:
        print("Belum ada pengeluaran yang dicatat.")
    else:
        print("Riwayat semua pengeluaran:")
        total = 0
        for tanggal, info in data.items():
            print(f"{tanggal} | {info['kategori']} | Rp{info['jumlah']}")
            total += info['jumlah']
        print("Total pengeluaran: Rp", total)
        print("Sisa uang: Rp", uang_awal - total)

# Fungsi menu untuk user (CRUD)
def menu_user(data, uang_awal):
    while True:
        print("\nPilih menu:")
        print("1. Tambah Pengeluaran")
        print("2. Tampilkan Semua Pengeluaran")
        print("3. Update Pengeluaran")
        print("4. Hapus Pengeluaran")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == "1":
            try:
                tanggal = input("Masukan Tanggal (DD-MM-YYYY): ")
                kategori = input("Kategori pengeluaran: ")
                jumlah = int(input("Jumlah pengeluaran (Rp): "))
                data[tanggal] = {"kategori": kategori, "jumlah": jumlah}
                print("Pengeluaran berhasil dicatat.")
            except ValueError:
                print("Input jumlah harus berupa angka.")

        elif pilihan == "2":
            hitung_pengeluaran(data, uang_awal)
            break
        elif pilihan == "3":
            tanggal = input("Masukkan tanggal pengeluaran yang ingin diubah (DD-MM-YYYY): ")
            if tanggal in data:
                kategori = input("Kategori baru: ")
                try:
                    jumlah = int(input("Jumlah baru (Rp): "))
                    data[tanggal] = {"kategori": kategori, "jumlah": jumlah}
                    print("Pengeluaran berhasil diperbarui.")
                except ValueError:
                    print("Jumlah harus berupa angka.")
            else:
                print("Tanggal tidak ditemukan.")
            break
        elif pilihan == "4":
            tanggal = input("Masukkan tanggal pengeluaran yang ingin dihapus (DD-MM-YYYY): ")
            if tanggal in data:
                del data[tanggal]
                print("Pengeluaran berhasil dihapus.")
            else:
                print("Tanggal tidak ditemukan.")
            break
        elif pilihan == "5":
            print("keluar dari program.")
            break
        else:
            print("tidak ada pilihan.")

# Fungsi menu untuk admin (Read only)
def menu_admin(data, uang_awal):
    while True:
        print("\nPilih menu:")
        print("1. Tampilkan Semua Pengeluaran")
        print("2. Keluar")
        pilihan = input("Masukkan pilihan (1/2): ")

        if pilihan == "1":
            hitung_pengeluaran(data, uang_awal)
            break
        elif pilihan == "2":
            print("keluar dari program.")
            break
        else:
            print("tidak ada pilihan.")

# Program utama
print("Catatan Pengeluaran Keuangan Harian Mahasiswa")
print("Nama: Mohammed Rifqy Syahdi")
print("NIM: 2509116037")
print("Kelas: Sistem Informasi A '2025")

try:
    uang_awal = int(input("Masukkan uang sangu awal bulan (Rp): "))
except ValueError:
    print("Input harus berupa angka.")
    exit()
except KeyboardInterrupt:
    print("jangan tekan CTRL + C.")
    exit()

riwayat_pengeluaran = {}

hasil_login = login()
if hasil_login["status"]:
    if hasil_login["role"] == "user":
        menu_user(riwayat_pengeluaran, uang_awal)
    elif hasil_login["role"] == "admin":
        menu_admin(riwayat_pengeluaran, uang_awal)

