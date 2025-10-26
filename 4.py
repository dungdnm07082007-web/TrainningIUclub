danh_sach_so = list(map(int, input().split()))
so_a = danh_sach[0]
so_b = danh_sach[1]
so_c = danh_sach[2]
ket_qua = "no"
if so_a + so_b == so_c:
    ket_qua = "yes"
elif so_a + so_c == so_b:
    ket_qua = "yes"
elif so_b + so_c == so_a:
    ket_qua = "yes"
print(ket_qua)