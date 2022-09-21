def profile(name, age, *language):
	print(f'이름 : {name}\t나이 : {age}', end = " ")
	for lang in language:
		print(lang, end = " ")
	print()
	
profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
profile("김태호", 25, "Kotlin", "Swift")


#내장모듈

#import math
#print(math.ceil(2.9)) # 올림
#print(math.floor(2.9)) # 버림
#print(math.sqrt(16)) # 제곱근