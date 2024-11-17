def Even(limit):
    for i in range(2,limit+1,2):
        yield i

for num in Even(10):
    print(num)