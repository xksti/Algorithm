# 입력 받기
n = int(input())
numbers = []

# 숫자 입력 받기
for _ in range(n):
    numbers.append(int(input()))

# 오름차순 정렬
numbers.sort()

# 결과 출력
for num in numbers:
    print(num)
