attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

vegetarian = input("Would you like vegetarian food?")
if vegetarian == "yes":
    print("Veggie delight caterers is the best place for vegetarian food")
elif vegetarian == "no":
    print("Gourmet Meals Caterers is the best choice for you")
