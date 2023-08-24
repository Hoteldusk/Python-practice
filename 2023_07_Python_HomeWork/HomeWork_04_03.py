#7-2 9p
def para_func(v1, v2, v3 = 0) :
    result = 0
    result = v1 + v2 + v3
    return result
hap = 0
hap = para_func(10, 20)
print("9p 1번실행")
print("매개변수 2개 함수 호출 결과 ==> ", hap)
hap = para_func(10, 20, 30)
print("9p 2번실행")
print("매개변수 3개 함수 호출 결과 ==> ", hap)

#7-2 10p
def para3_func(v1, v2, v3) :
    return v1 + v2 + v3
print("10p 1번실행")
print(para3_func(10,20,30))


# def para3_func(v1, v2=0, v3) :
#     return v1 + v2 + v3



def para3_func(v1, v2, v3=0) :
    return v1 + v2 + v3

print("10p 3번실행")
print(para3_func(10,20))


def para3_func(v1, v2=0, v3=0) :
    return v1 + v2 + v3

print("10p 4번실행")
print(para3_func(10))
print(para3_func(10,20,30))