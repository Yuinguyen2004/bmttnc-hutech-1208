# Viết một hàm nhận vào một chuỗi và trả về chuỗi đảo ngược của chuỗi đó.
def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
# Sử dụng hàm và in ra kết quả
input_string = input("Nhập một chuỗi: ")
print("Chuỗi đảo ngược: ", dao_nguoc_chuoi(input_string))