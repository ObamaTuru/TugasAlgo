#####KONTRIBUTOR#####
from Arjun import tampil_mahasiswa, edit_mahasiswa
from Reo import hapus_mahasiswa 
from Ravaneli import tambah_mahasiswa,tampilBuku
from Reza import hapus_buku,tambah_buku
from Amin import ubah_buku
'''hilmi di file ini'''

##################### CONTOH DATA ##############################
dataMahasiswa = [{"Nama" : "Rudi Keling", "NPM" : 2205045089},
                {"Nama" : "Cifut Keling", "NPM" : 2205045089},
                {"Nama" : "Rukpo Keling", "NPM" : 2205045079},
                {"Nama" : "Yadi Keling", "NPM" : 2205045079}]

dataBuku = [{
    "ISBN": "978-3-16-148410-0", "Judul": "Harry Potter",
    "Tahun Terbit": "1998",
    "Penerbit": "Bloomsbury Publishing",
    "Jumlah Buku": 100
},
{
    "ISBN": "978-3-16-148410-2",
    "Judul": "Kamar Rahasia",
    "Tahun Terbit": "1998",
    "Penerbit": "Bloomsbury Publishing",
    "Jumlah Buku": 100
},{
    "ISBN": "978-3-16-148410-19",
    "Judul": "Buah Apel",
    "Tahun Terbit": "1998",
    "Penerbit": "Bloomsbury Publishing",
    "Jumlah Buku": 100
}]

dataPeminjam = [{
        "Tanggal Peminjaman": 5,
        "Tanggal Pengembalian": 12,
        "Nama Peminjam":  "Rudi Keling",
        "Nama Buku yang Dipinjam": "Kamar Rahasia",
        "Denda": 0,
        "Status": "Pinjam"
    }]

dataPengembali = [{
        "Tanggal Peminjaman": 5,
        "Tanggal Pengembalian": 12,
        "Nama Peminjam":  "Yadi Keling",
        "Nama Buku yang Dipinjam": "Harry Potter",
        "Denda": 0,
        "Status": "Kembali"
    },
    {
        "Tanggal Peminjaman": 5,
        "Tanggal Pengembalian": 12,
        "Nama Peminjam":  "Rukpo Keling",
        "Nama Buku yang Dipinjam": "Kamar Rahasia",
        "Denda": 0,
        "Status": "Kembali"
    }]

#0. PESAN VALIDSI ERROR

def validasi(stringCust="Kesalahan Input!"):
    print("=!"*25)
    print(stringCust)
    print("=!"*25)


###########Main Program Bagian Bersama#########
while True:
    pilMain = input(("="*50)+"\nMenu Utama\n"+("="*50)+"\n1. Menu Mahasiswa/Peminjam\n2. Menu Katalog Buku\n3. Menu Transaksi Peminjaman Buku\n4. Histori Pengembalian Buku\n5. Exit\n"+("="*50)+"\nMasukkan Pilihan: ")
    if pilMain == '1':
        while True:
            pilSub = input(("="*50)+"\nSub Menu Mahasiswa\n"+("="*50)+"\n1. Tampil Mahasiswa\n2. Tambah Mahasiswa\n3. Edit Mahasiswa\n4. Hapus Mahasiswa\n5. Kembali Menu Utama\n"+("="*50)+"\nMasukkan Pilihan: ")
            if pilSub == '1':
                tampil_mahasiswa(dataMahasiswa) #Bagian_Arjun
            elif pilSub == '2':
                tambah_mahasiswa(dataMahasiswa) #Bagian_Neli
            elif pilSub == '3':
                edit_mahasiswa(dataMahasiswa) #Bagian_Arjun
            elif pilSub == '4':
                hapus_mahasiswa(dataMahasiswa) #Bagian_Reo
            elif pilSub == '5':
                break
            else:
                validasi()

    elif pilMain == '2':
        while True:
            pilSub = input(("="*50)+"\nSub Menu Buku\n"+("="*50)+"\n1. Tampil Buku\n2. Tambah Buku\n3. Edit Buku\n4. Hapus Buku\n5. Kembali Menu Utama\n"+("="*50)+"\nMasukkan Pilihan: ")
            if pilSub == '1':
                tampilBuku(dataBuku) #Bagian neli 
            elif pilSub == '2':
                tambah_buku(dataBuku) #Bagian reza
            elif pilSub == '3':
                ubah_buku(dataBuku) #Bagian amin
            elif pilSub == '4':
                hapus_buku(dataBuku,dataPeminjam) #Bagian reza
            elif pilSub == '5':
                break
            else:
                validasi()


