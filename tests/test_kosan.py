import unittest
from kosan.services import Kamar, KosService
from kosan.storage import PenyimpananCSV


class UjiKosan(unittest.TestCase):
    def setUp(self):
        # Siapkan 3 data kamar contoh sebelum setiap tes dijalankan
        self.layanan = KosService([
            Kamar("101", "Standar", 600000, "Budi"),
            Kamar("102", "AC", 900000),
            Kamar("103", "AC", 800000, "Siti"),
        ])

    def test_validasi_kamar(self):
        # Cek harga minus harus gagal
        with self.assertRaises(ValueError):
            Kamar("104", "AC", -1)

        # Cek nomor kamar kembar harus gagal
        with self.assertRaises(ValueError):
            self.layanan.tambah(Kamar("101", "AC", 700000))

    def test_cari_dan_urut(self):
        # Cek fitur pencarian
        hasil_cari = self.layanan.cari("siti")
        self.assertEqual(len(hasil_cari), 1)
        self.assertEqual(hasil_cari[0].nomor, "103")

        # Cek pengurutan dari harga termurah ke termahal
        hasil_urut = self.layanan.urutkan("harga")
        self.assertEqual(hasil_urut[0].harga, 600000)
        self.assertEqual(hasil_urut[-1].harga, 900000)

    def test_filter_dan_total(self):
        # Cek filter kamar (**kwargs)
        hasil_filter = self.layanan.filter_kamar(tipe="AC", harga_maks=850000)
        self.assertEqual(hasil_filter[0].nomor, "103")

        # Cek hitung total harga kamar terisi (*args)
        kamar_terisi = self.layanan.filter_kamar(status="Terisi")
        self.assertEqual(self.layanan.total_harga(*kamar_terisi), 1400000)

    def test_simpan_dan_baca_csv(self):
        penyimpanan = PenyimpananCSV("tes_kamar.csv")

        # Simpan data lalu baca kembali untuk memastikan jumlahnya 3
        penyimpanan.simpan(self.layanan.daftar)
        self.assertEqual(len(penyimpanan.muat()), 3)


if __name__ == "__main__":
    unittest.main()