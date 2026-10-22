cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Điện năng (kWh):", dien_nang_kwh, "Kiểu:", type(dien_nang_kwh))
print("Chi phí (VND):", chi_phi, "Kiểu:", type(chi_phi))

# Thay so_phut = 60
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Khi số phút là 60 -> Điện năng:", dien_nang_kwh, "| Chi phí:", chi_phi)