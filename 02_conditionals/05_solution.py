weather = str(input("Whtas the weather? ")).lower()


if weather =="sunny":
    activity ="Go for walk"
elif weather =="rain":
    activity = "Read a book"
elif weather =="snow":
    activity = "Snow Fight!"
else: activity = "duck around"

print(activity)