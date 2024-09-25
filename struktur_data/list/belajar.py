listku = [20, 10, 10, 80, 40, 60, 10, 20] # memungkinkan duplikasi
print(f'listku: {listku}')
# print(f'slicing: {listku[:5]}')
# print(f'slicing: {listku[5:]}')
print(f'slicing: {listku[2:5:2]}')
# slicing[startindex: endindex(pembatas): lompatan ]

listku[0]= 'berubah';
print(listku)
listku.append("baru")
print(listku)

listmu = ['halo', 10, 10.9, True, [10, 5]];
print(f'listmu: {listmu[-2]}')

def siswa(nama, usia):
    print(f"halo nama aku {nama} {usia} tahun")

def hello():
    nama = "udin"
    usia = 19
    siswa(nama, usia);
    print('halo bro')

hello()

gabung_list = listku + listmu;
print(gabung_list)