######################################Bagian Hilmi##################################
    elif pilMain == '3':            
        #1. Validasi Peminjam
        def validasiNamaDanBuku(nama,kata="Nama"):
            num=0
            if kata=="Nama": #validasi nama mahasiswa
                for i in dataMahasiswa:
                    if nama == i[kata]:
                        return num
                    num+=1
                return -1
            elif kata=="Judul": #validasi nama buku
                for i in dataBuku:
                    if nama == i[kata]:
                        return num
                    num+=1
                return -1
            else:
                for i in dataPeminjam: #validasi nama peminjam
                    if nama == i[kata]:
                        return num
                    num+=1
                return -1
        #2. Validasi tanggal    
        def validasiTgl(tgl):
            if tgl.isdigit():
                tgl=int(tgl)
                if tgl>0:
                    return 1
                else: 
                    return 0
            else:
                return 0
        #3. Menampilkan peminjam
        def tampilPeminjam():
            print(("=+"*25)+"\nDaftar Peminjam\n"+("=+"*25))
            for i in range(len(dataPeminjam)):
                print("Peminjam Ke-"+str(i+1))
                for y in dataPeminjam[i]:
                    print(y,":",dataPeminjam[i][y])
                print("=+"*25) 


        while True:
            pilSub = input(("="*50)+"\nMenu Transaksi Peminjaman\n"+("="*50)+"\n1. Daftar Peminjam Aktif\n2. Tambah Peminjam\n3. Edit Peminjam\n4. Pengembalian\n5. Hapus Peminjam\n6. Kembali Menu Utama\n"+("="*50)+"\nMasukkan Pilihan: ")
            #1 Tampil Peminjam
            if pilSub == '1':
                tampilPeminjam()
            #2 Tambah Peminjam
            elif pilSub == '2':
                while True: #validasi nama    
                    nama = input("Masukkan Nama Peminjam: ")
                    if validasiNamaDanBuku(nama)>=0:
                        cek=validasiNamaDanBuku(nama,"Nama Peminjam")
                        if cek>=0 and dataPeminjam[cek]["Status"]=="Pinjam":
                            print("=======Anda Sedang Meminjam Buku=======")
                            for i in dataPeminjam[cek]:
                                print(str(i)+" : "+str(dataPeminjam[cek][i]))
                            break
                        print("Buku Yang Tersedia: ")
                        tampilBuku(dataBuku)
                        while True:
                            while True: #validasi buku 
                                buku = input("Masukkan Nama Buku: ")
                                stokKe=validasiNamaDanBuku(buku,"Judul")
                                if dataBuku[stokKe]["Jumlah Buku"]<1:
                                    validasi("Stok Buku Habis, Masukkan Judul Lain!")
                                else:
                                    break
                            if stokKe>=0:
                                while True:  #validasi tanggal
                                    tgl = input("Masukkan Tanggal Sekarang (Format Angka): ")
                                    if validasiTgl(tgl):
                                        tgl=int(tgl) 
                                        break
                                    else:
                                        validasi("Masukkan Tanggal Dengan Benar!")
                                #Mengurangi Stok
                                dataBuku[stokKe]["Jumlah Buku"]-=1 
                                #Proses Penambahan
                                '''Tanggal Pengembalian (Default : H+7 dari tanggal peminjaman, format :D)'''
                                tglKembali=tgl+7
                                dataTambahPeminjam={
                                    "Tanggal Peminjaman": tgl, 
                                    "Tanggal Pengembalian": tglKembali,
                                    "Nama Peminjam": nama,
                                    "Nama Buku yang Dipinjam" : buku,
                                    "Denda": 0,
                                    "Status": "Pinjam"
                                }
                                dataPeminjam.append(dataTambahPeminjam)
                                validasi("Berhasil Tambah Data")
                                break
                            else:
                                validasi("Buku Tidak Tersedia!")
                        break
                    else:
                        validasi("Nama Tidak Tersedia Pada Data Mahasiswa/Peminjam!")
                        break
                
            # 3 Edit Peminjam
            elif pilSub == '3':
                while True: #validasi nama    
                    nama = input("Masukkan Nama Peminjam: ")
                    #Menandai Index Mahasiswa
                    mahaKe=validasiNamaDanBuku(nama,"Nama Peminjam")
                    if mahaKe>=0:
                        while True: #validasi tanggal
                            tgl = input("Masukkan Tanggal Sekarang (Format Angka): ")
                            if validasiTgl(tgl):
                                tgl=int(tgl)
                                while True: #Proses Ubah Data
                                    buku = input("Masukkan Nama Buku: ")
                                    if validasiNamaDanBuku(buku,"Judul")>=0:
                                        dataPeminjam[mahaKe]["Tanggal Peminjaman"]=tgl
                                        '''Tanggal Pengembalian (Default : H+7 dari tanggal peminjaman, format :D)'''
                                        dataPeminjam[mahaKe]["Tanggal Pengembalian"]=tgl+7
                                        dataPeminjam[mahaKe]["Nama Buku yang Dipinjam"]=buku
                                        validasi("Berhasil Edit Data")
                                        break
                                    else:
                                        validasi()  
                                break
                            else:
                                validasi()  
                        break        
                    else:
                        validasi("Nama Tidak Tersedia Pada Daftar Peminjam Aktif!")
                        break
            #4 PENGEMBALIAN
            elif pilSub == '4':
                while True: #validasi nama    
                    nama = input("Masukkan Nama Peminjam: ")
                    #Menandai Index Mahasiswa
                    mahaKe = validasiNamaDanBuku(nama,"Nama Peminjam")
                    if mahaKe>=0:
                        while True: #validasi tanggal
                            tgl = input("Masukkan Tanggal Sekarang (Format Angka): ")
                            if validasiTgl(tgl):
                                tgl=int(tgl)
                                while True: 
                                    #Proses Tambah Buku
                                    buku = dataPeminjam[mahaKe]["Nama Buku yang Dipinjam"]
                                    stokKe=int(validasiNamaDanBuku(buku,"Judul"))
                                    dataBuku[stokKe]["Jumlah Buku"]+=1
                                    #Proses menghitung denda
                                    selisih = tgl-dataPeminjam[mahaKe]["Tanggal Peminjaman"]
                                    '''Jumlah kemunduran dihitung dari 
                                    total selisih tanggal pengembalian 
                                    dengan peminjaman dikurangi dengan 7'''
                                    kemunduran= selisih-7
                                    '''ketika tanggal pengembalian
                                    dikurangi tanggal peminjaman adalah >7'''
                                    if(selisih>7):
                                        '''Denda dihitung dari jumlah kemunduran
                                        pengembalian dikali dengan 500'''
                                        dataPeminjam[mahaKe]["Denda"]=kemunduran*500
                                    dataPeminjam[mahaKe]["Tanggal Pengembalian"]=tgl
                                    dataPeminjam[mahaKe]["Status"]="Kembali"
                                    dataPengembali.append(dataPeminjam[mahaKe])
                                    dataPeminjam.pop(mahaKe)
                                    validasi("Berhasil Mengembalikan")
                                    break 
                                break
                            else:
                                validasi()  
                        break        
                    else:
                        validasi("Nama Tidak Tersedia Pada Daftar Peminjam Aktif!")
                        break
            #5
            elif pilSub == '5':
                tampilPeminjam()
                while True:
                    if dataPeminjam:
                        hapusData=input("Ingin Hapus Data Ke Berapa?: ")
                        if hapusData.isdigit():
                            hapusData=int(hapusData)
                            if hapusData>=1 and hapusData<=len(dataPeminjam):
                                dataPeminjam.pop(hapusData-1)
                                break
                            else:
                                validasi()
                        else:
                            validasi()
                    else:
                        validasi("Peminjam Aktif Kosong!")
                        break
            #6
            elif pilSub == '6':
                break
            else:
                validasi()
    elif pilMain == '4':
            print(("=="*25)+"\nHistori Pengembalian Buku\n"+("=="*25))
            for i in range(len(dataPengembali)):
                print("Pengembali Ke-"+str(i+1),end=" | ")
                for y in dataPengembali[i]:
                    print(y,":",dataPengembali[i][y],end=" | ")
                print() 
    elif pilMain == '5':
        break
    else:
        validasi()
####################################################################################
