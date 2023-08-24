# 문제2 : 순차구조를 사용
print("n\tn**2\t n**3")
print("=====================")
n = 1
print(n,"\t",str(n**2).rjust(2, " "),"\t",str(n**3).rjust(3, " "))
n += 2
print(n,"\t",str(n**2).rjust(2, " "),"\t",str(n**3).rjust(3, " "))
n += 2
print(n,"\t",n**2,"\t",n**3)
n += 2
print(n,"\t",n**2,"\t",n**3)