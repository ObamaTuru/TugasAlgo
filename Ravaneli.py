def tampilBuku(dataBuku):
    print(("=="*25)+"\nData Buku\n"+("=="*25))
    for i in range(len(dataBuku)):
        print("Buku Ke-"+str(i+1),end=" | ")
        for y in dataBuku[i]:
            print(y,":",dataBuku[i][y],end=" | ")
        print() 
        
def tambah_mahasiswa(dataMahasiswa):
    while True:
        try:
            npm = int(input("Masukkan NPM: "))
            for mahasiswa in dataMahasiswa:
                if mahasiswa["NPM"] == npm:
                    print("Data dengan NPM tersebut sudah ada.")
                    return 0
            else:
                break
        except ValueError:
            print("Masukkan Digit NPM yang VALID!")
    nama = input("Masukkan Nama: ")
    dataMahasiswa.append({
        "Nama": nama,
        "NPM": npm
    })
    print("Data mahasiswa berhasil ditambahkan.")
