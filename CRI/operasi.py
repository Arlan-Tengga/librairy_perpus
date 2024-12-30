from . import DATABASE
from .Util import random_string
import time

def create(tahun,judul,penulis):
    data = DATABASE.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d--%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + DATABASE.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + DATABASE.TEMPLATE["judul"][len(judul):]
    data["penulis"] = judul
    data["Tahun"] = tahun

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["Tahun"]}\n'
    print(data_str)
    try:
        with open(DATABASE.DB_NAME,'w',encoding="utf-8")as file:
            file.write(data_str)

    except:
        print("Gagal boss")
        
def create_first_data():
    penulis = input("Penulis : ")
    judul = input("judul : ")
    while(True):
        try:
            tahun = int(input("tahun\t: "))
            if len(str(tahun)) == 4 :
                break
            else:
                print("Tahun harus 6 angka")

            break
        except:
            print("Tahun harus angka")
    
    
    data = DATABASE.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d--%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + DATABASE.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + DATABASE.TEMPLATE["judul"][len(judul):]
    data["penulis"] = judul
    data["Tahun"] = tahun

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["Tahun"]}\n'
    print(data_str)
    try:
        with open(DATABASE.DB_NAME,'w',encoding="utf-8")as file:
            file.write(data_str)

    except:
        print("Gagal boss")

def read():
    try:
        with open(DATABASE.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("Membaca database error")
        return False


