# 비교하는 카드의 공격력만큼 동시에 서로 상대 카드의 생명력을 깎는다. 줄어든 생명력은 다시 회복되지 않는다.
# 생명력이 0 이하인 경우에는 카드는 죽은 상태로 전환된다.
# 카드가 두 장 모두 남아있다면 비교를 계속한다. => while문 사용하기

A_attack, A_hp = map(int, input().split())
B_attack, B_hp = map(int, input().split())

while True:
    # 체력 0 이하 될 때 까지 계속 때려버리기
    A_hp -= B_attack
    B_hp -= A_attack

    if A_hp > 0 and B_hp <= 0:
        print("PLAYER A")
        break
    
    elif A_hp <= 0 and B_hp > 0:
        print("PLAYER B")
        break

    elif A_hp <= 0 and B_hp <= 0:
        print("DRAW")
        break