def main():
    # 문자열을 입력받습니다.
    S = input().strip()
    # 인덱스를 입력받습니다.
    i = int(input().strip())

    # 문자열의 i번째 문자를 출력합니다.
    # Python의 인덱스는 0부터 시작하므로, i-1을 사용합니다.
    print(S[i - 1])


# main 함수를 호출합니다.
main()
