# 7-2 31~32p
def checkPasswd(passwd) :
    if len(passwd) < 8 : # 비밀번호 길이가 8 미만이면 False 반환
        return False
    else : # 비밀번호 길이가 8 이상
        if passwd.isalnum() : # 문자열이 숫자 또는 문자로만 구성?
            return True
        else :
            return False
## 전역변수 선언 부분
passwd = ''
## 메인 코드 부분
passwd = input('새로운 비밀번호를 입력하세요:')
if checkPasswd(passwd) :
    print('비밀번호가 생성됩니다')
else :
    print('오류! 비밀번호 생성 규칙을 확인하세요')
