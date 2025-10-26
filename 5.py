N_Q = input()
N, Q = map(int, N_Q.split())
a = input()
mang_a = list(map(int, a.split()))
tong_truoc = [0] * (N + 1)
tong_hien_tai = 0
for i in range(N):
    gia_tri = mang_a[i]
    tong_hien_tai += gia_tri
    tong_truoc[i + 1] = tong_hien_tai
for so_lan in range(Q):
        L_R = input()
        L_1, R_1 = map(int, L_R.split())
tong_R = tong_truoc[R_1]
tong_L_tru_1 = tong_truoc[L_1 - 1]
tong_doan_con = tong_R - tong_L_tru_1
print(tong_doan_con)