from kosan.services import Kamar

class PenyimpananCSV:
    def __init__(self, nama_file):
        self.nama_file = nama_file

    def muat(self):
        daftar_kamar = []
        try:
            with open(self.nama_file, "r") as file:
                baris_semua = file.readlines()

                # Mulai dari baris ke-2 (index 1) supaya judul kolom dilewati
                for baris in baris_semua[1:]:
                    data = baris.strip().split(",")
                    try:
                        kamar = Kamar(data[0], data[1], data[2], data[3])
                        daftar_kamar.append(kamar)
                    except:
                        pass  # Kalau baris kosong/rusak, lewati saja
        except:
            # Kalau file belum ada, bikin file baru yang masih kosong
            self.simpan([])

        return daftar_kamar

    def simpan(self, daftar_kamar):
        with open(self.nama_file, "w") as file:
            # Tulis judul kolom paling atas
            file.write("nomor,tipe,harga,penghuni\n")

            # Tulis data tiap kamar ke baris bawahnya pakai koma biasa
            for k in daftar_kamar:
                file.write(f"{k.nomor},{k.tipe},{k.harga},{k.penghuni}\n")