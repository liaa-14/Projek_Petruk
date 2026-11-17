from kosan.validasi import validasi_kamar


class Kamar:
    def __init__(self, nomor, tipe, harga, penghuni=""):
        self.nomor = str(nomor).strip()
        self.tipe = tipe
        self.harga = validasi_kamar(nomor, tipe, harga)
        self.penghuni = str(penghuni).strip()

    @property
    def status(self):
        if self.penghuni != "":
            return "Terisi"
        return "Kosong"


class KosService:
    def __init__(self, daftar=None):
        if daftar is None:
            self.daftar = []
        else:
            self.daftar = daftar

    def cari_nomor(self, nomor):
        for kamar in self.daftar:
            if kamar.nomor == nomor:
                return kamar
        return None

    def tambah(self, kamar):
        if self.cari_nomor(kamar.nomor) is not None:
            raise ValueError("Kamar sudah ada")
        self.daftar.append(kamar)

    def cari(self, kata):
        hasil = []
        for kamar in self.daftar:
            teks = f"{kamar.nomor} {kamar.tipe} {kamar.penghuni} {kamar.status}"
            if kata.lower() in teks.lower():
                hasil.append(kamar)
        return hasil

    def urutkan(self, kolom, turun=False):
        data = list(self.daftar)
        n = len(data)

        # Bubble sort biasa tanpa lambda dan getattr
        for i in range(n):
            for j in range(n - i - 1):
                if kolom == "harga":
                    nilai1 = data[j].harga
                    nilai2 = data[j + 1].harga
                else:
                    nilai1 = data[j].nomor
                    nilai2 = data[j + 1].nomor

                if nilai1 > nilai2:
                    data[j], data[j + 1] = data[j + 1], data[j]

        if turun:
            data.reverse()
        return data

    def filter_kamar(self, **kwargs):
        hasil = []
        for kamar in self.daftar:
            # Cek setiap syarat filter yang dimasukkan
            if "tipe" in kwargs and kamar.tipe != kwargs["tipe"]:
                continue
            if "status" in kwargs and kamar.status != kwargs["status"]:
                continue
            if "harga_maks" in kwargs and kamar.harga > kwargs["harga_maks"]:
                continue
            hasil.append(kamar)
        return hasil

    def total_harga(self, *args):
        total = 0
        for kamar in args:
            total += kamar.harga
        return total