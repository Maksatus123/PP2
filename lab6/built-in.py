import math
import time

#1
# li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(math.prod(li1))

#2
# s = input()
# upperL = 0
# lowerL = 0
# for i in s:
#     if(ord(i) >= 65 and ord(i) <= 90):
#         upperL += 1
#     elif(ord(i) >= 97 and ord(i) <= 122):
#         lowerL += 1
# print("Upper:", upperL,"\n"+"Lower:", lowerL)

#3 
# s = input()
# s1 = s[::-1]
# if s == s1:
#     print("It's a pallindrome")
# else:
#     print("It is not a pallindrome")

#4
# num = int(input())
# wait = int(input())
# time.sleep(wait / 1000)
# print(f"Square root of {num} after {wait} miliseconds is {math.sqrt(num)}")

#5
# cnt = 0
# tup = ("Hello", "Maksat", 1, 2, 3, True, "fwfeww", "fdsfs", "")

# for i in tup:
#     if bool(i):
#         cnt += 1

# print(cnt)