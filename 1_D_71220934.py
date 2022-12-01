print("Halo selamat datang di bioskop!")

def tempat():
    print("Dimanakah kamu ingin menonton?")
    print("1) XXI Empire")
    print("2) XXI Amplaz")
    print("3) XXI JCM")
    A = input("Masukkan pilihanmu: ")
    if(A == "4"):
        print("Pilihan tidak tersedia.")

def film():
    print("Mau nonton film apa nih? Ada film:")
    print("1. Frozen")
    print("2. Keramat")
    print("3. KKN di Desa Penari")
    B = input("Pilih nomor film: ")
    if(B =="4"):
        print("Pilihan tidak tersedia.")


def layar():
    print("Mau nonton layar bioskop apa :")
    print("1. Reguler")
    print("2. Dolby almos")
    print("3. Premiere")
    C = input("Pilih nomor tipe layar: ")
    if(C =="4"):
        print("Pilihan tidak tersedia.")
    D = input("Berapa banyak tiket? ")


def jam():
    print("Mau nonton jam berapa: ")
    print("1. 12.35")
    print("2. 14.45")
    print("3. 16.55")
    print("4. 19.05")
    E = input("Masukkan angka pilihan Anda: ")
    if(E == "1"):
        print("Oke berhasil, silahkan dinikmati di jam 12.35")
    elif(E == "2"):
        print("Oke berhasil, silahkan dinikmati di jam 14.45")
    elif(E == "3"):
        print("Oke berhasil, silahkan dinikmati di jam 16.55")
    else:
        print("Oke berhasil, silahkan dinikmati di jam 19.05")


tempat()
film()
layar()
jam()