def narxlarni_ol(narx_matnlari):
    togri_narxlar = []
    for narx in narx_matnlari:
        try:
            togri_narxlar.append(int(narx))
        except ValueError:
            print(f"Noto'g'ri narx: {narx}")
    return togri_narxlar

print(narxlarni_ol(["12000", "x", "5000"]))

print(narxlarni_ol([]))