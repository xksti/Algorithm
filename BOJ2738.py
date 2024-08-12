def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    M = int(data[1])

    matrix_a = []
    matrix_b = []

    index = 2
    for _ in range(N):
        row = list(map(int, data[index:index + M]))
        matrix_a.append(row)
        index += M

    for _ in range(N):
        row = list(map(int, data[index:index + M]))
        matrix_b.append(row)
        index += M

    result_matrix = []
    for i in range(N):
        result_row = []
        for j in range(M):
            result_row.append(matrix_a[i][j] + matrix_b[i][j])
        result_matrix.append(result_row)

    for row in result_matrix:
        print(" ".join(map(str, row)))

# main 함수를 호출
main()
