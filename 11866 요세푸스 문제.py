N, K = list(map(int, input().split()))

lis = []
for i in range(1, N+1):
    lis.append(i)

res = []
M = K-1

while len(res) != N:
    if len(lis) == 1:
        M = 0
        res.append(lis[0])
        break
    res.append(lis[M])
    del lis[M]


    M = (M + K-1) % len(lis)

res = ', '.join(map(str, res))

print(f'<{res}>')





















# arr = []
# t = 0
# while len(lis) != 0:
#     t += K - 1
#
#     if t >= len(lis):
#         t = t-len(lis)
#
#     arr.append(lis[t])
#
#     del lis[t]
#
#     if len(lis) <= K-1:
#
#         while len(lis) != 0:
#             arr.append(lis[-1])
#             del lis[-1]
#
#
# arr = ', '.join(map(str, arr))
#
# print(f'<{arr}>')

