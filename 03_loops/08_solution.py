number = int(input("Enter number"))


is_prime=True


if number>1:
    for i in range(2,number):
        print(i)
        if number%i==0:
            is_prime =False
            break
print(is_prime)
