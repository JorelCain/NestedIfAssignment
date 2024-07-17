place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You light a torch and proceed safely into the cave.")
    elif action == "proceed in the dark":
        print("You proceed into the cave blind. You fall and hit your head on a rock because you can't see anything. Game Over.")
    else:
        pass