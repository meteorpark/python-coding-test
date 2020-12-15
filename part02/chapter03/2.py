# # 큰 수의 법칙
# # N(array count), M, K를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split()) # 입력 값 : 5 8 3
# # N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split())) # 입력 값 : 2 4 5 4 6
#
# data.sort()  # 입력받은 수 정렬
# first = data[n - 1]  # 가장 큰 수
# second = data[n - 2]  # 두번째로 큰 수
#
# # 가장 큰 수가 더해지는 횟수 계산
# count = int(m / (k + 1)) * k
# count += m % (k + 1)
#
# result = 0
# result += count * first  # 가장 큰 수 더하기
# result += (m - count) * second  # 두번째로 큰 수 더하기
#
# print(result) # 최종 답안 출력


arrayCount, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
first = array[arrayCount - 1]
second = array[arrayCount - 2]

count = int(m / (k + 1)) * k  # 가장 큰 수가 더해지는 횟수
count += m % (k + 1)

result = 0
result += first * count
result += second * (m-count)
print(result)
