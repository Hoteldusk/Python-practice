# 9-1 19p

# 전역 변수 설정
lineNum = 1
# 파일열기 및 문자열 리스트 만들기
f = open("C:\MyPython\애국가.txt",'r',encoding="UTF-8")
lines = f.readlines()
# 행번호 출력하기
for inStr in lines :
    print(lineNum, ' : ', inStr, end = '')
    lineNum += 1
f.close()

