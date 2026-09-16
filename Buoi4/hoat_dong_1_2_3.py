#Hoạt động1
#Bài 1.1
sinh_vien = {
"ho_ten": "Nguyen Van A",
"nam_sinh": 2004,
"diem_tb": 8.5
}
print(sinh_vien["ho_ten"]) # truy xuat theo khoa
print(sinh_vien.get("diem_tb")) # truy xuat an toan bang get()
print(sinh_vien.get("lop", "Chua co")) # get() voi gia tri mac dinh neu khong co khoa
#Bài 1.2
sinh_vien["lop"] = "CNTT01" # them khoa moi
sinh_vien["diem_tb"] = 9.0 # sua gia tri khoa da co
print(sinh_vien)
diem_cu = sinh_vien.pop("diem_tb") # xoa theo khoa, tra ve gia tri vua xoa

print(sinh_vien, "- diem da xoa:", diem_cu)
sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"}) # cap nhat/them nhieu khoa cung luc
print(sinh_vien)
# Hoạt động 2
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}
for mon in diem_mon_hoc.keys():
    print(mon)
for diem in diem_mon_hoc.values():
    print(diem)
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")
tong_diem = 0
for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem
print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))
# Hoạt động 3
# Bài 3.1
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}
diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()}
print(diem_cong_diem)
ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()}
print(ten_mon_viet_hoa)
# Bài 3.2
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}
print(mon_hoc_ky1 & mon_hoc_ky2) # giao: mon hoc chung 2 hoc ky
print(mon_hoc_ky1 | mon_hoc_ky2) # hop: tat ca mon hoc ca 2 hoc ky

print(mon_hoc_ky1 - mon_hoc_ky2) # mon chi co o hoc ky 1
# Hoạt động 4
# Bài 4.1
chuoi_so = "25"
so = int(chuoi_so)
print(so, type(so))
so_thuc = float("3.14")
print(so_thuc, type(so_thuc))
danh_sach = list((1, 2, 3)) # tuple -> list
bo_ba = tuple([4, 5, 6]) # list -> tuple
tap_hop = set([1, 2, 2, 3, 3, 3]) # list -> set (tu loai bo trung lap)
tu_dien = dict([("a", 1), ("b", 2)]) # list cac tuple -> dict
print(danh_sach, bo_ba, tap_hop, tu_dien)
# Bài 4.2
#int("abc") -> quan sat loi ValueError
#int("3.14") -> quan sat loi ValueError
so_hop_le = int(float("3.14")) # cach lam dung: ep qua float truoc
print(so_hop_le)
# Bài 4.3
ket_qua = 5 + 2.5 # int + float -> Python tu dong chuyen thanh float
print(ket_qua, type(ket_qua))
ket_qua_2 = "Diem: " + str(8.5) # phai ep str() tuong minh, Python KHONG tu dong noi str voi so
print(ket_qua_2)