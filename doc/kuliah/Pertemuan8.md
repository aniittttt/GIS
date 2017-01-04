## Map Proxy

# Latar Belakang Masalah
Map Proxy adalah proxy open source untuk data geospasial. Cache ini mempercepat dan mengubah data dari layanan peta yang ada dan melayani setiap dekstop atau web GIS klien.

# Permasalahan dan Solusi Masalah
Map proxy berfungsi untuk melakukan caching agar semua request tidak langsung diteruskan kepada map server. Hal ini dilakukan pentingnya menjaga performansi agar load peta tidak terlalu lama. Langkah instalasi :

# yummy install python-pip python-devel
# pip install MapProxy

Buat file config map proxy direktori /var/mapproxy
# cd /var/

kebutuhan mapproxy dbutuhkan port 8080 yan dibuka dari iptables atau firewall os dengan menggunakan perintah 
# iptables -I INPUT -p tcp --dport 8080 -j ACCEPT
# service iptables save

cara melalukan konfigurasi MapProxy, yaitu :
1. Buat folder mapdata di /var pada drektori buat direktori baru dengan nama shp, mapfile, tmp dan common
2. Smpan file vektor shapefile peta didirektori /vaw/mapdata/shp (contoh file peta provinsi)
3. Edit file /var/mymapproxy/mapproxy.yml disesuaikan dengan konfigurasi data
untuk codingan lebih lengkapnya lihat di : 
https://github.com/aniittttt/SistemInformasiGeografi/blob/master/script/mapproxy.yml.txt
4. Lalu jalankan mapproxy dengan perintah
# mapproxy-util serve-develop mapproxy.yml -b 0.0.0.0
 
# Kesimpulan 
Map Proxy bersifat terbuka untuk data GIS ini

# Saran
Sebaiknya selalu diadakan praktik setiap minggu agar mahasiswa dapat lebih mengetahui tentang materi sistem geografis informasi