'''
Author  : Muhammad Fikri. N
NIM     : 13519069
Topik   : Topological Sort
'''
import os
ut = __import__('13519069_util')

print("              ________  .__                   .___             ")
print("               \_____  \ |  |   ____  ____   __| _/____ ___  ___")
print("                /   |   \|  | _/ ___\/  _ \ / __ |/ __ \\\  \/  /")
print("               /    |    \  |_\  \__(  <_> ) /_/ \  ___/ >    < ")
print("               \_______  /____/\___  >____/\____ |\___  /__/\_ \\")
print("                       \/          \/           \/    \/      \/\n")

print("-----------------------------")
print("|  Silahkan input nama file |")
print("|        (eg : tc)          |")
print("|   (Tanpa ekstensi file)   |")
print("-----------------------------")

print()

filename = input("Input nama file : ")
path = "../test/" + filename + ".txt"

isfile = os.path.isfile(path)

# Melakukan pengecekan apakah filename terdapat pada folder test atau tidak
while (not isfile):
    filename = input("Ulangi input nama file : ")
    path = "../test/" + filename + ".txt"
    isfile = os.path.isfile(path)

test = open(path, 'r')

temp = test.read().splitlines()  # baca file teks (dengan readlines yang sekaligus hapus \n)

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
    N_preq = (len(arr[i][1:len(arr[i])])) # N_preq adalah banyaknya prerequisite yang blm diambil
    Arr_preq = (arr[i][1:len(arr[i])])
    dict[arr[i][0]] = {                 # Key = Matkul
        "N_preq": N_preq,               # Value = dictionary (key1 = N_preq (banyak prerequisite yang blm diambil)
        "Arr_preq": Arr_preq            # key2 = Arr_preq (array dari matkul prerequisite))
    }

semester = [[]for i in range(40)] # Asumsi maksimal 40 semester yang dapat ditampung

temporary = []
i = -1

print()
print("-----------------------------")
print("|      Hasilnya adalah      |")
print("|        ↓ ↓ ↓ ↓ ↓ ↓        |")
print("-----------------------------")
print()

name_output = filename + "_sol.txt"
outfile = open("../test/solution/" + name_output, 'w')

if ut.is_Npreq_have_zero(dict):
    while (dict != {} and ut.is_Npreq_have_zero(dict)):
        i += 1

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

semester = [x for x in semester if x] # Untuk menghapus empty array dari sebuah array

if len(semester) <= 8:
    if (dict == {}):
        for i in range(len(semester)):
            print("Semester " + str(i+1) + ": ", end ="")
            outfile.write("Semester " + str(i+1) + ": ")
            print(ut.arrayToString(semester[i]))
            outfile.write(ut.arrayToString(semester[i]))
            outfile.write("\n")
    elif (not ut.is_Npreq_have_zero(dict)):
        for i in range(len(semester)):
            print("Semester " + str(i+1) + ": ", end ="")
            outfile.write("Semester " + str(i + 1) + ": ")
            print(ut.arrayToString(semester[i]))
            outfile.write(ut.arrayToString(semester[i]))
            outfile.write("\n")
        print("Tidak ada urutan yang mungkin lagi")
        outfile.write("Tidak ada urutan yang mungkin lagi\n")
        print("Pastikan kuliah dan prerequisite nya berupa Directed Acyclic Graph (DAG)")
        outfile.write("Pastikan kuliah dan prerequisite nya berupa Directed Acyclic Graph (DAG)\n")
        print("Silahkan atur pilihan matkul kamu lagi, FIGHTING (～￣▽￣)～")
        outfile.write("Silahkan atur pilihan matkul kamu lagi, FIGHTING ^_^")


else:
    print("Hasil proses melebihi 8 semester !!!")
    outfile.write("Hasil proses melebihi 8 semester !!!\n")
    print("Tidak boleh melebihi 8 semester :(")
    outfile.write("Tidak boleh melebihi 8 semester :(\n")
    print("Apakah tetap akan ditampilkan atau tidak perlu ?")
    print("-----------------------------")
    print("|         Opsi input        |")
    print("|       1. YA               |")
    print("|       2. TIDAK            |")
    print("-----------------------------")

    pil = int(input("Input pilihan : "))
    while (pil != 1 and pil != 2):
        pil = int(input("Ulangi input pilihan, pastikan pilihan 1 atau 2 : "))
    if pil == 1:
        for i in range(len(semester)):
            print("Semester " + str(i + 1) + ": ", end="")
            outfile.write("Semester " + str(i + 1) + ": ")
            print(ut.arrayToString(semester[i]))
            outfile.write(ut.arrayToString(semester[i]))
            outfile.write("\n")
        print("\nJangan lupa atur pilihan matkul kamu lagi, FIGHTING (～￣▽￣)～")
        outfile.write("\nJangan lupa atur pilihan matkul kamu lagi, FIGHTING ^_^")
    else:
        print("\nSilahkan atur pilihan matkul kamu lagi, FIGHTING (～￣▽￣)～")
        outfile.write("\nSilahkan atur pilihan matkul kamu lagi, FIGHTING ^_^")


