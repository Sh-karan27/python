spices = str(input("Enter species: ")).lower()
age =int(input("Enter age of pet: "))



if spices == "dog":
    if age <= 2:
        food = "Puppy food"
    else: food = "Doggo food"
elif spices =="cat":
    if age>5:
        food = "Pussy food"
    else: food="Hello kitty food"

print(food)
