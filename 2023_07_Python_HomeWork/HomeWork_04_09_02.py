# 7-3 21p
s=10
(lambda x,y: s+x+y)(10,20)

add_l=lambda x,y:x+y
sub_l=lambda x,y:x-y
mul_l=lambda x,y:x*y
(lambda x,y:(add_l(x,y),sub_l(x,y),mul_l(x,y)))(10,20)

def double(x):
    return x**2
list(map(double,[2,3,4])) # 함수객체를 map함수에서 사용

list(map(lambda x:x**2,[2,3,4])) # 람다 표현식을 사용
