order_size = str(input("Enter your coffe size: "))


need_extra_short = str(input("Need extra short? ")).lower()

if need_extra_short == "yes":
    extra_short= True
else: extra_short=False


if extra_short:
    coffee = order_size + " Coffee with extra short"
else: coffee = order_size + " Coffee"

print(coffee)
