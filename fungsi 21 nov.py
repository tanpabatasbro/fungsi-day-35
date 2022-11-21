def hello_word(nama):
    print(f"selamat datang di python {nama}")

hello_word("armin")#memanggil fungsi

#fungsi penjumlahan
def tambah(angka_1,angka_2):
    hasil = angka_1 +angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(5,3)

def group(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")

anggota = ["ucup","otong","dudung","asep"]
group(anggota)
