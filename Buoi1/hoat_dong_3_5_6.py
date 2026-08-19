# HOẠT ĐỘNG 3
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2

MUC_LUONG_TOI_THIEU = 5000000

print("Tên sinh viên:", ten)
print("Điểm Toán:", diem_toan)
print("Điểm Văn:", diem_van)
print("Số lượng môn học:", so_luong_mon_hoc)
print("Mức lương tối thiểu:", MUC_LUONG_TOI_THIEU)
# HOẠT ĐỘNG 5
print("\nBài tập 5.1:")
a = 17
b = 5

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

print("\nBài tập 5.2:")
diem = 6.5
tuoi = 20
diem_kha = (diem >= 6.5) and (diem < 8.0)
print("Điểm có đạt loại Khá không?", diem_kha)

tuoi_dac_biet = (tuoi < 18) or (tuoi > 60)
print("Tuổi chưa đủ 18 hoặc trên 60?", tuoi_dac_biet)

phu_dinh_tuoi = not tuoi_dac_biet
print("Phủ định lại điều kiện tuổi:", phu_dinh_tuoi)

print("\nBài tập 5.3:")
x = 10
x += 5
print("Sau x += 5, x =", x)
x -= 5
print("Sau x -= 5, x =", x)
x *= 2
print("Sau x *= 2, x =", x)
x /= 4
print("Sau x /= 4, x =", x)
x //= 2
print("Sau x //= 2, x =", x)
x **= 3
print("Sau x **= 3, x =", x)

danh_sach = [1, 2, 3, "python"]
kiem_tra_in = 3 in danh_sach
print("3 có trong danh_sach không?", kiem_tra_in)

list_khac = danh_sach
kiem_tra_is = danh_sach is list_khac
print("Hai biến có cùng tham chiếu không?", kiem_tra_is)

print("\nBài tập 5.4:")
print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)

# HOẠT ĐỘNG 6
print("\nBài tập 6.1:")
bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))

print("\nBài tập 6.2:")
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0
dtb = (diem_toan + diem_ly + diem_hoa) / 3
la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0
print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)

print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))