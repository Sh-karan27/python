n = int(input("Enter the range: "))


if n>10:
    print("Maximum limit is up to 10!")
    exit()


sum=0

for i in range(1,11):
    if i == 5:
        continue #keyord used to skip the iteration for the given condition 
    print(n, "X", i, "=", n*i)

