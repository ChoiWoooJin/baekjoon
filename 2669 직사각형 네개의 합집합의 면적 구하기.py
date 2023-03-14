arr = [[0]*100 for _ in range(100)]


for i in range(4):
    sc, sr, ec, er = list(map(int, input().split()))

    for row in range(sr, er):
        for col in range(sc, ec):
            arr[row][col] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)