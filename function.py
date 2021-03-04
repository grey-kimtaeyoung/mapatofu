## 함수 기본 문법
# def function_name(parameter):
#     # logic
#     print(parameter)


# function_name(10)


### 함수를 사용했을때와 사용하지 않았을때의 차이
## 사용하지 않았을때
# r_name = "김태영"
# n_name = "다니엘"
# print("진짜 이름은 " + r_name + " 입니다.")
# print("가짜 이름은 " + n_name + " 입니다.")
# r_name = "귀도반로섬"
# n_name = "독재자"
# print("진짜 이름은 " + r_name + " 입니다.")
# print("가짜 이름은 " + n_name + " 입니다.")

## 사용 했을때
# def names(real_name, nick_name):
#     print("진짜 이름은 " + real_name + " 입니다.")
#     print("가짜 이름은 " + nick_name + " 입니다.")


# names("김태영", "다니엘")
# names("귀도반로섬", "독재자")


## 함수를 이용한 피보나치 구하기 함수
# def fib(n):    # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()


# fib(10)