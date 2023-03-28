import time, platform, os   # sleep함수 사용, os탐색, 창 새로고침
import random   # 랜덤 데미지를 주기위한 모듈

# 플레이어 클래스의 구성
class Player():
    name = ""
    hp = 0
    current_hp = 0
    mp = 0
    current_mp = 0
    power = 0
    magic_power = 0

    # 클래스가 불러와질때 자동 실행, 파라미터로 넣은 값을 가지고 객체를 생성
    def __init__(self, name):   # 스탯이 랜덤이라 이름만 파라미터로 받음
        self.name = name
        self.hp = random.randint(30, 50)
        self.current_hp = self.hp
        self.mp = random.randint(10, 20)
        self.current_mp = self.mp
        self.power = random.randint(10, 15)
        self.magic_power = random.randint(20, 25)    
        print(f"\n{self.name}이(가) 생성 되었습니다.")
        print(f"\nHP: {self.hp}\nMP: {self.mp}\n힘: {self.power}\n마력: {self.magic_power}")
        
        # 랜덤 스탯에 불만이 있거나 이름을 잘못 지정했을 경우 Y/N을 작성해 재분배 선택
        while True:
            choice = input("진행하려면 Y / 다시하려면 N 을 입력해주세요: ")
            if choice not in ["Y", "N", "y", "n"]:  # 입력값이 Y/N이 아니라면 continue로 다시 반복
                print("Y 또는 N을 입력해주세요")
                continue
            elif choice in ["N", "n"]:
                p1 = Player(input("당신의 이름은 무엇입니까?: ")) # N을 입력할 경우 p1 재선언
            break   # Y가 들어오면 함수 종료

    # 플레이어의 일반 공격
    def nomal_attack(self, enemy):
        damage = int(self.power * (random.randrange(8, 12) / 10)) # damage가 float형식이라 int로 형변환
        enemy.current_hp = enemy.current_hp - damage # 적의 현재 hp는 현재hp - 데미지
        print(f"{self.name}의 공격! {enemy.name}에게 {damage}의 물리데미지를 입혔습니다.")
        time.sleep(0.5) # sleep함수를 사용해 텍스트가 바로 띄워지는걸 방지, 좀 더 게임처럼 느껴짐
        if enemy.current_hp <= 0:   # 적의 현재 hp가 0보다 작거나 같을경우 적 사망
            print(f"{enemy.name}이(가) 쓰러졌습니다.")
            time.sleep(0.5)

    # 플레이어의 마법 공격
    def magic_attack(self, enemy):
        damage = int(self.magic_power * (random.randrange(8, 12) / 10))
        enemy.current_hp = enemy.current_hp - damage
        self.current_mp = self.current_mp - 5
        print(f"{self.name}의 공격! {enemy.name}에게 {damage}의 마법데미지를 입혔습니다.")
        time.sleep(0.5)
        if enemy.current_hp <= 0:
            print(f"{enemy.name}이(가) 쓰러졌습니다.")
            time.sleep(0.5)
    
    # 플레이어의 상태
    def status(self):
        print(f"\n==={self.name}의 상태===\nHP: {self.current_hp} / {self.hp}\nMP: {self.current_mp} / {self.mp}")
        time.sleep(0.5)

# 몬스터 클래스 구성
class Monster():
    name = "monster"
    hp = 0
    current_hp = 0
    power = 0

    # 클래스가 불러와질때 자동 실행, 파라미터로 넣은 값을 가지고 객체를 생성
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.current_hp = hp
        self.power = power

    # 몬스터의 일반 공격, 몬스터는 일반 공격만 보유하고 있다.
    def nomal_attack(self, enemy):
        damage = int(self.power * (random.randrange(8, 12) / 10))
        enemy.current_hp = enemy.current_hp - damage
        print(f"\n{self.name}의 공격! {enemy.name}에게 {damage}의 물리데미지를 입혔습니다.")
        time.sleep(0.5)
        if enemy.current_hp <= 0:
            print(f"{enemy.name}이(가) 쓰러졌습니다.")
            time.sleep(0.5)

    # 몬스터 상태 체크
    def status(self):
        print(f"\n{self.name} HP: {self.current_hp} / {self.hp}")
        time.sleep(0.3)

# 창 새로고침, 텍스트가 계속 쌓이면 가독성에 좋지 않음
def new_cmd():
    com_os = platform.system()  # 사용자 시스템의 os가 무엇인지 탐색
    input("\nENTER 키를 눌러 다음으로 진행하세요")  # 새로고침이 되기 전 나온 정보들을 사용자가 읽고 넘어갈 수 있도록 엔터 입력 후 창 새로고침 진행
    if com_os == 'windows': # 환경이 윈도우라면 cls 입력
        os.system('Cls')
    else:   # 환경이 리눅스나 맥이라면 clear 입력
        os.system('Clear')
