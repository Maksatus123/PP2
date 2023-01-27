n = int(input())
l = list()
s = set()
d = dict()
while n != 0:
    l.append(n)
    n = int(input())
for i in l:
    s.add(i)
for i in range(len(l)):
    d[l[i]] = l.count(l[i])

print("Min number:", min(l),"\n", "Max number:", max(l),"\n", "Sum:",sum(l),"\n", "Average:", sum(l) / len(l))

for i in s:
    print(i, end=" ")
print("")
for i, j in d.items():
    print(str(i)+':', j)