def validasi_kamar(nomor, tipe, harga):
    # Cek nomor kamar tidak boleh kosong
    if not str(nomor).strip():
        raise ValueError("Nomor kamar wajib diisi")

    # Cek tipe kamar harus Standar atau AC
    if tipe not in ["Standar", "AC"]:
        raise ValueError("Tipe harus Standar atau AC")

    # Ubah harga ke angka dan pastikan tidak minus
    try:
        harga = int(harga)
    except:
        raise ValueError("Harga harus berupa angka")

    if harga < 0:
        raise ValueError("Harga tidak boleh negatif")

    return harga