numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

a = "goorm"

# 공간까지 삭제
del numbers[4]
print(numbers)

del numbers[:5]
print(numbers)

# 객체 자체를 삭제
del a
