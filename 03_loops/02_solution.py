n = int(input("Enter the range: "))
sum_even=0




for i in range(0,n+1):
    if i % 2 == 0:
        sum_even += i
print(sum_even) 