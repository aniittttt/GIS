# Retrieve Data Geospatial

## Latar Belakang Masalah 
Data Geospatial adalah data yang mengidentifikasi lokasi geografis atau karakteristik alam yang berada dibawa atau diatas permukaan bumi. Dalam geospatial dapat digambar dalam bentuk koordinat titik, garis, area (polygon) dan segiempat (grid). Retrieve disini berfungsi untuk Me-retrieve salah satu data vektor yang ada didalam peta. 

## Penjelasan dan Solusi Masalah
Metode Retrieve mempunyai 2 data, yaitu :
1. Shp (Geometri)
Shapefile ESRI merupakan format data geospasial yang umum untuk perangkat lunak sistem informasi geografis. Sebuah shapefile biasanya terdiri dari kumpulan file seperti shp, shx, dbf dan ektensi lainnya pada sebuah nama yang sama. Shapefile digambarkan dengan geometri : titik, garis, dan luasan. Data shp yaitu shape dan shapes. 
2. Dbf (Tabel)
Dbf merupakan format file yang biasa digunakan oleh perangkat lunak database. Dbf ini berbentuk tabel. Data dbf yaitu record, records dan field. 

Type shape :
1. Point (1)
2. Polyline (3)
3. Polygon (5)

Berikut Operasi pemrograman pengambilan data geospatial
import shapefile  #memanggil library di python
sf = shapefile.Reader ("D:\GIS\provinsi\provinsi.shp") #instalasi kelas dengan constrach input file
sf.fields  #menampilkan apa saja field di dbf
sf.records()  #mengambil semua record di dbf
sf.record(0)  # mengambil salah satu record ke-2
sf.shapes()  # mengambil data geometri
sf.shape(0) # mengambil data geometri

## Kesimpulan 
Retrieve pada data geospatial berfungsi untuk Me-retrieve salah satu data vektor yang ada didalam sebuah peta

## Saran
Untuk Me-retrieve salah satu data yang ada didalam geospatial ditentukan terlebih dahulu data apa yang akan diretrieve didalam peta 

## Daftar Pustaka :
[1] bakosurtanal.go.id/perpres/artikel/RUU%20IG/RUU%20IG%20FOR%20DPR.pdf <br>
[2] https://id.wikipedia.org/wiki/Shapefile <br>
[3] https://pypi.python.org/pypi/pyshp/1.2.0 <br> 

## Scan Plagiarisme
https://drive.google.com/file/d/0B3mytGJbyhIhUWRuZXVQcU82YTA/view
