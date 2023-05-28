def tampil_mahasiswa(dataMahasiswa):
    print(("=="*25)+"\nData Mahasiswa\n"+("=="*25))
    for i in range(len(dataMahasiswa)):
        print("Mahasiswa Ke-"+str(i+1),end=" | ")
        for y in dataMahasiswa[i]:
            print(y,":",dataMahasiswa[i][y],end=" | ")
        print() 

def edit_mahasiswa(dataMahasiswa):
    try:
        npm = int(input("Masukkan NPM mahasiswa yang akan diedit: "))
    except ValueError:
        print("NPM tersebut tidak ada.")
        return 0
    for mahasiswa in dataMahasiswa:
        if mahasiswa["NPM"] == npm:
            new_nama = input("Masukkan Nama baru: ")
            confirmation = input("Apakah Anda yakin ingin mengedit Nama tersebut? (Y/N): ")
            if confirmation.lower() == "y":
                mahasiswa["Nama"] = new_nama
                print("Data mahasiswa berhasil diubah.")
                return 1
            else:
                print("Proses edit dibatalkan.")
                return 0
    print("NPM tersebut tidak ada.")
    return 0


