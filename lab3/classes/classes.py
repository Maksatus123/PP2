import math

class IOHandler:
    def __init__(self) -> None:
        self.userInput=""

    def getString(self):
        self.userInput = input()

    def printString(self):
        print(self.userInput)

# 

class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length:int) -> None:
        super().__init__()
        self.length = length

    def area(self):
        return self.length**2
    
class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        super().__init__()
        self.width = width
        self.length = length

    def area(self):
        return self.width*self.length

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def show(self):
        return f"X: {self.x}, Y: {self.y}"
    
    def move(self, x, y):
        self.x+=x
        self.y+=y

    def dist(self):
        return math.sqrt(self.x**2+self.y**2)
    

class Account:
    def __init__(self, owner) -> None:
        self.owner = owner
        self.balance = 0

    def __showBalance(self):
       print(f"{self.owner}, your current balance is {self.balance}\n")

    def deposit(self, balance):
        self.balance+=balance
        self.__showBalance()

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance-=amount
            self.__showBalance()
        else:
            print(f"You cannot withdraw {amount}")
            self.__showBalance()



def isPrime(num: int):
  for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0:
      return False
  return True


items = [1,2,3,4,5,6,7,8,9,10]
items = filter(lambda x: isPrime(x), items)
print([i for i in items])
