n = int(input())
a = list(map(int, input().split()))
khoang_cach_min = float('inf') 
end = False
for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            end = j - i
            if end < khoang_cach_min:
                khoang_cach_min = end      
            end = True
if end:
    print(khoang_cach_min)
else:
    print(-1)