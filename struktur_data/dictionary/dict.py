import json
data = {
    'nama' : 'ahmad',
    'kelas' : 'TI14',
    'nim' : '0110221238',
    'hobi' : ['ngoding', 'membaca'],
    'uts' : 90,
    'uas' : 88
}

data_tambahan = {
    'bidang minat' : 'statistic',
    'bahasa pemrograman' : "JAVA"
}

print(f"data siswa {data.get('nama', 'data tidak ditemukan')}")


# # EKSTRASI
# daftar_kunci = data.keys()
# print(f"kumpulan keys dari data:  {daftar_kunci}" )

# print("\n----------\n")
# for kunci in daftar_kunci:
#     print(kunci)

# print("\n----------\n")

# daftar_nilai = data.values()
# for nilai in daftar_nilai:
#     print(nilai)

# print("\n----------\n")
# daftar_kunci_nilai = data.items()

# for k, v in daftar_kunci_nilai:
#     print(f'{k} : {v}')

# # mengubah dictionary
# data['uas'] = 100
# print("\n----------\n")
# for k, v in daftar_kunci_nilai:
#     print(f'{k} : {v}')

# # menambah data
# data['gender'] = 'LAKI-LAKI'
# print("\n----------\n")
# for k, v in daftar_kunci_nilai:
#     print(f'{k} : {v}')

# # update data
# data.update({'nama' :  "Ahmad Ihsanullah Rabbani",'Program Studi' : "Sistem Informasi"})
# print("\n----------\n")
# for k, v in daftar_kunci_nilai:
#     print(f'{k} : {v}')

# # menghapus data -> pop()
# data_pop = data.pop('alamat', 'tidak ditemukan datanya');
# print("\n----------\n")
# for k, v in daftar_kunci_nilai:
#     print(f'{k} : {v}')
# print(f'data hasil pop: {data_pop}')

# concatenation
data_gabungan = {**data, **data_tambahan};
print(f'data gabungan : {data_gabungan}')

# JSON, mekanisme dumping
with open('fileku.json', 'w') as fileku:
    json.dump(data_gabungan, fileku)

# read json