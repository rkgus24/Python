evennumbers = [2, 4, 6, 8]
oddnumbers = [1, 3, 5, 7]
evennumbers.append(10)
print(evennumbers)

evennumbers.insert(0, 0) # 맨 앞에 0을 넣음
print(evennumbers)

evennumbers.expend(oddnumbers) # 리스트까지 합하는 것
print(evennumbers)
print(len(evennumbers))
