marks = [90, 25, 67, 45, 80]
number = 0

for mark in marks:
	number = number + 1
	print(mark)
	
	if mark >= 60:
		#print("%d번 학생은 합격입니다." % number2)
		#print(f"{number}학생은 {mark}점으로 합격입니다.")
		print("{}학생은 {}점으로 합격입니다." .format(number, mark))
	else:
		#print("%d번 학생은 불합격입니다." % number2)
		print(f"{number}학생은  {mark}점으로 불합격입니다.")
		
str = "{}학생은 {}점으로 합격입니다"
print(str.format('가현', 100))
