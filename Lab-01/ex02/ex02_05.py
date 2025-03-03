so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập lương mỗi giờ làm tiêu chuẩn: "))
gio_tieu_chuan = 44 # 44 giờ/tuần
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan) # số giờ làm vượt chuẩn mỗi tuần
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5 #tổng thu nhập
print(f"số tiền thực lĩnh của nv là: {thuc_linh}")
