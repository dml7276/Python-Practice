jumin = "990122-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2 직전까지 (0, 1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒷자리 : " + jumin[7:]) # 7부터 끝까지
print("뒷자리(뒤에부터) :" + jumin[-7:]) # 뒤에부터 7까지 출력