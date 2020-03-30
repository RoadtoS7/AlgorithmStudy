# 2020-03-21
# Example 1
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()


# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

# Example 2
class Fourcal:
    def setData(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

a = Fourcal()
a.setData(4, 2)
# 1. 매개변수 self
# setData의 첫번째 매개변수인 self에는 setData메서드를 호출한 객체 a가 자동으로 전달된다.
# 파이썬 첫 번째 매개변수 이름은 관습적으로 self라는 이름을 사용한다.
# 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에

# 2. 함수 수행문
# 수행문내에서 self는 호출한 객체인 a이기 때문에 다음과 같이 해석된다.
# a.first = 4 : a객체에 객체변수 first 가 생성되고 값 4가 저장된다.
# a.second = 2: a객체에 객체변수 second 가 생성되고 값 2가 저장된다.

print(a.first)
print(a.second)
# 출력됨-> a의 객체변수 first, second 가 생성됨을 알 수 있음

print(a.add())











