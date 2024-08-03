def main():
    T = int(input())  # 테스트 케이스의 개수 입력

    for _ in range(T):
        R, S = input().split()
        R = int(R)

        result = ""
        for char in S:
            result += char * R

        print(result)


# main 함수를 호출
main()
