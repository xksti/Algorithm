import math

# 소수 판별 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# 입력 받기
n = int(input())
numbers = list(map(int, input().split()))

# 소수 개수 세기
prime_count = 0
for num in numbers:
    if is_prime(num):
        prime_count += 1

# 결과 출력
print(prime_count)
