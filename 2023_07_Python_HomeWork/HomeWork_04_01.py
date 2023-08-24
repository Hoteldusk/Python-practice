# 7-1, 16p
def get_pi() :
    return '3.141592653589793238'
x = get_pi()
print(x)

# 7-2, 17p
x = get_pi()
print(x)
# 값을 실수형으로 y에 반환
y = float(get_pi())
print(y)
# y를 소수점 아래 20자리까지 출력
print(f'{y:.20f}')
# y를 정수아래 3자리, 소수점아래 20자리까지 출력
print(f'{y:3.20f}')
