# input().split() : 입력받은 값을 공백을 기준으로 분리
# 첫번째 입력받을 값은 NxM(몇 행 몇 열)인지를 받는다.

# case 1
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)


# case 2

# n, m = map(int, input().split())
#
# result = 0
#
# for i in range(n):
#     data = list(map(int, input().split()))
#
#     min_value = 101
#     for a in data:
#         min_value = min(min_value, a)
#     result = max(result, min_value)
#
# print(result)


