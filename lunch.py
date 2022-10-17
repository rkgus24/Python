import random
menus = ["김치 볶음밥", "초밥", "김치찌개", "국밥", "파스타", "짜장면", "칼국수", "돈까스"]
prices = [6000, 9000, 7000, 6000, 7000, 6000, 4000, 5000]

print("메뉴 : ")
for menu, price in zip(menus, prices):
    print(menu, price)
    
i = random.randint(0, len(menus) - 1)
print("추천 메뉴 : ", menus[i])
print("메뉴 가격 : ", prices[i])