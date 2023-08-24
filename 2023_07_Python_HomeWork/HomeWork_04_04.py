# 7-2 16p
def func3() :
    result1 = 100
    result2 = 200
    return result1, result2

hap1, hap2 = 0, 0

hap1, hap2 = func3()
print("func3()에서 돌려준 값 ==> ", hap1, hap2)

# 7-2 17p
def func3() :
    result1 = 100
    result2 = 200
    return result1, result2
hap1,hap2=func3()
print("func3()에서 돌려준 값==>", hap1,hap2)

hap_tup=func3()
print("func3()에서 돌려준 값==>", hap_tup)

print("func3()에서 돌려준 값==>", hap_tup[0],hap_tup[1])