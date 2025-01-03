from .import operasi

def delete_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor buku yang akan di delete ")
        no_buku = int(input("Masukkan nomor buku : "))
        data_buku = operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4]

            print("\n"+"="*100)
            print("Data yang ingin anda Hapus")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            is_done = input("Apakah anda yakin (y/n)? ")
            if is_done == "y" or is_done == "Y":
                operasi.delete(no_buku)
                break
        else:
            print("nomor tidak valid, silahkan masukan lagi")

    print("Data berhasil di hapus")
        

    while(True):
        print("\n"+"="*100)
        print("Silahkan pilih data yakin ingin mngubahnya? ")
        print(f"1. judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        is_done = input("Apakah Sudah selesai (y/n): ")
        if is_done == "y" or is_done == "Y" :
            break

def update_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor buku yang akan di update")
        no_buku = int(input("Masukkan nomor buku : "))
        data_buku = operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("nomor tidak valid,silahkan masukkan lagi")
    
    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while(True):
        print("\n"+"="*100)
        print("Silahkan pilih data yang anda ingin anda ubah")
        print(f"1. judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        user_option = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul = input("judul\t: ")
            case "2": penulis = input("penulis\t: ")
            case "3":
                while(True):
                    try :
                        tahun = int(input("tahun\t:"))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("masukkan angka dan yyyy")
                    except :
                        print("masukkan format angka dan yyyy")
        
        is_done = input("Apakah Sudah selesai (y/n): ")
        if is_done == "y" or is_done == "Y" :
            break
    operasi.update(no_buku,pk,data_add,tahun,judul,penulis)


def read_console():
    data_file = operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end = "")

    # Footer
    print("="*100+"\n")
