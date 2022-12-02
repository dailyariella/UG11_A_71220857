print("====== Program Manipulasi String ======")
print("Pilihan Menu :")
print("1. Hitung Kata")
print("2. Ubah Kata")
pilihan=input("Pilihan anda :")
kata=input("Masukkan sebuah kalimat/kata :")

def hitung_kata () :
    a=input ("Masukkan kata yang ingin dihitung :")
    a1=kata.count (a)
    print ("Terdapat sebanyak",a1,"kata",a,"di dalam kalimat")

def ubah_kata ():
    b=input ("Masukkan kata yang ingin diubah :")
    c=input ("Masukkan kata pengganti :")
    d=kata.replace (b,c)
    print ("String berhasil diubah menjadi :",d)

if pilihan=="1":
    hitung_kata ()

elif pilihan=="2":
    ubah_kata ()
else:
    print ("Pilihan yang anda input tidak terdaftar di daftar pilihan")
