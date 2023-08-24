# 7-3 12p
def func(name,age,address): # 3개 매개변수를 사용하는 함수 정의
    print('name:',name)
    print('age:',age)
    print('address',address)
     
func('홍길동','광주시',30) # 위치 매개변수 사용, 순서 틀림

func(name='홍길동',address='광주시',age=30) # 키워드 매개변수 사용

func(age=30,name='홍길동',address='광주시') # 순서 고려 없이 사용

# 7-3 13p
d={'name':'홍길동','address':'광주시','age':30} # 키워드 딕셔너리 정의
func(**d) # 딕셔너리 언패킹

func(*d) # 리스트 언패킹, 키워드가 순서대로 위치 매개변수로 사용
