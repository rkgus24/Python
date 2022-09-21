def palindrome(string):
	return print(string == string[::-1]) # 리스트를 뒤에서 부터 순차적으로 (역순으로) 비교하는 것

str = input("문장을 입력하세요 : ")
palindrome(str)