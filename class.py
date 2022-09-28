class human: # class의 이름 정의
    def __init__(self, height, age): # class가 처음 호출될 때 실행될 method
        self.height = height # class안에서의 멤버 변수
        self.age = age
        
    def how_old(self): # 객체가 스스로 쓸 수 있는 메소드
        print(self.age, "살 입니다.")
    
    def how_tall(self): 
        print(self.height, "cm 입니다.")
        
GH = human(163, 17) # 인스턴스 생성
JK = human(178, 17) # 인스턴스 생성

GH.how_old()
human.how_old(GH) # 편한거 사용

JK.how_tall()

print(GH.height)

