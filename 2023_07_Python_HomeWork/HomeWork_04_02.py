# 7-2 21p
def plus(v1, v2) :
    """이 함수는 v1과 v2를 더한 뒤 결과를 반환합니다."""
    result = 0
    result = v1 + v2
    return result
x = plus(100, 200)
print(x)
print(plus.__doc__)

# 7-2 22p
print(plus.__doc__)
help(plus)