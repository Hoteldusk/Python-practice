# 7-3 19p
def add(x,y):
    return x+y
add(10,20)

add_lambda = lambda x,y: x+y
add_lambda(10,20)

# 7-3 20p
(lambda x,y: x+y)(10,20)

(lambda : 10)()

(lambda x,y: s=x+y)(10,20)