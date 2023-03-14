N = int(input())
lis2 = []
for i in range(N):
    lis = list(map(int, input().split()))
    lis2.append(lis)  # lis2 : 제곱해주기 전 리스트
# print(lis2)

lis3 = []
for k in range(len(lis2)):
    for o in range(3):
        lis3.append((lis2[k][o]) ** 2)  # lis2에 제곱실행
# print(lis3)


def list_chunk(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)] # 제곱실행 한 리스트 다시 3개씩 묶어줌

lis4 = list_chunk(lis3, 3)
# print(lis4)

# 제곱해주기 전 후보들의 총 투표수 합 (a_1 = 1, b_1 = 2, c_1 = 3)
a_1 = 0
for j in lis2:
    a_1 += j[0]

b_1 = 0
for j in lis2:
    b_1 += j[1]

c_1 = 0
for j in lis2:
    c_1 += j[2]

lis5 = [a_1, b_1, c_1]  #제곱 전 리스트
lis5_max = max(lis5) #제곱 전 max

# 제곱해준 후 후보들의 총 투표수 합 (a = 1, b = 2, c = 3)
a = 0
for j in lis4:
    a += j[0]

b = 0
for j in lis4:
    b += j[1]

c = 0
for j in lis4:
    c += j[2]

lis6 = [a, b, c]  #제곱 후 리스트
lis6_max = max(lis6) #제곱 후 max

if lis5.count(lis5_max) == 1:
    print(lis5.index(lis5_max) + 1, lis5_max)

else:
    if lis6.count(lis6_max) == 1:
        print(lis6.index(lis6_max)+1, lis5[lis6.index(lis6_max)])
    else:
        print('0', a_1)


# else:
#     if a == b and b == c and a == c:
#         print('0', a_1)
#     else:
#
#         maxV = 0
#         for l in lis6:
#             if l > maxV:
#                 maxV = l  # 제곱한 것의 합의 최댓값
#
#         d = lis6.index(maxV) + 1
#
#         print(d, lis5[lis6.index(maxV)])