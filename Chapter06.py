members = ['egoing', 'leezche', 'graphittie', 'abcd', 'efgh', 'ijklm']
i = 0
j = len(members) - 1
while j >= 0:
	print(members[j], end = ", ")
	j -= 1
 
 #members.reverse() 
# 원본이 사라지므로 조심해서 써야 함 역순으로 출력된 값을 기준으로 0 1 2 3 순서가 결정 됨
# ex) ijklm = 0, efgh = 1 ...
#print(members)

#temp = list(reversed(members)) # 원본을 유지하며 쓰고싶을 때
#print(temp)
