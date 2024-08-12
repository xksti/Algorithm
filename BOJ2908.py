def main():
    # 두 개의 세 자리 수를 입력받는다
    a, b = input().split()

    # 숫자를 거꾸로 읽기 위해 문자열을 뒤집는다
    reversed_a = int(a[::-1])
    reversed_b = int(b[::-1])

    # 두 수 중 큰 수를 출력.
    if reversed_a > reversed_b:
        print(reversed_a)
    else:
        print(reversed_b)


# main 함수를 호출
main()
