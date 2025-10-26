n = int(input())
so = list(map(int, input().split()))
tong_le = 0
N = len(so)
for i in range(N):
    if i % 2 != 0:
        tong_le += so[i]
print(tong_le)