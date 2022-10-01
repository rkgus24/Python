import random
luckNum = random.sample(range(1, 45), 6)
bonusNum = random.randint(1, 45)

while bonusNum not in luckNum:
	bonusNum = random.randint(1, 45)
	
luckNum.sort()
print(f"행운번호 {luckNum} 보너스번호 [{bonusNum}]")
