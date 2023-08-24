# 9-1 25p
with open("C:\MyPython\애국가.txt",'rb') as f:
    f.read(5)
    f.readline()
    f.readline(10)

with open("C:\MyPython\애국가.txt",'r',encoding="UTF-8") as f:
    f.read(5)
    f.readline()
    f.readline(10)
    
# 9-2 26p
with open("C:\MyPython\애국가.txt",'r',encoding="UTF-8") as f:
    lines = f.readlines() 
with open("C:\MyPython\애국가.txt",'rb') as f:
    lines_b = f.readlines() 
lines[0]
lines_b[0]
lines[1]
lines_b[1]
# 9-2 27p
lines[0] #텍스트파일 읽기
lines_b[0] #바이너리파일 읽기
lines[0].encode() #텍스트 문자열을 바이너리 코드로 인코딩
lines_b[0].decode() #바이너리 코드를 텍스트 문자열로 디코딩
help(lines[0].encode) # encode함수 기능 설명 출력
help(lines_b[0].decode) # decode 함수 기능 설명 출력


