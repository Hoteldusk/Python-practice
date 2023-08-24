a = 3 > 6
print(3 > 6)
print(a)

suf = 10
vol = 20
isStop = suf == vol
print("suf 와 vol이 같은가? : ",isStop)



print("원뿔 계산 프로그램 선택구조로 개선")
# 반지름 높이 값 입력받은 값 할당
print("원뿔의 부피와 겉넓이를 구하는 프로그램 입니다")
rad = int(input("반지름의 값을 입력 해 주세요 : "))
hei = int(input("높이의 값을 입력해 주세요 : "))

if rad > 0 and hei >0: 
# 부피 출력
    print("원뿔의 부피의 값은 ", (1 / 3 * 3.14 * rad **2 * hei), "입니다", sep="")
# 겉넓이 출력
    print("원뿔의 겉넓이의 값은 ", (3.14 * rad **2 + 3.14 * rad * hei), "입니다", sep="")
    
else:
    print("입력값이 잘못되었습니다","양의 정수로 입력해주세요")

   
# 세 정수중 가장 큰값을 판단하는 프로그램
print("\n세 정수중 가장 큰값을 판단하는 프로그램입니다")
A = int(input("A 입력 : "))
B = int(input("B 입력 : "))
C = int(input("C 입력 : "))

# A, B, C 중 가장 큰 수 출력
# 1.기본 제공 함수 사용
# print(max(A, B, C))

# 2. if, elif 사용
if A > B :
    if A > C :
        print(A)
    else :
        print(C)
else :
    if B > C :
        print(B)
    else :
        print(C)