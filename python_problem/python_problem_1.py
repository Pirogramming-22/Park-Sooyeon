num = 0
br_num = 0

while br_num < 31:
    while 1:
        A_input = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
        if A_input.isdigit():
            num = int(A_input)
            if num in [1, 2, 3]:
                break
            else:
                print("1, 2, 3 중 하나를 입력하세요.")
        else:
            print("정수를 입력하세요")

    for i in range(num):
        br_num += 1
        print("playerA :",br_num)
        if br_num == 31:
            exit()

    while 1:
        B_input = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
        if B_input.isdigit():
            num = int(B_input)
            if num in [1, 2, 3]:
                break
            else:
                print("1, 2, 3 중 하나를 입력하세요.")
        else:
            print("정수를 입력하세요")

    for j in range(num):
        br_num += 1
        print("playerB :",br_num)
        if br_num == 31:
            exit()
