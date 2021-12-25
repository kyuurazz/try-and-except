def input_nama():
    global nama
    while True:
        nama = input("Masukkan Nama        : ") 
        if nama == "":
            print("Nama Tidak Boleh Kosong!\n")
            print("Masukan Nama dengan Benar")
        else:
            return nama


def input_nim():
    global nim
    while True:
        try:
            nim = int(input("Masukkan NIM         : "))
            if nim == "":
                print("NIM Tidak Boleh Kosong!")
        except ValueError:
            print("\nMasukan NIM Dengan Angka")
        else:
            return nim


def input_tugas():
    global tugas
    while True:
        try:
            tugas = int(input("Masukkan Nilai Tugas : "))
            if tugas == "":
                print("Nilai Tugas Tidak Boleh Kosong!")
        except ValueError:
            print("\nMasukan Nilai Tugas Dengan Angka")
        else:
            return tugas


def input_uts():
    global uts
    while True:
        try:
            uts = int(input("Masukkan Nilai UTS   : "))
            if uts == "":
                print("Nilai UTS Tidak Boleh Kosong!")
        except ValueError:
            print("\nMasukan Nilai UTS Dengan Angka")
        else:
            return uts


def input_uas():
    global uas
    while True:
        try:
            uas = int(input("Masukkan Nilai UAS   : "))
            if uas == "":
                print("Nilai UAS Tidak Boleh Kosong!")
        except ValueError:
            print("\nMasukan Nilai UAS Dengan Angka")
        else:
            return uas