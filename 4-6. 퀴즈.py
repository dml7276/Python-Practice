""" 
Quiz) 사이트 별로 비밀번호를 만들어주는 프로그램을 작성하시오.
예) http://naver.com
규칙 1 : http:// 부분은 제외 => naver.com
규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙 3 : 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
                    (nav)               (5)             (1)             (!)
예) 생성된 비밀번호 : nav51!                               
"""

url = input("사이트 주소를 입력하세요 : ")
url = url.replace("http://", "")
print(url)

url = url[:url.index(".")] # 0부터 . 직전까지
print(url)

pw = url[0:3] + str(len(url)) + str(url.count('e')) + "!"
print("생성된 비밀번호 : %s" % pw)
