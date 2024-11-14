# age = int(input("Please state your age: "))
# day = str(input("Please enter the day: "))
# adult_ticket = 12
# child_ticket = 8
# discount = 2



# if day == "wednesday":
#     if age >= 18:
#         print(f"{adult_ticket-discount}$ for 18 and above, {discount}$ discount on Wednesdays:)")
#     else:
#         print(f"{child_ticket-discount}$ children(below 18), {discount}$ discount on Wednesdays:)")
# else:
#     if age >= 18:
#         print(f"{adult_ticket}$ for 18 and above")
#     else:
#         print(f"{child_ticket}$ children(below 18)")
    



age = int(input("Please state your age: "))
day = str(input("Please enter the day: "))
price = 12 if age >=18 else 8


if day =="wednesday":
    price= price-2
    # price-=2 same as above
    print(f"Ticket price is: ${price}, $2 wednesday discount :)")
else:  print(f"Ticket price is: ${price}")


