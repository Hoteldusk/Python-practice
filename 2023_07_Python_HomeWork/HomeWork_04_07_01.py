# 7-3 6p
def func(name,age,address): # 3개 매개변수를 사용하는 함수 정의
    print('name:',name)
    print('age:',age)
    print('address',address)
    
func('홍길동',30,'광주시') # 위치 매개변수 사용

x = ('홍길동',30,'광주시') # 3개 값을 가지는 튜플 정의
func(*x) # 위치 매개변수로 튜플 언패킹 사용

y = ['임꺽정',33,'전주시'] # 3개 값을 가지는 리스트 정의
func(*y) # 위치 매개변수로 리스트 언패킹 사용