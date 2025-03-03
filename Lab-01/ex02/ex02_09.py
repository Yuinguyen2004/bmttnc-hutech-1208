# Viết hàm kiểm tra xem một số được nhập vào có phải là số nguyên tố hay không.
def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# kiểm tra số nguyên tố và in ra kết quả
number = int(input("Nhập một số cần kiểm tra: "))
if(kiem_tra_so_nguyen_to(number)):
    print(number, "là số nguyên tố")
else:
    print(number, "không phải là số nguyên tố")