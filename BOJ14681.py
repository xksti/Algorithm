def main():
    # 두 정수를 입력
    x = int(input())
    y = int(input())

    # 각 사분면을 판별하고 출력
    if x > 0 and y > 0:
        print(1)  # 1사분면
    elif x < 0 and y > 0:
        print(2)  # 2사분면
    elif x < 0 and y < 0:
        print(3)  # 3사분면
    elif x > 0 and y < 0:
        print(4)  # 4사분면

# main 함수를 호출
main()
