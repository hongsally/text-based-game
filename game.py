name = input("Enter your name: ")
print(f'Hello{name} welcome to happy village')
job = input("Are you are merchant or an adventurer: ")
if job == "adventurer":
    king = input("Wow awesome, do you want to visit the king?")
    if king == "yes":
        trip = input("You go to the castle to visit the king. He ask you if you can defeat a dragon, will you go?")
        if trip == "yes":
            men = int(input("you go the the mountain where the dragon lives. How many help will you take to help you?"))
            if men < 5:
                print("you didnt have enough people to help you, You were eaten by dragon")
            elif men > 7:
                print("your crew broke out in a fight and one man killed you")
            else:
                print("You have defeated the drangon with your crew")
if job == "merchant":
    print("WE DONT NEED MORE MERCHANTS GET OUT")
elif king == "no":
    print("You have been placed in prison for refusing the king")
elif trip == "no":
    print("You have been placed in prison for refusing the king")