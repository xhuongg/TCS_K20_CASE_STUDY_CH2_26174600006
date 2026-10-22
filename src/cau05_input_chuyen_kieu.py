ma_may = input("Nhập mã máy: ")
cong_suat_str = input("Nhập công suất W: ")
so_phut_str = input("Nhập số phút: ")
don_gia_str = input("Nhập đơn giá: ")

print("Type ban đầu:", type(ma_may), type(cong_suat_str), type(so_phut_str), type(don_gia_str))

# Chuyển kiểu
cong_suat_w = float(cong_suat_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_str)

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print(f"Điện năng: {dien_nang_kwh} kWh")
print(f"Chi phí: {chi_phi} VND")
