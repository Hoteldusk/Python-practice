# 9-1 21p
lineNum = 1
# 파일열기 및 문자열 리스트 만들기
with open("C:\MyPython\애국가.txt",'r',encoding="UTF-8") as f:
    lines = f.readlines()
# 행번호 출력하기
for inStr in lines :
    print(lineNum, ' : ', inStr, end = '')
    lineNum += 1