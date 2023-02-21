import math
# 1
# n = int(input())
# print (math.radians(n))

#2
# h = int(input("Height: "))
# a = int(input("Base, first value: "))
# b = int(input("Base, second value: "))
# area = ((a + b) / 2) * h
# print(area)

#3

# n = int(input("Input number of sides: "))
# length = int(input("Input the length of sides: "))
# area = (n * length**2) / (4 * math.tan(math.pi/n))
# print("The area of the polygon is:" + str(round(area)))

#4
length = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))
area = float(length * height)
print("Expected Output: " + str({area}))

