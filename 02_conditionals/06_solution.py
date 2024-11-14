distance = int(input("Enter your distance: "))



if distance <= 3:
    transport = "Walk"
elif distance <=15:
    transport = "Bike"
else: transport = "Car"

print(transport)