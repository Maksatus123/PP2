import datetime
#1
t = datetime.datetime.today() - datetime.timedelta(5)
print(t)

#2
print(datetime.datetime.today() - datetime.timedelta(1))
print(datetime.datetime.today())
print(datetime.datetime.today() + datetime.timedelta(1))

#3
dt = datetime.datetime.today().replace(microsecond=0)

print(dt)
#4
dt1 = datetime.datetime.now()
dt2 = datetime.datetime.now() - datetime.timedelta(days = 19)
delta = dt1 - dt2
print(delta)
