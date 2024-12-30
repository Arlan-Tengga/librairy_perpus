import os
import CRI as CRI

if __name__ == "__main__":
    sistem_operasi = os.name

    #check data base ada atau tidak

    match sistem_operasi:
        case "ponix" : os.system("clear")
        case "nt" : os.system("cls")
    
    print("SELAMAT DATANG")
    print("DI PERPUSTAKAAN BERSAMA")
    print("=======================")

    CRI.init_console()

    while(True):
        match sistem_operasi:
            case "ponix" : os.system("clear")
            case "nt" : os.system("cls")
    
        print("SELAMAT DATANG")
        print("DI PERPUSTAKAAN BERSAMA")
        print("=======================")

        print(f"1.  Read Data")
        print(f"2.  Create Data")
        print(f"3.  Update Data")
        print(f"4.  Deleta Data\n")

        user_option = input("masukkan opsi: ")

        match user_option :
            case "1": CRI.read_console()
            case "2": CRI.create_console()
            case "3": CRI.update_console()
            case "4": print("Deleta Data")
        
        print("=======================")
        
        is_done = input("Apakah Sudah Selesai (y/n)?  ")
        if is_done == "y" or is_done =="Y":
            break

    print("Selesai!")