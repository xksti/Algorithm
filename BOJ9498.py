def main():
    # 시험 점수를 입력
    score = int(input())

    # 점수에 따른 학점을 출력
    if 90 <= score <= 100:
        print("A")
    elif 80 <= score <= 89:
        print("B")
    elif 70 <= score <= 79:
        print("C")
    elif 60 <= score <= 69:
        print("D")
    else:
        print("F")


# main 함수를 호출
main()
