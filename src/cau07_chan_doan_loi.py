# Đoạn mã đã được sửa lỗi:
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))  # Sửa: Chuyển sang float/int để thực hiện phép toán số học
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000

print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")  # Sửa: Đổi tên biến dien_nang -> dien_nang_kwh và đóng ngoặc đơn

# Lỗi 1: TypeError - cong_suat_w chưa chuyển từ str sang số nên không dùng phép chia / được.
# Lỗi 2: NameError - biến 'dien_nang' chưa được định nghĩa (tên đúng là 'dien_nang_kwh').
# Lỗi 3: SyntaxError - thiếu dấu đóng ngoặc ')' ở cuối dòng print.
