# Shapefile

## Latar Belakang Masalah
Shapefile adalah format data geospasial yang umum untuk perangkat lunak sistem informasi geografis. Sebuah shapefile biasanya terdiri dari kumpulan file yang berekstensi  shp, shx, dbf, dan ekstensi lainnya pada sebuah nama yang sama. Shapefile keruangan digambaran dengan geometri  : titik, garis dan luas.

## Permasalahan dan Solusi Masalah
 Pyshp dapat membuat salah satu file komponen seperti shp atau dbf file yang tanpa menulis yang lain. Beberapa sostem GIS berbasis web menggunakan shp-uploap untuk menentukan daerah tujuan.

 Setting Type SHP ada 3 yaitu : point, polyline dan polygon
import shapefile
w = shapefile.Writer(shapeType=1)
w.shapeType
import shapefile
w = shapefile.Writer(shapeType=3)
w.shapeType

 Menambahkan record ke 1 yaitu point (x,y) atau (122,37) dimana x dan y adalah koordinat langitude dan longitude (122,37,0,0)
w = shapefile.Writer()
w.point(122,37)
w.shapes()[0].points
[[122, 37, 0, 0]]

Polygon shapefile harus memiliki minimal 4 poin dan 4 titik terakhir harus sama seperti yang pertama. PySHP otomatis akan melakukan polygon tertutup. Semua garis harus memiliki dua titik. Ini yang disamakan antara dua jenis yang disebut "poli" 
w = shapefile.Write()
w.poly(shapeType=3, parts=[[[122,37,4,9], [117,36,3,4]], [[115,32,8,8], [118,20,6,4], [113,24]]])

Dbf (tabel identitas geometri) field untuk membantu atribut tabel
w = shapefile.Writer()
w.field('Provinsi','C','2')

## Kesimpulan
Shapefile adalah data geospasial yang terdiri dari kumpulan file seperti shp dan dbf dalam materi pertemuan 5 

 ## Saran
Sebaiknya agar lebih mengerti lagi tentang Shapefile menggunakan Python dibutuhkan praktikum dalam mata kuliah GIS ini