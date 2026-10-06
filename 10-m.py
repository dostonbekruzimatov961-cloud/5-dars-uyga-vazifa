def chegirmali_narxlar(narx_matnlari, chegara):
    if chegara < 0:
        raise "Chegara manfiy bo'lishi mumkin emas!"

    f_narxlar = filter(lambda narx: narx.isdigit() and int(narx)>=chegara, narx_matnlari)
    ch_narxlar = list(map(lambda narx: int(narx)-2000, f_narxlar))
    return ch_narxlar

assert chegirmali_narxlar(["9000", "10000", "15000", "x"], 10000) == [ 8000, 13000]