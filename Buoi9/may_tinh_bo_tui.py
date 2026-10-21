import tkinter as tk
from tkinter import messagebox

def bam_nut(ky_tu):
    bieu_thuc_hien_tai = bien_bieu_thuc.get()
    bien_bieu_thuc.set(bieu_thuc_hien_tai + str(ky_tu))

def xoa_man_hinh():
    bien_bieu_thuc.set("")

def tinh_ket_qua():
    bieu_thuc = bien_bieu_thuc.get().strip()
    if bieu_thuc == "":
        messagebox.showerror("Loi", "Vui long nhap phep tinh truoc khi bam =.")
        return
    try:
        ket_qua = eval(bieu_thuc)
        bien_bieu_thuc.set(str(ket_qua))
    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho 0.")
        bien_bieu_thuc.set("")
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le.")
        bien_bieu_thuc.set("")

cua_so = tk.Tk()
cua_so.title("Ung dung May tinh bo tui")
cua_so.geometry("320x380")
cua_so.resizable(False, False)

bien_bieu_thuc = tk.StringVar()

tk.Label(cua_so, text="MAY TINH BO TUI", font=("Arial", 16, "bold")).grid(
    row=0, column=0, columnspan=4, pady=15
)

entry_man_hinh = tk.Entry(
    cua_so, textvariable=bien_bieu_thuc, font=("Arial", 14), width=24, justify="right"
)
entry_man_hinh.grid(row=1, column=0, columnspan=4, padx=15, pady=10)

danh_sach_nut = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
]

for ky_tu, hang, cot in danh_sach_nut:
    if ky_tu == "=":
        tk.Button(cua_so, text=ky_tu, width=5, height=2, command=tinh_ket_qua).grid(
            row=hang, column=cot, padx=5, pady=5
        )
    else:
        tk.Button(
            cua_so, text=ky_tu, width=5, height=2, command=lambda x=ky_tu: bam_nut(x)
        ).grid(row=hang, column=cot, padx=5, pady=5)

tk.Button(cua_so, text="Xoa man hinh (C)", width=26, height=2, command=xoa_man_hinh).grid(
    row=6, column=0, columnspan=4, padx=10, pady=10
)

if __name__ == "__main__":
    cua_so.mainloop()