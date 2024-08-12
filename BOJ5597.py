def main():
    # 총 학생 수와 제출한 학생 수
    total_students = set(range(1, 31))

    # 제출한 학생의 번호를 입력
    submitted_students = set()
    for _ in range(28):
        submitted_students.add(int(input().strip()))

    # 제출하지 않은 학생을 찾는다
    missing_students = total_students - submitted_students

    # 제출하지 않은 학생의 번호를 출력
    for student in sorted(missing_students):
        print(student)


# main 함수를 호출
main()
