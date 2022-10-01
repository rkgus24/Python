mem = {"김구름": 25, "박에듀": 23, "온라인": 24}

print(mem.keys())
names = list(mem.keys()) #새로운 리스트 변수에 초기화

names.append("윤레벨")
print("새로운 리스트",names)
print("원래 딕셔너리에서 key 모음", list(mem.keys()))
print(mem.values())
print(list(mem.values()))
print("key와 value를 튜플로", mem.items())
print(mem.get("정판교", "없습니다"), mem.get("온라인", "없습니다"))

exist = '박에듀' in mem #굉장히 직관적인 용법
print(exist)

exist = '한바로' in mem
print(exist)

mem.clear()
print(mem) #빈 딕셔너리 출력
