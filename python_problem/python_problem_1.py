num = 0

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
    i += 1
    print("playerA :",i)
