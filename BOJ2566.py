# 9x9 배열을 입력받습니다.
matrix = [list(map(int, input().split())) for _ in range(9)]

# 초기값 설정
max_value = -1
max_row = 0
max_col = 0

# 배열 순회
for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row = i + 1  # 행 번호는 1부터 시작
            max_col = j + 1  # 열 번호는 1부터 시작

# 결과 출력
print(max_value)
print(max_row, max_col)
