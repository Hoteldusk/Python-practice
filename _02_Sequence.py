# 순차구조
# 프로그램 코드는 위에서 아래로 순차적으로 실행
print("   *")
print("  ***")
print(" *****")
print("*******")

# input() 
# 사용자 입력을 받는 함수 () 내부에 prompt 문구 삽입가능
# 입력데이터를 문자타입의 데이터로 변환

# 원뿔 계산 프로그램

# 반지름 높이 값 입력받은 값 할당
print("원뿔의 부피와 겉넓이를 구하는 프로그램 입니다")
rad = int(input("반지름의 값을 입력 해 주세요 : "))
hei = int(input("높이의 값을 입력해 주세요 : "))

# 부피 출력
print("원뿔의 부피의 값은 ", (1 / 3 * 3.14 * rad **2 * hei), "입니다", sep="")

# 겉넓이 출력
print("원뿔의 겉넓이의 값은 ", (3.14 * rad **2 + 3.14 * rad * hei), "입니다", sep="")
