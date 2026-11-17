"""Titik masuk aplikasi Data Kosan (tahap progres: tampil di terminal, belum ada GUI)."""

import os

from kosan.services import KosService
from kosan.storage import PenyimpananCSV


def cetak(judul, data):
    """Cetak judul, lalu daftar kamar sebagai tabel teks sederhana."""
    print("\n== " + judul + " ==")
    for k in data:
        print(f"{k.nomor:<6}{k.tipe:<10}{k.harga:>10}  {k.penghuni:<16}{k.status}")


def main():
    """Muat data dari CSV, lalu tunjukkan semua fitur yang sudah jadi."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "kamar.csv")
    service = KosService(PenyimpananCSV(path).muat())

    cetak("Semua kamar", service.daftar)
    cetak("Cari 'siti'", service.cari("siti"))
    cetak("Urut harga (turun)", service.urutkan("harga", turun=True))
    cetak("Filter AC, harga maks 950000", service.filter_kamar(tipe="AC", harga_maks=950000))

    terisi = service.filter_kamar(status="Terisi")
    print("\nPendapatan per bulan: Rp", service.total_harga(*terisi))


if __name__ == "__main__":
    main()
