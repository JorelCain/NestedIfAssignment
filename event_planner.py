attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

vegetarian = input("Would you like vegetarian food?")
print("Veggie Delight Caterers") if vegetarian == "yes" else print("Gourmet Meals Caterers")
