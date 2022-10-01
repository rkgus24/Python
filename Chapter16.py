import random

numbers = [] # 리스트 선언

while len(numbers) < 6:
	number = random.randint(1, 45)
	if number not in numbers:
		numbers.append(number) # 발생한 난수 리스트 추가
		
numbers.sort()
print(f'행운숫자는 {numbers} 입니다')
