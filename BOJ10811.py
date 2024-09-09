# 입력받기
n, m = map(int, input().split())

# 바구니 초기화 (1부터 N까지의 번호가 들어있음)
baskets = list(range(1, n+1))

# M번의 작업
for _ in range(m):
    i, j = map(int, input().split())
    # i-1부터 j까지의 인덱스를 뒤집음 (i와 j는 1-based index이므로 0-based로 맞춰줌)
    baskets[i-1:j] = baskets[i-1:j][::-1]

# 결과 출력
print(*baskets)
