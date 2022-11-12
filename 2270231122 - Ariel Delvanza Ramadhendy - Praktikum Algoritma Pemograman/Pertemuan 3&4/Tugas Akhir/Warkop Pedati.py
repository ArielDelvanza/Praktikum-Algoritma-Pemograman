print("SELAMAT DATANG DI WARKOP PEDATI")
print("Masukkan Jumlah Pemesanan yang Diinginkan")
n = float(input())
while n > 0:
    n = n - 1
    print("Masukkan Nama Anda : ")
    nama = input()
    print("Masukkan Alamat Anda : ")
    alamat = input()
    print("Masukkan No. Telepon Anda : ")
    telepon = input()
    print("Masukkan Tanggal Pemesanan : ")
    tanggal = input()

    print("Pemesanan Atas Nama : " + nama)
    print("=====MENU MAKANAN : =====")
    print("1. Roti Bakar - Rp. 15.000 ")
    print("2. Mie Goreng - Rp. 9.000")
    print("3. Bubur Kacang Hijau - Rp. 10.000")
    print("Silahkan Pilih Menu Makanan! ")
    nomor = input()
    print("Silahkan Masukkan Porsi yang Diinginkan! ")
    porsi = int(input())
    if nomor == "1":
        totalmkn = porsi * 15000
        print("Total Harga Roti Bakar = " + str(totalmkn))
        mkn = "Roti Bakar"
    else:
        if nomor == "2":
            totalmkn = porsi * 9000
            print("Total Harga Mie Goreng = " + str(totalmkn))
            mkn = "Mie Goreng"
        else:
            if nomor == "3":
                totalmkn = porsi * 10000
                print("Total Harga Bubur Kacang Hijau = " + str(totalmkn))
                mkn = "Bubur Kacang Hijau"
            else:
                print("Pilihan tidak ada, silahkan masukkan ulang!!!")
    print("=====MENU MINUMAN : =====")
    print("1. Es Teh - Rp. 2.000")
    print("2. Es Jeruk - Rp. 3.500")
    print("3. Kopi - Rp. 4.000")
    print("Silahkan Pilih Menu Minuman! ")
    nmr = input()
    print("Silahkan Masukkan Jumlah Minuman yang Diinginkan! ")
    gelas = int(input())
    if nmr == "1":
        totalmnm = gelas * 2000
        print("Total Harga Es Teh = " + str(totalmnm))
        mnm = "Es Teh"
    else:
        if nmr == "2":
            totalmnm = gelas * 3500
            print("Total Harga Es Jeruk = " + str(totalmnm))
            mnm = "Es Jeruk"
        else:
            if nmr == "3":
                totalmnm = gelas * 4000
                print("Total Harga Kopi = " + str(totalmnm))
                mnm = "Kopi"
    totalsemua = totalmkn + totalmnm
    print("Total yang Harus Dibayar = " + str(totalsemua))
    print("Masukkan Uang yang Dibayarkan")
    uang = int(input())
    kembalian = uang - totalsemua
    print("Kembalian  = " + str(kembalian))
    print("========== STRUK PEMBELIAN ==========")
    print("Nama\t\t  : " + nama)
    print("Alamat\t\t  : " + alamat)
    print("No. Telepon\t  : " + telepon)
    print("Tanggal Pemesenan : " + tanggal)
    print ("Rincian Pemesanan :",porsi,mkn,"( Rp", totalmkn,")")
    print ("\t\t  :",gelas,mnm,"( Rp", totalmnm,")")
    print("Total Pembayaran  : Rp " + str(totalsemua))
    print("Dibayar\t\t  : Rp " + str(uang))
    print("Kembalian\t  : Rp " + str(kembalian))
    print("====================")

