# creditscore-analytic-model-dev
Menggunakan dataset credit score yang memiliki tujuan apakah seseorang terlambat (1) atau tidak (0) dalam membayar kredit.

## Yang dibutuhkan:

### 1. Postman [download](https://www.getpostman.com/downloads/) <br>
Terdapat pilihan juga untuk mac dan ubuntu. <br>

## Tata cara melakukan pengujian menggunakan Postman

### 1. Menginstall Postman
Link download ada diatas, untuk OS windows cukup memilih tombol Windows **(32 bit/64 bit sesuai pc anda)**, untuk Mac ataupun Ubuntu dapat memilih dibawahnya.

(Gambar1)

### 2. Membuat akun terlebih dahulu dan Login
Dapat membuat akun seperti biasa, ataupun dengan akun email google.

### 3. Ganti METHOD dengan POST
Tujuannya adalah kita mencoba untuk memberikan inputan nilai, lalu didaptkan hasil prediksi dari model yang kita buat.

(Gambar2)

### 4. Isikan 'Request URL'
Isikan kolom request URL menggunakan **nostartama.pythonanywhere.com/api** sebagai website yang nantinya akan kita gunakan.

(Gambar3)

### 5. Ganti sub-pilihan ke **Body** dan **raw**
(Gambar4)

Bertujuan untuk mengganti dari 'Params' (yang berisikan parameter) ke 'Body' (yang berisikan kode API).

(Gambar42)

### 6. Mengisi baris menggunakan aturan pada inputan di POSTMAN

Bertujuan untuk mengatur inputan yang kita sediakan.

Sebelumnya, berikut penjelasan variabel yang kita digunakan:

> * 'LIMIT_BAL': Batas maksimal kredit
> * "AGE": Usia
> *	"BILL_AMT1": Tagihan kredit bulan ke-1 (kontinyu)
> * "PAY_AMT1": Kredit yang dibayarkan bulan ke-1 (kontinyu)
> *	"PAY_1_2": Tepat waktu atau tidak (bln 1)? - 0: Tepat waktu / 1: Terlambat
> *	"BILL_AMT2": Tagihan kredit bulan ke-2 (kontinyu)
> *	"PAY_AMT2": dibayarkan bulan ke-2 (kontinyu)
> *	"PAY_2_2": Tepat waktu atau tidak (bln 2)? - 0: Tepat waktu / 1: Terlambat
> *	"BILL_AMT3": Tagihan kredit bulan ke-3 (kontinyu)
> *	"PAY_AMT3": dibayarkan bulan ke-3 (kontinyu)
> *	"PAY_3_2": Tepat waktu atau tidak (bln 3)? - 0: Tepat waktu / 1: Terlambat
> * "EDUCATION_2": Diploma/S1 atau tidak? - 0: Tepat waktu / 1: Terlambat
> *	"EDUCATION_3": SMA atau tidak? - 0: Tepat waktu / 1: Terlambat

Isikan dengan:

{
	"LIMIT_BAL": "{{LIMIT_BAL}}",
	"AGE":"{{AGE}}",
	"BILL_AMT1":"{{BILL_AMT1}}",
	"PAY_AMT1":"{{PAY_AMT1}}",
	"PAY_1_2":"{{PAY_1_2}}",
	"BILL_AMT2":"{{BILL_AMT2}}",
	"PAY_AMT2":"{{PAY_AMT2}}",
	"PAY_2_2":"{{PAY_2_2}}",
	"BILL_AMT3":"{{BILL_AMT3}}",
	"PAY_AMT3":"{{PAY_AMT3}}",
	"PAY_3_2":"{{PAY_3_2}}",
	"EDUCATION_2":"{{EDUCATION_2}}",
	"EDUCATION_3":"{{EDUCATION_3}}"
}

Tujuannya adalah ketika kita memasukkan banyak pengujian, tidak terjadi error (fitur pengulangan pada POSTMAN). Untuk data yang digunakan akan dijelaskan nanti. Contoh penulisannya pada baris kode:

(Gambar 5)

### 7. Simpan dan Masukkan kedalam Folder

Simpan hasil yang sudah kita buat sebelumnya, klik tombol *save* pada lingkaran yang sudah ditandai.

(Gambar 6)

Selanjutnya akan muncul tampilan seperti dibawah, tidak dapat disimpan bukan? Itu dikarenakan harus membuat folder terlebih dahulu. Caranya dengan klik '+Create Collection' (Gambar Bawah 1) -> Lalu pilih folder tersebut (Gambar Bawah 2)

(Gambar 7)

(Gambar 8)

### 9. Membuat Inputan / Membuat file JSON (opsional/hanya untuk banyak data)

### 10. Isikan input sesuai variabel yang dibuat saat Machine Learning

Berikut variabel yang disediakan untuk diberi nilai sesuai keinginan:

### 11. Pilih 'Runner' (opsional/hanya untuk banyak data) 

Pilih Tab 'Runner' untuk menjalankan program. 

(Gambar 10)



### 12. Contoh Hasil Runner (opsional/hanya untuk banyak data)

Berikut hasil dari runner yang sudah dijalankan, untuk lebih jelasnya ada pada hasil_11data.json

(Gambar 11)






