python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n")) 
print(python.find("Java")) # 원하는 문자열이 없으면 -1 반환
# print(python.index("Java")) 원하는 문자열이 없으면 에러 발생

print(python.count("n")) # n이 문자열 내에서 몇번 등장하는 지