# hàm kiểm tra số nhị phân chia hết cho 5 không
def chia_het_cho_5(so_nhi_phan):
    # chuyển số nhị phân sang thập phân
    so_thap_phan = int(so_nhi_phan, 2)
    # kiểm tra số thập phân chia hết cho 5 không
    if so_thap_phan % 5 == 0:
        return True
    return False
# nhập chuỗi số nhị phân từ người dùng
so_nhi_phan = input("Nhập số nhị phân(phân tách bởi dấu ,): ")
# tách chuỗi số nhị phân thành các số nhị phân và kiểm tra số chia hết cho 5
so_nhi_phans = so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phans if chia_het_cho_5(so)]
# in ra các số nhị phân chia hết cho 5
if len(so_chia_het_cho_5) > 0:
    print("Các số nhị phân chia hết cho 5: ", ', '.join(so_chia_het_cho_5))
else:
    print("Không có số nhị phân nào chia hết cho 5")