# 7-2 27p

def func1() :
    global a 
    a = 10
    print("func1()에서 a의 값 ", a)
def func2() :
    print("func2()에서 a의 값 ", a)

a = 20

func1()
func2()

# 7-2 28p
func1() # [글로벌 예약어 코드]에서 정의된 함수
func2() # [글로벌 예약어 코드]에서 정의된 함수

#del(a) # 전역변수 a를 파이썬 실행환경에서 제거
#func2() # 전역변수 a가 없어서 에러 발생

func1() # global 예약어로 전역변수 a 다시 정의
func2()

# 7-2 29p
def A1():
    x=10 # A1의 지역변수 x
    def A2():
        x=20 # A2의 지역변수 x
    
    A2()
    print(x)
A1()

def A1():
    x=10 # A1의 지역변수 x
    def A2():
        nonlocal x # x는 A2

        x=20    # A1의 지역변수
                # x를 사용
    A2()
    print(x)
A1();

print("30p")

# 7-2 30p
def A1():
    x=10 # A1의 지역변수 x
    y=100 # A1의 지역변수 y
    
    def A2():
        x=20 # A2의 지역변수
    
        def A3():
            nonlocal x
            nonlocal y
            x = x+5000 # A2 의 지역변수 x를 사용
            y = y+5000 # A1 의 지역변수 y를 사용
        A3()
    A2()
    print(x) # A3에서는 A2의 x값을 변경, A1의 x는 값의 변화 없음
    print(y) # A3에서 변경한 내용이 A1의 y에 반영됨
A1()

