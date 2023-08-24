# 문제3 : 선택구조를 사용 정수입력받고 성적 산출기준에 따라 성적이 출력되는 프로그램 작성
score = int(input("점수를 입력하세요 : "))
if score > 100 or score < 0 :
    print("잘못된 점수입니다.")
else :
    if score >= 90 and score <= 100 :
        print("A입니다.")
    elif score >= 80 and score <= 89 :
        print("B입니다.")
    elif score >= 70 and score <= 79 :
        print("C입니다.")
    elif score >= 60 and score <= 69 :
        print("D입니다.")
    else :
        print("F입니다.")