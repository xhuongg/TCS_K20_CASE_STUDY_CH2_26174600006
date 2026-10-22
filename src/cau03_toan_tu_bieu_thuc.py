tong_phut = 135
cong_suat_w = 250

so_gio = tong_phut // 60
phut_con_lai = tong_phut % 60
print(f"Thời gian: {so_gio} giờ {phut_con_lai} phút")

bien_su_dung_lau = tong_phut > 60
print("Sử dụng lâu (>60 phút):", bien_su_dung_lau)

bien_du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Dữ liệu hợp lệ:", bien_du_lieu_hop_le)

# Biểu thức 1: 100 + 20 * 3 = 160 (nhân trước cộng sau)
# Biểu thức 2: (100 + 20) * 3 = 360 (ngoặc trước)
print("Kết quả 1:", 100 + 20 * 3)
print("Kết quả 2:", (100 + 20) * 3)