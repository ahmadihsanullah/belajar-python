# gabungan
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3 = {5,6,7,8}

# Gabungan dari beberapa set berarti mengumpulkan semua elemen dari setiap set tanpa ada yang terduplikasi.
set_gabungan = set1.union(set2, set3)
print(f'hasil gabungan: {set_gabungan}')

# irisan set atau intersection 
# irisan berarti mencari elemen yang sama di semua set.
# menghasilkan set baru
set_irisan = set1.intersection(set2, set3)
print(f'irisan set: {set_irisan}')

# operasi selisih atau difference
# Selisih adalah mencari elemen yang ada di satu set, tetapi tidak ada di set lainnya.
# menghasilkan set baru, yg tidak ketemu di set lainnya
set_selisih = set2.difference(set1, set3)
# data yang ada di set2 dan terdapat di set 1 maka akan di eliminir => (3,4)
# data yang ada di set2 dan terdapat di set 3 maka akan di eliminir => (5, 6)
print(f'set selisih: {set_selisih}')

# simmetical difference
# Beda setangkup mencari elemen yang hanya ada di salah satu set, tetapi tidak ada di kedua set sekaligus.
beda_setangku = set1.symmetric_difference(set2)
print(f'beda setangku: {beda_setangku}')
