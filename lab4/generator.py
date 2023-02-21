#1
# n = int(input())
# a = (i**2 for i in range(1,n+1))
# for i in a:
#     if i < n:
#         print(i)

#2
# n = int(input())
# generator = (i for i in range(1, n + 1))
# for num in generator:
#     if num % 2 == 0:
#         print(num, end=", ")

#3
# def func():
#     n = int(input())
#     x = lambda x : x if (x % 3 == 0 and x % 4 == 0) or x == 0 else "o"
#     a = (x(i) for i in range(1, n+1))
#     for i in range(n):
#         y = next(a)
#         if(y != "o"):
#             print(y)  
# func()

#4
# def squares_gen(a, b):
#     for i in range(a, b+1):
#         yield i ** 2

# a = int(input())
# b = int(input())

# squares = squares_gen(a, b)

# for i in squares:
#     print(i, end=", ")

#5
def down_to_zero(n):
    for i in range(n, 0, -1):
        yield i

n = int(input())
gen = down_to_zero(n)
for i in gen:
    print(i)
