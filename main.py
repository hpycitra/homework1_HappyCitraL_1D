print('PEKERJA FREELANCE')
nama_pekerja = str (input('Masukkan Nama :'))
pendidikan = str (input('Masukkan Pendidikan Anda :'))
usia = int(input('Masukkan Usia :'))
jenis_kelamin = str (input('Masukkan Jenis Kelamin :'))
tinggi_badan = float(input('Masukkan Tinggi Badan :'))
berat_badan = float(input('Masukkan Berat Badan :'))
status = str(input('Masukkan Status Anda (Sudah Menikah/Belum Menikah):')) 
if usia > 17 and tinggi_badan > 155 and berat_badan > 45 and status == 'Belum Menikah' :
 hasil = 'Selamat Anda di terima freelance harian dan mengikuti training terlebih dahulu'
else: 
    hasil = ' Maaf anda tidak di terima'
print(hasil)


