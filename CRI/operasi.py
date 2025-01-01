from . import DATABASE
from .Util import random_string
import time

def update(no_buku,pk,data_add,tahun,judul,penulis):
    data = DATABASE.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + DATABASE.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + DATABASE.TEMPLATE["judul"][len(judul):]
    data["penulis"] = judul
    data["Tahun"] = tahun

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["Tahun"]}\n'
    panjang_data = len(data_str)

    try:
        with(open(DATABASE.DB_NAME,'r+',encoding="utf-8"))as file :
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("erorr bosss")



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

def read(**kwargs):
    try:
        with open(DATABASE.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else :
                    return content[index_buku]
            else :
                return content
    except:
        print("Membaca database error")
        return False



