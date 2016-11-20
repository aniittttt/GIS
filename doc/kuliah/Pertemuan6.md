 # Create Point

## Latar Belakang Masalah 
Titik (point) meliputi semua objek geografis yang dikaitkan dengan koordinat (x,y). Satu buah objek titik memiliki satu baris dalam tabel atribut. Karakteristik-karakteristik dari titik ini dijelaskan oleh kolom-kolom yang dibentuk tabel atribut  
 
## Permasalahan dan Solusi Masalah
Contoh-contoh objek dunia nyata yang biasa dijadikan simbol titik antara lain kota, pelabuhan, bandara, rumah sakit, sekolah, dan lain-lain. Dalam skala peta yang lebih besar seperti kota dan bandara bisa saja dijadikan sebagai simbol area/luasana (polygon)

* write point
w = shapeType
w.field ('Provinsi','C','40')
w.field ('Jawa Barat','Nita')
w.record ('Jawa Barat','Nita')
w.point (10,10,0,0)
w.save('provinsi.shp')
exit() 

* Delete point
e.delete (1)

* Read Point
sf = shape
sf.records()
sf.record(0)
sf.record(1)
sf.shapes()[0].point

## Kesimpulan
Titik (point) meliputi objek geografis yang dikaitkan dengan koordinat (x,y)

## Saran 
Sebaiknya dalam menentukan titik koordinat di dalam suatu peta dibutuhkan ketelitian

