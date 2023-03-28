import time  # sleep함수 사용
import game_class   # 클래스 모듈

# 플레이어의 행동 함수
def player_turn():
    while True: # while문을 사용해 break를 걸 때 까지 계속 실행
        try:    
            print("\n===공격 방식 선택===\n1. 물리 공격\n2. 마법 공격")
            player_skill_input = int(input("\n공격할 방식의 번호를 입력해주세요: "))
            if player_skill_input == 0 or player_skill_input > 2:   # 1,2 외에 다른 숫자가 들어오면 다시 입력
                print("공격방식을 다시 입력해주세요")
                continue  # while문을 처음부터 다시 시작함
            
            if player_skill_input == 2:
                if p1.current_mp < 5:
                    print("스킬을 사용하는데 필요한 MP가 모자랍니다.")
                    continue 
        except ValueError:  # ValueError가 나왔을때 execpt문 실행
            print("공격방식을 숫자로 입력해주세요")
            continue 
            
        break  # while문을 빠져나옴

    print("\n===공격 대상 선택===")
    for i, m in enumerate(monster_list):    # enumerate함수를 사용해 i는 순서를 m은 m1,m2와 같은 몬스터 변수를 입력
        print(f"{i+1}. {m.name} (HP: {m.current_hp} / {m.hp})")

    while True: # while문을 사용해 break를 걸 때 까지 계속 실행
        try:    
            player_target_input = int(input("\n공격할 대상의 번호를 입력해주세요: ")) 
            if player_target_input <= 0 or player_target_input > len(monster_list): # 0 또는 리스트의 갯수보다 더 많은 숫자 입력 시 다시 입력
                print("잘못된 대상을 선택하셨습니다. 다시 선택해주세요.")
                continue 
        except ValueError:  # ValueError가 나왔을때 execpt문 실행
            print("대상 번호를 숫자로 입력해주세요.")
            continue
            
        break

    if player_skill_input == 1: # 공격방식의 번호 입력이 1(노말어택)이라면
        game_class.Player.nomal_attack(p1, monster_list[player_target_input -1])    # game_class 파일 Player 클래스의 nomal_attack함수 실행
    elif player_skill_input == 2: # 공격방식의 번호 입력이 2(매직어택)이라면
        game_class.Player.magic_attack(p1, monster_list[player_target_input -1])

# 몬스터의 행동함수
def monster_turn():
    for monster in monster_list:
        game_class.Monster.nomal_attack(monster, p1)    # 반복문을 돌면서 한마리씩 플레이어 어택

# 몬스터 리스트 제거 함수(반복문으로 간략화 가능해 보임)
def monster_death():  
    for m in monster_list:
        if m.current_hp <= 0:
            monster_list.remove(m)

p1 = game_class.Player(input("당신의 이름은 무엇입니까?: "))    # Player 클래스 __init__에서 많은 숫자가 랜덤으로 부여시켜서 name만 받음
m1 = game_class.Monster("주황버섯", 15, 4)  # Monster 클래스 __init__에서 요구하는 (name, hp, power)
m2 = game_class.Monster("초록버섯", 25, 5)
m3 = game_class.Monster("파랑버섯", 35, 6)

monster_list = [m1, m2, m3] # 몬스터 리스트

turn = 1    # 턴 이라는 변수 선언, 1로 선언해야 시작할때 1번째 턴이라고 나오기때문에 1로 선언

# 게임 실행 부분
while True: # break가 걸릴 때 까지 반복 실행
    game_class.new_cmd()
    print(f"\n====={turn}번째 턴====")  # f_string을 이용
    time.sleep(0.3) # 텍스트가 한번에 입력되는 것을 방지함, 좀 더 게임처럼 즐길 수 있음
    p1.status() # p1 = 플레이어, 플레이어의 상태를 보여주는 status함수를 사용
    time.sleep(0.3)
    for m in monster_list:  # 몬스터 리스트에 있는 몬스터들을 m이라는 변수에 순차 저장
        m.status()  # m에 m1,m2,m3 순서로 들어오고 status함수 사용, 몬스터가 죽으면 리스트에서 삭제되기에 m2가 죽으면, m1,m3가 순차적으로 들어옴
        time.sleep(0.3)

    print("\n===플레이어 턴===")
    player_turn()   # 플레이어 행동함수 실행
    monster_death() # 몬스터 리스트 제거 함수 실행

    if monster_list == []:  # 몬스터가 모두 죽어서 리스트가 비어버렸다면
        print("\n====clear!====\n당신이 승리했습니다.")
        break   # 반복문 종료
    
    print("\n===몬스터 턴===")
    time.sleep(0.3)
    monster_turn()  # 몬스터 행동함수 실행

    if p1.current_hp <= 0:  # 플레이어의 체력이 0보다 같거나 작다면
        print("\n당신이 사망하였습니다.\n ====게임 오버====")
        break   # 반복문 종료

    turn += 1   # 턴 + 1
    print("\n====턴 종료====")    # 위의 break에 걸리지 않았다면 다시 반복문으로 돌아감
    time.sleep(0.3)