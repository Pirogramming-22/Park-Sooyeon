import random
def brGame(player, br_num):

    if player == "computer":
        num = random.randint(1, 3)
    
    else:
        while 1:
            player_input = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
            if player_input.isdigit():
                num = int(player_input)
                if num in [1, 2, 3]:
                    break
                else:
                    print("1, 2, 3 중 하나를 입력하세요.")
            else:
                print("정수를 입력하세요")

    for i in range(num):
        br_num += 1
        print(player + " : " + str(br_num))
        if br_num == 31:
            if player == "computer":
                print("player win!")
            else:
                print("computer win!")
            exit()
    return br_num

num = 0
br_num = 0
while br_num < 31:
    br_num = brGame("computer", br_num)
    br_num = brGame("player", br_num)