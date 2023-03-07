import os
#1
# directories = os.listdir()
# files = list()

# #only directories
# for i in directories:
#     if not os.path.isfile(i):
#         print(i)

# print()
# #only files
# for i in directories:
#     if os.path.isfile(i):
#         print(i)

# #files and directories
# for i in directories:
#     print(i, end=" ")

#2 
# first = 'built-in.py'
# first_path = os.path.abspath(first)
# second = 'directories.py'
# second_path = os.path.abspath(second)

# files_path = [first_path, second_path]

# for i in files_path:
#     print('Exist:', os.access(i, os.F_OK))
#     print('Readable:', os.access(i, os.R_OK))
#     print('Writable:', os.access(i, os.W_OK))
#     print('Executable:', os.access(i, os.X_OK))

#3
# p1 = ('E:\Maksat\PP2\date.py')
# print(os.path.exists(p1))
# p2 = os.path.abspath('directories.py')
# print(os.path.exists(p2))
# print(os.path.basename(p2))
# print(os.path.dirname(p2))


#4
# with open(r"text.txt", 'r') as fp:
#     x = len(fp.readlines())
#     print('Total lines:', x)

#5

# l = ["apple", "banana", "orange", "melon"]
# with open("text.txt", 'w') as fp:
#     for i in l:
#         fp.write(i)

#6

# for i in range(65, 90):
#         path = r"E:\Maksat\PP2\lab6"
#         name = os.path.join(path, chr(i) +".txt")
#         f = open(name, "a")
# for i in os.listdir(path):
#     print(i)

#7

# path1 = r"E:\Maksat\PP2\lab6\text.txt"
# path2 = r"E:\Maksat\PP2\lab6\text1.txt"

# fp1 = open(path1, "r")
# fp2 = open(path2, "w")

# for i in fp1:
#     fp2.write(i)

# fp1.close()
# fp2.close()

# fp2 = open(path2, "r")

# for i in fp2:
#     print(i)


#8
path1 = r"E:\Maksat\PP2\lab6\test.txt"

if os.access(path1, os.F_OK) and os.access(path1, os.R_OK) and os.access(path1, os.W_OK) and os.access(path1, os.X_OK):
    os.remove(path1)
    print("File has been removed")
else:
    print("File does not exist")