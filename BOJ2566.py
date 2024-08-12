def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    # 9x9 행렬을 생성
    matrix = []
    index = 0
    for i in range(9):
        row = list(map(int, data[index:index + 9]))
        matrix.append(row)
        index += 9

    # 최댓값과 그 위치를 찾음
    max_value = -1
    max_position = (0, 0)
    for i in range(9):
        for j in range(9):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_position = (i + 1, j + 1)  # 행과 열의 번호를 1부터 시작하도록 조정

    # 최댓값과 그 위치를 출력
    print(max_value)
    print(max_position[0], max_position[1])

# main 함수를 호출합니다.
main()
