from collections import namedtuple 
Barang = namedtuple('Barang', ['nama_barang', 'harga_jual', 'garansi_vendor']) # mendefinisikan named tuple dengan nama barang

barang1 = Barang('keyboard', 500, True)
print(f'barang1: {barang1}')