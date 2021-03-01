# Topological Sort ~~~ Decrease and Conquer

**TopSort for prerequisite problem** 

Muhammad Fikri. N \
13519069 \
K02 

## Description
Program ini digunakan untuk menyusun rencana pengambilan matkul.  \
Program membaca input berupa file eksternal dengan ekstensi .txt  \
yang sudah ada pada folder test. Kemudian, output nya akan tersimpan \
pada file dengan format <NamaFile_input>_sol.txt. 

Representasi graf pada program ini menggunakan dictionary. \
dictionary tersebut memiliki key = matkul dan value yang \
berbentuk dictionary juga. Dictionary value memiliki dua key \
yaitu N_preq yaitu banyaknya prerequisite yang blm diambil dan \
Arr_preq yaitu array yang berisi informasi prerequisite matkul tersebut \
Pendekatan algoritma decrease and conquer pada program ini adalah \
dengan penghapusan vertex yang telah diambil (matkul) dan pengurangan \
N_preq atau N_masuk jika berhubungan dengan vertex yang dihapus tadi. \
Varian decrease and conquer yang digunakan pada topological sort adalah \
decrease by a constant

## Requirements
install python dan pastikan dapat dijalankan

## How to run
<b>clone repository </b>
```
https://github.com/mfikrin/TopSort.git
```
Atau\
Download zip pada repository ini kemudian ekstrak

Setelah itu, Jalankan terminal (cmd)\
Pastikan sudah berada di folder "TopSort" jika belum silahkan\
change directory menggunakan perintah "cd" (tanpa tanda kutip).\
Lalu, pada cmd ketik (masukkan perintah)

```
cd src
python 13519069_main.py
```
Kemudian, akan diperoleh tampilan kurang lebih seperti ini.
```
              ________  .__                   .___
               \_____  \ |  |   ____  ____   __| _/____ ___  ___
                /   |   \|  | _/ ___\/  _ \ / __ |/ __ \\  \/  /
               /    |    \  |_\  \__(  <_> ) /_/ \  ___/ >    <
               \_______  /____/\___  >____/\____ |\___  /__/\_ \
                       \/          \/           \/    \/      \/

-----------------------------
|  Silahkan input nama file |
|        (eg : tc)          |
|   (Tanpa ekstensi file)   |
-----------------------------

Input nama file :
```

 <b> Enjoy !!! </b>
