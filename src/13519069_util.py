'''
Author  : Muhammad Fikri. N
NIM     : 13519069
Topik   : Topological Sort
'''

# Untuk menghapus string kosong
def delete_arr_empty(arr):
    while ("" in arr):
        arr.remove("")
    return arr

# Untuk menghapus elemen arr / matkul (berisi matkul beserta prereq) yang telah diambil (arrTakes)
def delete_arr(arr,arrTakes):
    while (len(arrTakes) > 0):
        for content in arr:
            course = content[0]
            for take in arrTakes:
                if course == take:
                    arr.remove(content)
                    arrTakes.remove(take)
    return arr

# Untuk menghapus record dictionary yang memiliki kunci = key
def delete_dict(dict,key):
    for course in dict.keys():
        if course == key:
            dict.pop(key)
            return dict

# Untuk mengurangi banyaknya prerequisite yang blm diambil
def minus_Npreq(dict,arrTakes):
    for course, info_course in dict.items():
        for take in arrTakes:
            if take in info_course['Arr_preq']:
                info_course["N_preq"] -= 1

# Untuk mengetahui apakah ada matkul yang banyak prerequisite yang blm diambil = 0
def is_Npreq_have_zero(dict):
    return any(info_course["N_preq"] == 0 for course, info_course in dict.items())

# Untuk convert array to string
def arrayToString(arr):
    string = ""
    for i in range(len(arr)):
        if (i < (len(arr)-1)):
            string += arr[i]
            string += ", "
        else:
            string += arr[i]
            string += "."
    return string
