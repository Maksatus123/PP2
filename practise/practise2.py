# def mul(a, b, c):
#     return a * b * c

# print(mul(int(input()), int(input()), int(input())))


# def mul_N(*l):
#     s = 1
#     for i in l:
#         s = i * s
#     print(s)

# mul_N(1,2)
# mul_N(5,6,8,9)

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return(n * factorial(n-1))


# n = int(input())
# print(factorial(n))



# def fibonacci_of(n):
#     if n in {0, 1}:
#         return n
#     return fibonacci_of(n - 1) + fibonacci_of(n - 2)

# n = int(input())
# print(fibonacci_of(n))


# time = input().split(" ")

# date = time[0].split("-")

# year = lambda x: date[0]
# month = lambda x: date[1]
# day = lambda x: date[2]
# time1 = lambda x: time[1] 

# print(year(date))
# print(int(month(date)))
# print(day(date))
# print(time1(time))

# def evenOrOdd(*l):
#     even = lambda x: [i for i in x if i % 2 == 0]
#     odd = lambda x: [i for i in x if i % 2 == 1]
#     print(type(even(l)))
#     print("Number of even:", len(even(l)))
#     print("Number of odd:", len(odd(l)))

# evenOrOdd(1,2,3,4,5,6,7,8)


# class Transport:
#     size = 'Big'

# class Car(Transport):
#     velocity = "90 m/s"

# class SportCar(Car):
#     color = "yellow"

# sixty = SportCar()
# print(sixty.color)
# print(sixty.size)
