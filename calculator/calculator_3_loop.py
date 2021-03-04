choice = 0

while(choice != '5'):
    print("사칙연산을 선택 하세요.")
    print("1.더하기 / 2.빼기 / 3. 곱하기 / 4.나누기 / 5.종료")

    choice = input("선택 하세요(1/2/3/4/5):")

    if choice != '5':
        num1 = int(input("첫번째 숫자 : "))
        num2 = int(input("두번째 숫자 : "))
        print("")

        if choice == '1':
            print(num1, "+", num2, "=", num1+num2)

        elif choice == '2':
            print(num1, "-", num2, "=", num1-num2)

        elif choice == '3':
            print(num1, "*", num2, "=", num1*num2)

        elif choice == '4':
            print(num1, "/", num2, "=", num1/num2)

        print("")
    else:
        print("계산기 종료")
