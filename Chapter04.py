marks = [90, 25, 67, 45, 80]
number = 0

for mark in marks: # not in : marks 안에 없을 때
	number = number + 1
	if mark < 60 : continue
	print(f"{number}학생은 {mark}점으로 합격입니다")
	
names = ['강민석', '김강민', '김병찬', '김영준', '노가현', '박수빈', '박정빈', '배유정', '심지혜', '유성욱', '윤동현', '이근호', '이채우', '천나영', '하현재']
for name in names:
	print(name, end = ", ")
