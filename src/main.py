'''
Author  : Muhammad Fikri. N
NIM     : 13519069
Topik   : Topological Sort
'''

import util as ut

filename = input("Masukkan nama file (eg : tc) (Tanpa ekstensi file) : ")
test = open("../test/" + filename + ".txt", 'r')
temp = test.read().splitlines() # baca file teks (dengan readlines yang sekaligus hapus \n)

# delete string kosong (ketika file .txt memiliki banyak enter tp tidak ada record)
ut.delete_arr_empty(temp)

temps = []

for i in range(len(temp)):
    elm = temp[i].replace('.',"")
    elm = elm.replace(" ","")
    temps.append(elm)

arr = []

for i in range(len(temps)):
    # mengubah array of string menjadi array of array string dgn delimiter koma (,)
    content = temps[i].split(',')

    arr.append(content)

dict = {}

for i in range(len(arr)):
    N_preq = (len(arr[i][1:len(arr[i])]))
    Arr_preq = (arr[i][1:len(arr[i])])
    dict[arr[i][0]] = {
        "N_preq": N_preq,
        "Arr_preq": Arr_preq
    }

semester = [[]for i in range(40)] # Asumsi maksimal 40 semester yang dapat ditampung

temporary = []
i = -1
if ut.is_Npreq_have_zero(dict):
    while (dict != {} and ut.is_Npreq_have_zero(dict)):
        i += 1
        print("print i woiiii : " + str(i))

        # untuk mengulang array temporary kembali kosong (berisi matkul yang diambil)
        temporary = []

        for content in arr:
            if dict[content[0]]["N_preq"] == 0:
                take = content[0]
                semester[i].append(take)
                temporary.append(take)

                # Menghapus course yang telah diambil pada dict
                ut.delete_dict(dict,take)

        ut.minus_Npreq(dict,temporary)
        ut.delete_arr(arr,temporary)

else:
    print("Tidak ada urutan yang mungkin")
    print("Pastikan kuliah dan prerequisite nya berupa Directed Acyclic Graph (DAG)")

semester = [x for x in semester if x] #

if len(semester) <= 8:
    for i in range(len(semester)):
        print("Semester " + str(i+1) + ": ", end ="")
        print(ut.arrayToString(semester[i]))

else:
    print("Hasil proses melebihi 8 semester !!!")
    print("Tidak boleh melebihi 8 semester :(")
    print("Apakah tetap akan ditampilkan atau tidak perlu ?")
    print("-----------------------------")
    print("|         Opsi input        |")
    print("|       1. YA               |")
    print("|       2. TIDAK            |")
    print("-----------------------------")

    pil = int(input("Input pilihan : "))
    while (pil != 1 or pil != 2):
        pil = int(input("Ulangi input pilihan, pastikan pilihan 1 atau 2 : "))
    if pil == 1:
        for i in range(len(semester)):
            print("Semester " + str(i + 1) + ": ", end="")
            print(ut.arrayToString(semester[i]))
        print("Jangan lupa atur pilihan matkul kamu lagi, FIGHTING (～￣▽￣)～")
    else:
        print("Silahkan atur pilihan matkul kamu lagi, FIGHTING (～￣▽￣)～")


