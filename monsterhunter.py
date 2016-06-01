action = ""

inventory = ("sword",
             "shield",
             "armour",
             "health potion")
chest = ("gold", "boots")

#x and y are map co-ordinates. i & j are counters for actions
#key tracks whether the key has been found or not
x = int(1)
y = int(0)
i = int(0)
j = int(0)
key = ("key", "no")
keys = ("no")

#when the troll dies and player gets to x == 0 y ==3
#it signals the end of the game
troll = int(10)
trollx = int(0)
damage = int(0)
player = "alive"

print ("General commands:\n n goes north\n s goes south\n e goes east \n w is a mysterious function\n f is fight \n i is is inventory\n l is look")

print ("You are standing in a corridor stretching away north,\n to your left is a fireplace,\n each ghostly dying ember wroughts it's ghost upon the floor")
i += 1

while troll > int(0) and player == "alive":
    while x == 1 and y == 0 and player == "alive":
        action = input ("\nwhat do you do?")
        if action == "i":
            print ("\nYour inventory contains")
            for item in inventory:
                print (item)
        elif action == "l":
            if i == 1:
                print ("I just told you what you saw mong, scroll up")
                i += 1
            elif i == 2:
                print ("Fine...\n you are standing in a corridor stretching away north,\n to your left is a fireplace,\n each ghostly dying ember wroughts it's ghost upon the floor\n have you got it this time???")
                i += 1
            elif i > 2:
                print ("You are standing in a FUCKING corridor stretching away to the GODDAMN north,\n to your left is a SHIT GARGLING fireplace,\n and then some EDGAR ALLEN POE SHIT GOES ON")
            else:
                print ("You are standing in a corridor stretching away north,\n to your left is a fireplace,\n each ghostly dying ember wroughts it's ghost upon the floor")
                i += 1
        elif action == "f":
            if j == 0:
                print ("really? what do you want to fight?")
                j += 1
            elif j == 1:
                print ("fine you swing around like a ballerina, you magnificent douch")
                j +=1
            elif j == 2:
                print ("\n Fuck you, your twirling gets the better of you and you chop")
                input ("\n your dick and/or ovaries off and or out")
                print ("you bleed to death on the floor")
                player = "dead"
        elif action == "n":
            y += 1
        elif action == "e" or action == "s":
            print ("you cannot go that way...")
        elif action == "w":
            print ("you are now in the same position but with singed feet")
        else:
            print ("I did not understand that command")
    action = ""
    i = 0
    j = 0
    while x == 1 and y == 1:
        if j == 0:    
            print ("\nyou have found a chest")
            j += 1
            action = input ("to look inside chest type 'l'")
            if action == "l":
                input ("You find a chest, it contains" + str(chest))
                action = input ("take chest?")
                if action == "y":
                    inventory += chest
                    chest = ()
                if action == "n":
                    print ("Fine have it your way")
        else:
            action = input("\nWhat do you do?")
            if action == "l":
                print ("You see the chest again")
                print ("The chest contains" + str(chest))
                #trying to check to see if there is anything in the chest
                if "boots" in chest:
                        action = input ("take chest?")
                        if action == "y":
                            inventory += chest
                            chest = ()
                        if action == "n":
                            print ("jesus make up your mind")
                else:
                    print ("The chest is empty, like nick clegg's promises")
            elif action == "i":
                print ("\nYour inventory contains")
                for item in inventory:
                    print (item)
            elif action == "f":
                input ("you try to fight the chest")
                print ("it wins")
            elif action == "n":
                print ("You go north, into the great beyond.")
                y += 1
            elif action == "s":
                y -= 1
                j = int(0)
            elif action == "e" or action == "w":
                print ("You cannot go that way...")
            else:
                print ("Sorry i do not understand that command")   
        action = ""
    while x == 1 and y ==2:
        j = int(0)
        action = input("\nYou are at a junction. What do you do?")
        if action == "l":
            if i == 0:
                print ("You see a wall straight in front of you, it looks pretty solid\nThere are arches to the east and west\nYou hear growling coming from the east")
                i +=1
            elif 1 < i < 5:
                print ("don't start that shit again")
            else:
                print ("You see a wall straight in front of you, it looks pretty solid\nThere are arches to the east and west\nYou hear growling coming from the east")            
        elif action == "i":
            print ("\nYour inventory contains")
            for item in inventory:
                print (item)
        elif action == "f":
            print ("you charge up as high as you can and swing at the wall, it doesn't budge")
        elif action == "e":
            if keys == "yes":
                print ("You unlock the gate and come face to face with a TROLL!")
                x -= 1
            else:
                print ("There is a gate there, something moves in the dark")
        elif action == "w":
            if keys == "no":
                x += 1
                print ("you go west")
            else:
                print("As you turn to go back west rubble falls and blocks the area")
                print("You cannot go that way")
        elif action == "s":
            print ("turn tail and walk away like a sissy")
            y -= 1
        elif action == "n":
            print ("You summon up you courage and run face first into the wall")
            print ("Ouch")
        else:
            print ("i don't understand what you mean by that")
    action = ""
    while x == 2 and y == 2:
        action = input("\nIt looks like a dead end. What do you do?")
        if action == "i":
            print ("\nYour inventory contains")
            for item in inventory:
                print (item)
        elif action == "l":
            print ("You cast around in the darkness, something smells rancid")
            print ("You see a glimmer in the dark, it's a key!")
            print ("You pick up the key")
            inventory += key
            keys = "yes"
            print ("You go back to the junction")
            x -= 1
        elif action == "f":
            print ("you try to fight the dark")
            input ("you are likely to be eaten by a grue")
        elif action == "e":
            print ("you go to turn but what's that? A key. You pick it up")
            inventory += key
            keys = "yes"
            print ("you go back to the junction")
            x -= 1
        else:
            print ("i'm sorry that action has no meaning here")
    while x == 0 and y == 2 and troll > 0 and player == "alive":
        action = input("\nA troll is facing you! what do you do?")
        if action == "f":
            print ("You swing your sword valiently at the troll")
            import random
            damage = random.randint(1,5)
            troll = troll - damage
            print ("you did", damage)
            print ("the troll now has", troll, "health")
            input ("the troll swings back at you")
            print ("you block with your shield,\n however the might of the troll deals you concussive force and you die")
            print ("game over")
            player = "dead"
        elif action == "w":
            print ("you run out of the room, troll following")
            action = input("standing at the junction, troll charging, what do you do")
            if action == "f":
                print ("you widly swing your sword")
                input ("it misses the troll by a country mile")
                print ("but it hits the rope holding the gate open")
                input ("the troll's head gets caugt in the two ton doors closing")
                troll -= 4
                print ("\nthe troll is stuck and only has", troll, "health remaining")
                while troll > 0:
                    action = input("the troll is stuck and bleeding, what do you do?")
                    if action == "f":
                        print ("you swing your sword at the disabled troll's head")
                        import random
                        damage = random.randint(1,5)
                        troll = troll - damage
                        print ("you did", damage, "damage")
                        print ("the troll now has", troll, "health")
                    else:
                        print ("no you don't, finish it, he's suffering")
            elif action == "s":
                print ("you turn to run")
                input ("the troll mocks you in his troll language for cowardice")
                print ("it sounds a bit like ewooh wooh putow")
                print ("\n then it kicks you in the back turning you inside out as you fly into the chest")
                input ("i guess what's left of your armour will be left for the next guys")
                player = "dead"
            else:
                print ("I don't even know what you were trying to do")
                player = "dead"
        elif action == "e":
            print ("you run straight into the troll")
            input ("were you hoping to startle it or something?")
            print ("the troll crushes your head with one hand and goes back to sleep")
            player = "dead"
            print ("game over")
        else:
            input ("you cannot do that right now")
            print ("your hesitation has let the troll get behind you")
            print ("the troll eats you whole, you will be digested over thousands of years")
            player = "dead"

if player == "dead":
    input ("\nGAME OVER")
    print ("\nyou've lost this time")
    print ("next time try to do better")
elif troll < 1:
    print ("\nyou killed the troll")
    print ("you monster")
    print ("its an endangered species due to people like you")
else:
    print ("i don't know how you got here and i don't like it")
input ("press enter to exit")
    

