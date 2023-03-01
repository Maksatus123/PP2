import re

def zeroOrMoreB():
    txt = input()
    x = re.findall("ab*", txt)
    print(x)
# zeroOrMoreB()

def twoORthree():
    txt = input()
    x = re.findall("ab{2,3}", txt)
    print(x)
# twoORthree()

def sequenceOfLowerLetters():
    txt = input()
    l = []
    txt = txt.split('_')
    for i in range(0, len(txt) - 1):
        x1 = re.search("[a-z]", txt[i])
        x2 = re.search("[a-z]", txt[i + 1])
        if x1 and x2:
            l.append(txt[i] + "_" + txt[i + 1])
    print(l)
# our problem was if a_i_a_b it printed a_i and a_b, I fixed this problem via using two searches that return object
# sequenceOfLowerLetters()

def findAa():
    txt = input()
    x = re.findall("[A-Z][a-z]+", txt)
    print(x)
# findAa()

def startWithAEndWithB():
    txt = input()
    x = re.findall("a.*b", txt)
    print(x)
# startWithAEndWithB()

def replace():
    txt = input()
    x = txt
    # pattern = ",. "
    x = re.sub("\s", ":", txt)
    x = re.sub("[.]", ":", x)
    x = re.sub(",", ":", x)
# replace()

def snakeToCamel():
    txt = input()
    x = txt.split("_")
    for i in range(1, len(x)):
        x[i] = x[i].capitalize()
    for x in x:
        print(x, end='')
# snakeToCamel()

def splitUpper():
    txt = input()
    x = txt
    for i in range(0, len(x)):
        if x[i].isupper():
            x1 = x[:i]
            x2 = x[i + 1:]
            x = x1 + ' ' + x2
    # l = x.split(' ')
    l = re.split("\s", x)
    l2 = []
    for i in l:
        if len(i) != 0:
            l2.append(i)
    print(l2)
# splitUpper()

def splitUpper2():
    txt = input()
    x = re.sub(r"([A-Z][a-z]+)", r" \1", txt).strip()
    print(x)
# splitUpper2()

def camelToSnake():
    txt = input()    
    x = re.sub(r"([A-Z][a-z]+)", r" \1", txt).strip()
    # camelCase
    # print(x)
    # camel Case
    x = x.split(' ')
    s = ''
    for i in range(0, len(x)):
        s += x[i].lower() + '_'
    print(s[:-1])
# camelToSnake()