import time
import random
import art
import screen_functions as func

all_stats =list()

# Booleans to check status
skill_check = False
sane = True
alive = True

# Variables for stats/name/mods
username = " "
charisma = 0    
charisma_mod = 0    # Persuasion
strength = 0
strength_mod = 0    #Strength rolls
determination = 0
dexterity = 0
dexterity_mod = 0   #Picking Locks etc
sanity = 0
health = 0
health_mod = 0
attack = 0
attack_mod = 0

# Main Inventory
inventory = []

# Main Inventory
inventory = []

#Play Again?
def replay_game():
    play_again = input("""
    Would you like to play again?
    Yes  |  No  """)
    play_again = play_again.lower()
    if play_again == "yes":
        func.spacer(2)
        stat_wipe()
        print("\033c")
        intro()
    if play_again == "no":
        func.spacer(2)
        print("Thanks for playing!")
        func.spacer(20)
        print("\033c")
    else:
        func.spacer(1)
        print("I'm just going to take that as a no.")
        func.spacer(20)
        print("\033c")

def stats_roll():
    stats = list()
    while len(stats) < 4:
        stats.append(random.randint(1, 6))
    stats.remove(min(stats))
    stat_indv = sum(stats)
    all_stats.append(stat_indv)
    return all_stats

def create_char():
    stats_roll()
    stats_roll()
    stats_roll()
    stats_roll()
    stats_roll()
    stats_assign()

# Stat Table
def stat_table():
    print(f"            {art.bcolors.OKYELLOW}Your Stats{art.bcolors.ENDC}")
    print(f"{art.bcolors.OKRED}Sanity{art.bcolors.ENDC}: {sanity}        {art.bcolors.OKRED}Dexterity{art.bcolors.ENDC}: {dexterity}")
    print(f"{art.bcolors.OKRED}Strength{art.bcolors.ENDC}: {strength}        {art.bcolors.OKRED}Charisma{art.bcolors.ENDC}: {charisma}")
    print(f"{art.bcolors.OKRED}Determination{art.bcolors.ENDC}: {determination}\n")
# Sanity & Health Checks
# Called on loss of these stats to check level/punish/reward
def health_check():
    global alive
    global health
    if health <= 0:
        alive = False
        func.spacer(1)
        print("Unfortunately, your health is now zero...")
        func.spacer(0.5)
        print("You have died...")
        func.spacer(3)
        func.clear_screen()
        art.gameover_screen()
    else:
        alive = True

def sanity_check():
    global sane
    global sanity
    global health

    sanity_attempt = 0

    if sanity <= 0:
        sane = False
        func.spacer(1)
        print("Bad luck, you've gone completely insane...")
        func.spacer(1)
        print("An abandoned hospital is no place for the insane.")
        func.spacer(1)
        print("You get lost amongst the commotion, muttering something about an all seeing eye, ironically, never to be seen again.")
        func.spacer(3)
        func.clear_screen()
        art.gameover_screen()
    elif sanity in range(11, 15) and sanity_attempt == 0:
        func.spacer(1)
        print("You're starting to go a bit mad?")
        func.spacer(1)
        print("QUICK! Let's do some simple maths to keep you sharp!")
        func.spacer(0.5)
        sanity_maths = input("What's 46 multiplied by 82? \n")
        if sanity_maths == str(46*82):
            func.spacer(3)
            print("Good work! You're still sharp")
            sanity += 1
            sanity_attempt += 1
        else:
            func.spacer(3)
            print("I thought that would be easy for you...guess not.")
            sanity -= 2
            func.spacer(1)
            print("The confusion of doing maths has somehow injured you.")
            health -= 2
            health_check()
            print(f"Your health is now {art.bcolors.BOLD}{art.bcolors.OKRED}{health}{art.bcolors.ENDC}HP!")
            sanity_attempt += 1
            sane = True
    elif sanity in range(6, 10) and sanity_attempt == 0:
        func.spacer(1)
        print("You're going even madder!")
        func.spacer(1)
        print("WHAT'S THAT?!")
        func.spacer(2)
        print("You've lashed out to attack the figure...it was your own arm...2 damage!")
        health -= 2
        health_check()
        func.spacer(1)
        print(f"Your health is now {art.bcolors.BOLD}{art.bcolors.OKRED}{health}{art.bcolors.ENDC}HP!")
        sanity_attempt += 1
        sane = True
    elif sanity in range(1, 5) and sanity_attempt == 0:
        sanity_attempt += 1
        func.spacer(1)
        print("You're properly mad...")
        func.spacer(1)
        print("We're going to need some real brain teaser to bring you back...")
        func.spacer(1)
        sanity_ceaser = input("""
        DECODE THIS SENTENCE: Lw'v RN wr eh pdg vrphwlphv
        """)
        sanity_ceaser = sanity_ceaser.lower()
        if sanity_ceaser.strip() == "it's ok to be mad sometimes" or "its ok to be mad sometimes":
            func.spacer(1)
            print("HAIL CEASER! You got it!")
            sanity += 2
            health += 2
            func.spacer(0.5)
            print("You've had a little pick me up, how smug.")
            print(f"Your health is now {art.bcolors.BOLD}{art.bcolors.OKRED}{health}{art.bcolors.ENDC}HP!")
            sane = True
        else:
            func.spacer(1)
            print("Sorry...wkdw'v qrw lw.")
            func.spacer(2)
            health -= 2
            health_check()
            print("You've hit yourself in frustration...but a bit too hard.")
            print(f"You now have {art.bcolors.BOLD}{art.bcolors.OKRED}{health}{art.bcolors.ENDC}HP!")
            sane = True
    else:
        sane = True

# Skill Checks
# Uses player mods to roll against a random number (emulating D&D DC rolls)
def veryeasy_skill(modifier):
    global charisma_mod
    global dexterity_mod
    global strength_mod
    global skill_check

    skill_roll = random.randint(1, 20)

    if skill_roll + modifier <= 5:
        print("You have failed the check!")
        print(f"You only rolled a {art.bcolors.BOLD}{art.bcolors.OKRED}{skill_roll}{art.bcolors.ENDC}, which wasn't enough even with your + {art.bcolors.BOLD}{art.bcolors.OKRED}{modifier}{art.bcolors.ENDC}!")
        skill_check = False
    else:
        print(f"That's a {art.bcolors.BOLD}{art.bcolors.OKRED}{skill_roll}{art.bcolors.ENDC} + {art.bcolors.BOLD}{art.bcolors.OKRED}{modifier}{art.bcolors.ENDC}! You pass the check!")
        skill_check = True

def easy_skill(modifier):
    global charisma_mod
    global dexterity_mod
    global strength_mod
    global skill_check

    skill_roll = random.randint(1, 20)

    if skill_roll + modifier <= 10:
        print("You have failed the check!")
        print(f"You only rolled a {art.bcolors.BOLD}{art.bcolors.OKRED}{skill_roll}{art.bcolors.ENDC}, which wasn't enough even with your + {art.bcolors.BOLD}{art.bcolors.OKRED}{modifier}{art.bcolors.ENDC}!")
        skill_check = False
    else:
        print(f"That's a {art.bcolors.BOLD}{art.bcolors.OKRED}{skill_roll}{art.bcolors.ENDC} + {art.bcolors.BOLD}{art.bcolors.OKRED}{modifier}{art.bcolors.ENDC}! You pass the check!")
        skill_check = True

def med_skill(modifier):
    global charisma_mod
    global dexterity_mod
    global strength_mod
    global skill_check

    skill_roll = random.randint(1, 20)

    if skill_roll + modifier <= 15:
        print("You have failed the check!")
        print(f"You only rolled a {art.bcolors.BOLD}{art.bcolors.OKRED}{skill_roll}{art.bcolors.ENDC}, which wasn't enough even with your + {art.bcolors.BOLD}{art.bcolors.OKRED}{modifier}{art.bcolors.ENDC}!")
        skill_check = False
    else:
        print(f"That's a {art.bcolors.BOLD}{art.bcolors.OKRED}{skill_roll}{art.bcolors.ENDC} + {art.bcolors.BOLD}{art.bcolors.OKRED}{modifier}{art.bcolors.ENDC}! You pass the check!")
        skill_check = True

def hard_skill(modifier):
    global charisma_mod
    global dexterity_mod
    global strength_mod
    global skill_check

    skill_roll = random.randint(1, 20)

    if skill_roll + modifier <= 20:
        print("You have failed the check!")
        print(f"You only rolled a {art.bcolors.BOLD}{art.bcolors.OKRED}{skill_roll}{art.bcolors.ENDC}, which wasn't enough even with your + {art.bcolors.BOLD}{art.bcolors.OKRED}{modifier}{art.bcolors.ENDC}!")
        skill_check = False
    else:
        print(f"That's a {art.bcolors.BOLD}{art.bcolors.OKRED}{skill_roll}{art.bcolors.ENDC} + {art.bcolors.BOLD}{art.bcolors.OKRED}{modifier}{art.bcolors.ENDC}! You pass the check!")
        skill_check = True

def veryhard_skill(modifier):    # Basically Impossible
    global charisma_mod
    global dexterity_mod
    global strength_mod
    global skill_check

    skill_roll = random.randint(1, 20)

    if skill_roll + modifier <= 23:
        print("You have failed the check!")
        print(f"You only rolled a {art.bcolors.BOLD}{art.bcolors.OKRED}{skill_roll}{art.bcolors.ENDC}, which wasn't enough even with your + {art.bcolors.BOLD}{art.bcolors.OKRED}{modifier}{art.bcolors.ENDC}!")
        skill_check = False
    else:
        print(f"That's a {art.bcolors.BOLD}{art.bcolors.OKRED}{skill_roll}{art.bcolors.ENDC} + {art.bcolors.BOLD}{art.bcolors.OKRED}{modifier}{art.bcolors.ENDC}! You pass the check!")
        skill_check = True

# # # Character Creator Functions # # #
# Stats Roller - Rolls 4d20, removes the lowest values, adds them together
# Assigns Modifers based on stat scores
def mods_assign():
    global strength
    global strength_mod
    global charisma
    global charisma_mod
    global dexterity
    global dexterity_mod

    if strength in range(18,20):
        strength_mod = 4
        strength_mod
    elif strength in range(16,17):
        strength_mod = 3
        strength_mod
    elif strength in range(14,15):
        strength_mod = 2
        strength_mod
    elif strength in range(12,13):
        strength_mod = 1
        strength_mod
    elif strength in range(8,9):
        strength_mod -= 1
        strength_mod
    elif strength in range(6,7):
        strength_mod -= 2
        strength_mod
    elif strength in range(4,5):
        strength_mod -= 3
        strength_mod
    else:
        strength_mod = strength_mod
    
    if charisma in range(18,20):
        charisma_mod = 4
    elif charisma in range(16,17):
        charisma_mod = 3
    elif charisma in range(14,15):
        charisma_mod = 2
    elif charisma in range(12,13):
        charisma_mod = 1
    elif charisma in range(8,9):
        charisma_mod -= 1
    elif charisma in range(6,7):
        charisma_mod -= 2
    elif charisma in range(4,5):
        charisma_mod -= 3
    else:
        charisma_mod = charisma_mod

    if dexterity in range(18,20):
        dexterity_mod = 4
    elif dexterity in range(16,17):
        dexterity_mod = 3
    elif dexterity in range(14,15):
        dexterity_mod = 2
    elif dexterity in range(12,13):
        dexterity_mod = 1
    elif dexterity in range(8,9):
        dexterity_mod -= 1
    elif dexterity in range(6,7):
        dexterity_mod -= 2
    elif dexterity in range(4,5):
        dexterity_mod -= 3
    else:
        dexterity_mod = dexterity_mod 

# Attack/Health Generators
def attack_scorer():
    global strength
    global sanity
    global dexterity
    global attack_mod
    global attack_score
    attack_base = strength + dexterity + sanity
    attack_base = attack_base / 3
    attack_score = int(attack_base + attack_mod)
    return attack_score

def health_scorer():
    global charisma
    global determination
    global sanity
    global health
    global health_mod

    health_base = determination + sanity + charisma
    health_base = health_base / 3
    health = int(health_base + health_mod)
    return health

# # # GAME STORY # # #
# Intro/Character Creation

# Wipes Stats for a Fresh Game
def stat_wipe():
    global username
    global charisma  
    global charisma_mod
    global strength
    global strength_mods
    global determination
    global dexterity
    global dexterity_mod
    global sanity
    global health
    global health_mod
    global attack
    global attack_mod
    global all_stats

    username = " "
    charisma = 0    
    charisma_mod = 0    # Persuassion
    strength = 0
    strength_mod = 0    #Strength rolls
    determination = 0
    dexterity = 0
    dexterity_mod = 0   #Picking Locks etc
    sanity = 0
    health = 0
    health_mod = 0
    attack = 0
    attack_mod = 0
    all_stats = list()

def stats_assign():
    global charisma
    global strength
    global determination
    global sanity
    global dexterity
    global username
    
    print(f"OK {art.bcolors.OKBLUE}{username}{art.bcolors.ENDC}. Let's roll your stats...")
    func.spacer(2)
    print(f"You rolled {art.bcolors.BOLD}{art.bcolors.OKRED}{all_stats}{art.bcolors.ENDC}")
    func.spacer(0.5)
    print("Let's put the highest number on what you think is most important.")
    func.spacer(1)
    print(f"{art.bcolors.BOLD}{art.bcolors.OKRED}Dexterity{art.bcolors.ENDC} and {art.bcolors.BOLD}{art.bcolors.OKRED}Strength{art.bcolors.ENDC} decide how hard you hit.")
    func.spacer(0.5)
    print(f"{art.bcolors.BOLD}{art.bcolors.OKRED}Charisma{art.bcolors.ENDC} and {art.bcolors.BOLD}{art.bcolors.OKRED}Determination{art.bcolors.ENDC} effect how long you'll live.")
    func.spacer(0.5)
    print(f"but {art.bcolors.BOLD}{art.bcolors.OKRED}Sanity{art.bcolors.ENDC} holds it all together...")
    func.spacer(2)
    while len(all_stats) != 0:
        func.spacer(1)
        stat_table()
        stat_request = input(f"""
        What is your most important stat?
        {art.bcolors.OKRED}Charisma | Sanity | Strength | Determination | Dexterity{art.bcolors.ENDC}?
        """)
        quest = stat_request.lower()
        if stat_request == "charisma" and charisma == 0:
            charisma = max(all_stats)
            print(f"Your {art.bcolors.BOLD}{art.bcolors.OKRED}Charisma{art.bcolors.ENDC} score is {art.bcolors.BOLD}{art.bcolors.OKRED}{charisma}{art.bcolors.ENDC}")
            all_stats.remove(max(all_stats))
            print(f"Your remaining stats are {art.bcolors.BOLD}{art.bcolors.OKRED}{all_stats}{art.bcolors.ENDC}")
            func.spacer(1)
        elif stat_request == "dexterity" and dexterity == 0:
            dexterity = max(all_stats)
            print(f"Your {art.bcolors.BOLD}{art.bcolors.OKRED}Dexterity{art.bcolors.ENDC} score is {art.bcolors.BOLD}{art.bcolors.OKRED}{dexterity}{art.bcolors.ENDC}")
            all_stats.remove(max(all_stats))
            print(f"Your remaining stats are {art.bcolors.BOLD}{art.bcolors.OKRED}{all_stats}{art.bcolors.ENDC}")
            func.spacer(1)
        elif stat_request == "strength" and strength == 0:
            strength = max(all_stats)
            print(f"Your {art.bcolors.BOLD}{art.bcolors.OKRED}Strength{art.bcolors.ENDC} score is {art.bcolors.BOLD}{art.bcolors.OKRED}{strength}{art.bcolors.ENDC}")
            all_stats.remove(max(all_stats))
            print(f"Your remaining stats are {art.bcolors.BOLD}{art.bcolors.OKRED}{all_stats}{art.bcolors.ENDC}")
            func.spacer(1)
        elif stat_request == "sanity" and sanity == 0:
            sanity = max(all_stats)
            print(f"Your {art.bcolors.BOLD}{art.bcolors.OKRED}Sanity{art.bcolors.ENDC} score is {art.bcolors.BOLD}{art.bcolors.OKRED}{sanity}{art.bcolors.ENDC}")
            all_stats.remove(max(all_stats))
            print(f"Your remaining stats are {art.bcolors.BOLD}{art.bcolors.OKRED}{all_stats}{art.bcolors.ENDC}")
            func.spacer(1)
        elif stat_request == "determination" and determination == 0:
            determination = max(all_stats)
            print(f"Your {art.bcolors.BOLD}{art.bcolors.OKRED}Determination{art.bcolors.ENDC} score is {art.bcolors.BOLD}{art.bcolors.OKRED}{determination}{art.bcolors.ENDC}")
            all_stats.remove(max(all_stats))
            print(f"Your remaining stats are {art.bcolors.BOLD}{art.bcolors.OKRED}{all_stats}{art.bcolors.ENDC}")
            func.spacer(1)
        else:
            print("Sorry, can you say that again?")
            func.spacer(1)
    func.spacer(2)
    attack_scorer()
    print(f"Your {art.bcolors.OKCYAN}attack score{art.bcolors.ENDC} is {art.bcolors.OKCYAN}{attack_score}{art.bcolors.ENDC}!")
    func.spacer(2)
    health_scorer()
    print(f"Your {art.bcolors.HEADER}health{art.bcolors.ENDC} is {art.bcolors.OKRED}{health}HP{art.bcolors.ENDC}!")
    func.spacer(3)
    sleep_or_go()

def intro():
    global username
    func.spacer(1)
    art.gametitle_screen()
    func.spacer(5)
    print(f"Your nightmare begins in the {art.bcolors.BOLD}{art.bcolors.OKYELLOW}City of London{art.bcolors.ENDC}.")
    func.spacer(1)
    print("The Capital has been under strict lockdown rules for several months.")
    func.spacer(1)
    print(f"The population is being overun by a {art.bcolors.BOLD}{art.bcolors.OKYELLOW}new variant{art.bcolors.ENDC} which is 99 percent infectious.")
    func.spacer(1)
    print("Your last memory is calling 999 as you begin to feel unwell...")
    func.spacer(1)
    username = input("Survivor, What Is Your Name? ")
    username = username.capitalize()
    func.spacer(1)
    print(f"Wakey Wakey {art.bcolors.OKBLUE}{username}{art.bcolors.ENDC}!")
    func.spacer(2)
    print(f"{art.bcolors.OKBLUE}{username}'s{art.bcolors.ENDC} eyes open")
    func.spacer(1)
    print("You find yourself in a hospital bed.")
    func.spacer(0.5)
    print(f"Take in your surroundings {art.bcolors.OKBLUE}{username}{art.bcolors.ENDC}. Things aren't what they seem out there!")
    func.spacer(2)
    create_char()

def sleep_or_go():
    print(f"OK {art.bcolors.OKBLUE}{username}{art.bcolors.ENDC}! Shall we get on with it?")
    sleep_choice = input("""Or would you like to move forward, or sleep and try again tomorrow?
    Go  |  Sleep

    """)
    sleep_choice = sleep_choice.lower()
    if sleep_choice.strip() == "go":
        func.spacer(1)
        print(f"OK {art.bcolors.OKBLUE}{username}{art.bcolors.ENDC}! Let's go!")
        func.spacer(1)
    elif sleep_choice.strip() == "sleep":
        func.spacer(1)
        print(f"OK {art.bcolors.OKBLUE}{username}{art.bcolors.ENDC}, let's have a snooze...")
        func.spacer(1)
        stat_wipe()
        intro()
    else:
        func.spacer(1)
        print("Sorry, I didn't quite get that?")
        sleep_or_go()

# ROOM TWO - BEDROOM
def bedroom():
    func.spacer(1)
    art.bedroom_title_art()
    print("You look around the room, the lights are flickering on and off.")
    func.spacer(2)
    print(f"Whilst searching the room you come across a {art.bcolors.BOLD}{art.bcolors.OKYELLOW}chest of drawers{art.bcolors.ENDC}, a {art.bcolors.BOLD}{art.bcolors.OKYELLOW}wardrobe{art.bcolors.ENDC} and a {art.bcolors.BOLD}{art.bcolors.OKYELLOW}medicine cabinet{art.bcolors.ENDC}.")
    func.spacer(2)
    bedroom_choice1()
    
def bedroom_choice1():
    response = input(f"Would you like to loot the {art.bcolors.BOLD}{art.bcolors.OKYELLOW}chest of drawers{art.bcolors.ENDC}? \nYes / No?\n")
    response = response.lower()
    if response == "yes":
        func.spacer(2)
        print(f"You loot the {art.bcolors.BOLD}{art.bcolors.OKYELLOW}chest of drawers{art.bcolors.ENDC} and find a {art.bcolors.BOLD}{art.bcolors.OKCYAN}bottle of water{art.bcolors.ENDC}.")
        func.spacer(1)
        bedroom_choice2()
    elif response == "no":
        func.spacer(2)
        print ("You carry on looking around the room for loot.")
        func.spacer(1)
        bedroom_choice2()
    else: 
        func.spacer(2)
        print ("I didn't understand that. Please try the command again. \n")
        bedroom_choice1()
        
def bedroom_choice2():
    response = input(f"Would you like to loot the {art.bcolors.BOLD}{art.bcolors.OKYELLOW}wardrobe{art.bcolors.ENDC}? \nYes / No?\n")
    response = response.lower()
    if response == "yes":
        func.spacer(2)
        print(f"You loot the {art.bcolors.BOLD}{art.bcolors.OKYELLOW}wardrobe{art.bcolors.ENDC} and find nothing of use.")
        func.spacer(1)
        bedroom_choice3()
    elif response == "no":
        func.spacer(2)
        print ("You carry on looking around the room for loot.")
        func.spacer(1)
        bedroom_choice3()
    else: 
        func.spacer(2)
        print ("I didn't understand that. Please try the command again. \n")
        bedroom_choice2()

def bedroom_choice3():
    global health
    response = input(f"Would you like to loot the {art.bcolors.BOLD}{art.bcolors.OKYELLOW}medicine cabinet{art.bcolors.ENDC}? \nYes / No?\n")
    response = response.lower()
    if response == "yes":
        func.spacer(2)
        print(f"You loot the {art.bcolors.BOLD}{art.bcolors.OKYELLOW}medicine cabinet{art.bcolors.ENDC} and find a {art.bcolors.BOLD}{art.bcolors.OKCYAN}first aid kit{art.bcolors.ENDC} and then you head for the exit.")
        health += 3
        print(f"Your {art.bcolors.HEADER}health{art.bcolors.ENDC} is now {art.bcolors.OKRED}{health}HP{art.bcolors.ENDC}!")
        func.spacer(1)
        hallway()
        
    elif response == "no":
        func.spacer(2)
        print ("You head towards the exit.")
        func.spacer(1)
        hallway()
    else: 
        func.spacer(2)
        print ("I didn't understand that. Please try the command again. \n") 
        func.spacer(1)
        bedroom_choice3()

# ROOM THREE - HALLWAY
def hallway():
    print("Entering a dimly lit hallway, you take in your surroudings.")
    func.spacer(1)
    print("You see 2 doors, the right is closed and the other thrown wide open, from a quick glance it looks to be a surgery room.")
    func.spacer(3)
    hallwayoptions()

def hallwayoptions():
    response = input("Do you want to go right or left?\n")
    response = response.lower()
    func.spacer(1)
    if response == "left":
        print("Eager to see if you can arm yourself, you step into the room.")
        func.spacer(1)
        surgery_room()
    elif response == "right":
        print("The door opens with ease as you step inside.")
        func.spacer(1)
        morgue()
    else:
        print("I know the hallway is nice but you can't stay here.")
        hallwayoptions()

#ROOM THREE POINT FIVE - SURGERY

def surgery_room():
    art.surgery_title_art()
    func.spacer(2)
    attack_scorer()
    print("You find yourself in a cold, barren room.")
    func.spacer(1)
    print(f"It looks like this was once a surgery, but all that's now left is {art.bcolors.BOLD}{art.bcolors.OKYELLOW}blood-stained scrubs{art.bcolors.ENDC} and chilled tables.")
    surgery_options()

def surgery_options():
    global attack_mod
    global attack_score
    global strength
    global dexterity
    global sanity
    global health
    global response

    func.spacer(2)    
    print("You can see:")
    print(f"{art.bcolors.BOLD}{art.bcolors.OKYELLOW}A pile of bloody scrubs{art.bcolors.ENDC} to your left.")
    print(f"{art.bcolors.BOLD}{art.bcolors.OKYELLOW}A surgeons drawer{art.bcolors.ENDC} in front of you.")
    print(f"{art.bcolors.BOLD}{art.bcolors.OKYELLOW}A door{art.bcolors.ENDC} to the right.")
    func.spacer(0.5)
    print("The door is still open behind you.")
    func.spacer(0.5)
    surgery_choices()

def surgery_choices():
    global response
    global attack_mod
    global sanity
    print("Which direction would you like to go?")
    response = input("Left  |  Right  |  Forward  |  Back  \n")
    response = response.lower()
    if response == "forward" and "scalpel" not in inventory:
        func.spacer(1)
        print(f"You loot the {art.bcolors.BOLD}{art.bcolors.OKYELLOW}surgeons drawer{art.bcolors.ENDC} and find a {art.bcolors.BOLD}{art.bcolors.OKCYAN}scalpel{art.bcolors.ENDC}.")
        attack_mod += 2 
        inventory.append("scalpel")
        response = input("Left  |  Right  |  Back  \n")
        response = response.lower()
        if response == "left" and "zombie finger" not in inventory:
            func.spacer(1)
            zombie_scrubs()
        elif response == "right":
            func.spacer(1)
            print("You walk down a long, winding corridor...")
            morgue()
        elif response == "back":
            func.spacer(1)
            surgery_choices()
        else:
            surgery_choices()
    elif response == "left" and "zombie finger" not in inventory:
        func.spacer(1)
        zombie_scrubs()
    elif response == "left" and "zombie finger" in inventory:
        func.spacer(0.5)
        print("You've done this already, better cheese it in case there's more zombies!")
        sanity -= 1
        sanity_check()
        func.spacer(1)
        print("The repetition is driving you slowly insane")
        surgery_options()    
    elif response == "right":
        func.spacer(1)
        print("You walk down a long, winding corridor...")
        morgue()
    elif response == "back":
        func.spacer(1)
        hallwayoptions()
    else:
        func.spacer(1)
        print ("I didn't understand that. Please try the command again.")
        response = input("Left  |  Right  |  Forward  |  Back  \n")
        response = response.lower()
        if response == "forward" and "scalpel" not in inventory:
            func.spacer(1)
            print("You loot the drawer and find a SCALPEL.")
            attack_mod = attack_mod + 2
            inventory.append("scalpel")
            surgery_choices()
        elif response == "left" and "zombie finger" not in inventory:
            func.spacer(1)
            zombie_scrubs()
        elif response == "forward" and "scalpel" in inventory:
            func.spacer(0.5)
            print("You've already got the scalpel, get a move on please!")
            sanity -= 1
            sanity_check()
            func.spacer(1)
            print("The repitition is driving you slowly insane")
            surgery_options()
        elif response == "left" and "zombie finger" in inventory:
            func.spacer(0.5)
            print("You've done this already, better cheese it in case there's more zombies!")
            sanity -= 1
            sanity_check()
            func.spacer(1)
            print("The repitition is driving you slowly insane")
            surgery_options()
        elif response == "right":
            func.spacer(1)
            print("You walk down a long, winding corridor...")
            morgue()
        elif response == "back":
            func.spacer(1)
            hallwayoptions()
        else:
            surgery_choices()

# ROOM FOUR - MORGUE
def morgue():
    art.morgue_title_art()
    func.spacer(1)
    print(f"\n{art.bcolors.OKBLUE}{username}{art.bcolors.ENDC}" + " enters the morgue.")
    func.spacer(1)
    print("'These places are supposed to be clean!'")
    func.spacer(1)
    print("But there was blood all over the place.")
    func.spacer(1)
    print("The room had an eerie feel to it.")
    func.spacer(1)
    print("Not only did it look like a massacre had gone on in here, but it was half ransacked!")
    func.spacer(1)
    print(f"{art.bcolors.OKBLUE}{username}{art.bcolors.ENDC} spots an unopened works {art.bcolors.BOLD}{art.bcolors.OKYELLOW}locker{art.bcolors.ENDC} and an unlocked {art.bcolors.BOLD}{art.bcolors.OKYELLOW}freezer drawer{art.bcolors.ENDC}.")
    func.spacer(1)
    morgue1()

def morgue1():
    response = input(f"Would you like to look in the {art.bcolors.BOLD}{art.bcolors.OKYELLOW}freezer drawer{art.bcolors.ENDC}? \nYes / No?\n")
    response = response.lower()
    if response == "yes":
        func.spacer(1)
        print(f"You look inside the {art.bcolors.BOLD}{art.bcolors.OKYELLOW}freezer drawer{art.bcolors.ENDC} to find a frozen body, but this was different.")
        func.spacer(1)
        print("It would seem that the body had an onset of necrosis, pretty badly.")
        func.spacer(1)
        print("'I wonder what caused this?'")
        func.spacer(1)
        morgue2()
    elif response == "no":
        func.spacer(1)
        print("Maybe it is too much to risk,")
        func.spacer(1)
        print("You decide to pass on the possible fresh human popsickle.")
        func.spacer(1)
        morgue2()
    else: 
        func.spacer(1)
        print ("I didn't understand that. Please try the command again. \n")
        morgue1()

def morgue2():
    response = input(f"Would you like to try your luck with the {art.bcolors.BOLD}{art.bcolors.OKYELLOW}locker{art.bcolors.ENDC} {art.bcolors.OKBLUE}{username}{art.bcolors.ENDC}?\nThere could be some really useful items inside. \nYes / No?\n")
    response = response.lower()
    if response == "yes":
        func.spacer(1)
        print(f"You open the {art.bcolors.BOLD}{art.bcolors.OKYELLOW}locker door{art.bcolors.ENDC} and find a couple of items.")
        func.spacer(1)
        print(f"There is some sort of {art.bcolors.BOLD}{art.bcolors.OKYELLOW}Robotic arm (r){art.bcolors.ENDC} and what appears to an ancient {art.bcolors.BOLD}{art.bcolors.OKYELLOW}Sceptre (s){art.bcolors.ENDC}")
        func.spacer(1)
        print("You can only carry one,")
        func.spacer(1)
        locker_choice()
    elif response == "no":
        func.spacer(1)
        print(f"I really think you should look in the {art.bcolors.BOLD}{art.bcolors.OKYELLOW}locker{art.bcolors.ENDC}.")
        func.spacer(1)
        morgue2()
    else: 
        func.spacer(1)
        print("I didn't understand that. Please try the command again. \n")
        morgue2()

def locker_choice():
    global strength_mod
    global dexterity_mod
    response = input(f"which do you choose?\n{art.bcolors.BOLD}{art.bcolors.OKYELLOW}Robotic arm (r){art.bcolors.ENDC} or {art.bcolors.BOLD}{art.bcolors.OKYELLOW}Sceptre (s){art.bcolors.ENDC}\n")
    response = response.lower()
    if response == "r":
        func.spacer(1)
        art.terminatorhand_art()
        func.spacer(1)
        print("Looks hefty, could be good for swinging?!\nI hope it has a laser weapon!")
        strength_mod += 4
        func.spacer(0.5)
        print(f"Your strength is now {art.bcolors.BOLD}{art.bcolors.OKRED}{strength}{art.bcolors.ENDC}!")
        func.spacer(1)
        terminator()
    elif response == "s":
        func.spacer(1)
        art.sceptre_art()
        func.spacer(1)
        print("I'm no doctor, but I bet this will cause some damage! You even feel more nimble")
        dexterity_mod += 4
        func.spacer(0.5)
        print(f"Your {art.bcolors.BOLD}{art.bcolors.OKRED}dexterity{art.bcolors.ENDC} is now {art.bcolors.BOLD}{art.bcolors.OKRED}{dexterity}{art.bcolors.ENDC}!")
        func.spacer(1)
        loki()
    else:
        func.spacer(1)
        print ("I didn't understand that. Please try the command again. \n")
        locker_choice()

def exit():
    print("You cautiously exit the room minding the fridge section on your way out.")
    func.spacer(1)

# ZOMBIE ATTACK - Plays against attack score, zom's is randomly generated
def zombie_scrubs():
    global attack_mod
    global attack_score
    global strength
    global dexterity
    global sanity
    global health

    print("The pile of bloody scrubs slowly begins to shuffle on the spot...")
    func.spacer(2)
    print("A half decayed, undead husk is dragging itself out from beneath the piles!")
    zom_attack = random.randint(8, 15)
    if attack_score > zom_attack:
        func.spacer(0.5)
        print("The zombie mass shuffles towards you...")
        func.spacer(0.5)
        print("But they're no match for your quick reactions. You easily dispose of them")
        sanity -= 1
        sanity_check()
        health -= 2
        health_check()
        inventory.append("zombie finger")
        print(f"The bugger tried to scratch you! Your health is now {art.bcolors.BOLD}{art.bcolors.OKRED}{health}{art.bcolors.ENDC} and you don't feel so sane anymore...")
        func.spacer(0.5)
        print("You swiped his at his finger and it broke right off, maybe it will be useful later.")
        func.spacer(0.5)
        art.zombiefinger_art()
        func.spacer(1)
        print("What now zombie killer? That door?")
        response = input("Yes  |  No  \n")
        response = response.lower()

        if response == "yes":
            morgue()
        elif response == "no":
            print("Fine! We'll head back.")
            surgery_choices()
        else:
            print("Sorry, I didn't quite get that? Probably your cowardly voice...")
            print("I'll assume you said head back!")
            surgery_choices()
           
    else:
        print("I don't think you can take that...")
        sanity -= 2
        sanity_check()
        func.spacer(0.5)
        print("What you saw has scarred you for life though...")
        surgery_choices()

# TERMINATOR PATH
def terminator():
    ("Coming out the morgue you're startled to a stop by the sight of a figure metres away.")
    func.spacer(2)
    print("They're hard to make out under the flickering fluorescent light but... you think they're a real person!")
    func.spacer(3)
    print("Thank the Gods, the last thing you need is to come uncomfortably close to another one of those monsters wearing human skin.")
    func.spacer(4)
    print("So you take cautious steps forward,")
    func.spacer(3)
    print("Only to freeze up as the figure takes large and steady strides towards you instead.")
    func.spacer(3)
    print("Getting closer and closer until finally they're close enough that you can see they have... a glowing red eye?")
    func.spacer(3)
    print(f"{art.bcolors.OKGREEN}Come with me if you want to live.{art.bcolors.ENDC}")
    func.spacer(1)
    print("Despite the promise of living, you are undeniably terrified of this gigantic... man?")
    func.spacer(2)
    print(f"{art.bcolors.OKGREEN}I'm a Terminator from the future and your life is important.{art.bcolors.ENDC}")
    func.spacer(2)
    print(f"{art.bcolors.OKGREEN}Firstly, these creatures must be put to an end,{art.bcolors.ENDC}")
    func.spacer(1)
    print(f"{art.bcolors.OKGREEN}I will go to the basement and kill the group in there.{art.bcolors.ENDC}")
    func.spacer(2)
    print(f"{art.bcolors.OKGREEN}The basement is too dangerous for you, grab the key to the chopper and go to the roof.{art.bcolors.ENDC}")
    func.spacer(1)
    print(f"{art.bcolors.OKGREEN}I will find you again, now go.{art.bcolors.ENDC}")
    func.spacer(1)
    terminator_run()

def terminator_run():
    func.spacer(2)
    response = input ("Will you listen to him and get to the chopper?\nYes or No\n")
    response = response.lower()

    if response == "yes":
        print ("You grab the helicopter key and go on ahead without The Terminator. Time to find an elevator.")
        func.spacer(1)
        basement()
    elif response == "no":
        print("You decide to stick by The Terminators side and follow him to eradicate the zombies in the basement.")
        func.spacer(2)
        print("This so called group is actually a horde, soon you're surrounded,")
        func.spacer(1)
        print("Bullets and blood are flying everywhere,")
        func.spacer(1)
        print("You make a valiant effort but soon enough a zombie latches onto your neck.")
        func.spacer(1)
        print("                             Survival tip - You won't be back!")
        art.gameover_screen()
    else:
        print("Despite being a robot from the future even The Terminator can not understand the language you just spoke. Give it another try.")
        func.spacer(1)
        terminator_run()

# LOKI PATH

def loki():
    print("Coming out the morgue you're startled to a stop by the sight of a figure metres away.")
    func.spacer(2)
    print("They're hard to make out under the flickering fluorescent light but... you think they're a real person!")
    func.spacer(3)
    print("Thank the Gods, the last thing you need is to come uncomfortably close to another one of those monsters wearing human skin.")
    func.spacer(3)
    print("So you take cautious steps forward,")
    func.spacer(2)
    print("Only to freeze up as the figure takes large and steady strides towards you instead.")
    func.spacer(2)
    print("Getting closer and closer until finally they're close enough that you can see they're wearing a... cape!?")
    func.spacer(2)

    print(f"{art.bcolors.OKGREEN}You're saviour is heeeere!{art.bcolors.ENDC}")
    func.spacer(3)

    print("Beyond just how absurd this person looks, you can't deny it look suits them well.")
    func.spacer(2)
    print(f"{art.bcolors.OKGREEN}I am Loki, God of Mischief and I have a glorious plan!{art.bcolors.ENDC}")
    func.spacer(2)
    print(f"{art.bcolors.OKGREEN}So listen up mortal{art.bcolors.ENDC}")
    func.spacer(2)

    print(f"{art.bcolors.OKGREEN}I say we, and by we I mean YOU. Go investigate what's in the basement over there while I go check out the security room. {art.bcolors.ENDC}")
    func.spacer(2)
    print("You could listen to him, however you do see a helicoptor key hanging up on the wall... could be a good idea check the roof.")
    func.spacer(4)
    loki_run()

def loki_run():
    func.spacer(1)
    print("Do you trust Loki?")
    response = input("Yes | No \n")
    response = response.lower()
    if response == "yes":
        func.spacer(0.5)
        print ("You listen and go ahead without Loki to search the basement. You hear groaning behind the door.")
        func.spacer(1)
        print("Stupidly, you decide to go inside.")
        func.spacer(1)
        print("As soon as the door opens, you're attacked by a group of zombies and your buried under the pile.")
        func.spacer(1)
        print("Being devoured alive...")
        func.spacer(1)
        print("Survival tip: Never trust the GOD OF MISCHIEF!")
        func.spacer(3)
        art.gameover_screen()
    elif response == "no":
        func.spacer(0.5)
        print("You decide not to trust the God of Mischief and grab the helicoptor key, intent on getting to the roof.")
        func.spacer(1)
        basement()
    else:
        func.spacer(0.5)
        print("You must give the God a clear answer.")
        func.spacer(1)
        loki_run()

# ROOM SIX - Elevator Puzzle

def basement():
    art.basement_title_art()
    func.spacer
    print("You find yourself in a dark, dingy basement.")
    func.spacer(0.5)
    print("You can hear the sounds of zombies all around...")
    func.spacer(1)
    print("Quick! What's that in front of you?!")
    number_puzzle()

def number_puzzle():
    global sanity
    global strength_mod
    global dexterity_mod
    global charisma_mod

    print("In front of you is a lock to the elevator.")
    func.spacer(5)
    art.lockclosed_image()
    func.spacer(2)
    print("Attached to it is a clue on how to get through...")
    func.spacer(5)
    func.clear_screen()

    print("  | 6 | 8 | 2 |      |     | 6 | 4 | 5 |      |     | 2 | 0 | 6 |           ")
    print("   ONE number is     |     ONE number is      |     TWO numbers are         ")
    print("correct and properly |  correct, but placed   |   correct, but placed       ")
    print("       placed.       |        wrong.          |          wrong.             ")
    print("                                                                            ")
    print("             | 7 | 3 | 8 |     |   | 7 | 8 | 0 |                            ")
    print("          NOTHING is correct   |   ONE number is                            ")
    print("                               | correct, but placed                        ")
    print("                               |       wrong.                               ")
    print("                                                                            ")
    print("                                                                            ")
    print("                                                                            ")
    print("                      THREE DIGIT NUMBERS ONLY                              ")
    print("                      DRIVES YOU SLOWLY INSANE                              ")
    print("                             BE CAREFUL!                                    ")
    print("                                                                            ")

    func.spacer(3)
    print("You could probably solve that...")
    func.spacer(2)
    puzzle_choices()

def puzzle_choices():
    global sanity
    global health
    global inventory
    
    print("What do you want to do?")
    func.spacer(1)
    puzzle_choice = input("""
    Solve the Puzzle (A)
    Rip off the lock (B)
    Check out that Thumb Scanner (C)
    Pick the lock (D)
    """)
    puzzle_choice = puzzle_choice.lower()

    if puzzle_choice == "a":
        print("OK then hot shot, give it a go!")
        func.spacer(0.5)
        puzzle_answer = input(str("Key in a three digit number, or say BACK: \n"))
        puzzle_answer = puzzle_answer.lower()
        if puzzle_answer == "052":
            func.spacer(2)
            art.lock_animation()
            print("BLOODY HELL! That's the one, let's get out of here")
            rooftop()
        elif len(puzzle_answer) != 3:
            func.spacer(0.5)
            print("I SAID THREE DIGITS! This is driving me crazy.")
            sanity -= 1
            sanity_check()
            func.spacer(0.5)
            print(f"Your {art.bcolors.BOLD}{art.bcolors.OKRED}sanity{art.bcolors.ENDC} is now {art.bcolors.BOLD}{art.bcolors.OKRED}{sanity}{art.bcolors.ENDC}!")
            puzzle_choices()
        elif puzzle_answer == "back":
            func.spacer(0.5)
            print("OK then...")
            func.spacer(1)
            number_puzzle()
        else:
            func.spacer(0.5)
            print("Try again")
            func.spacer(1)
            puzzle_answer = input(str("Key in a three digit number: \n"))
            if puzzle_answer == "052":
                func.spacer(2)
                art.lock_animation()
                print("BLOODY HELL! That's the one, let's get out of here")
                rooftop()
            elif len(puzzle_choice) != 3:
                func.spacer(0.5)
                print("I SAID THREE DIGITS! This is driving me crazy.")
                sanity -= 1
                sanity_check()
                print(f"Your {art.bcolors.BOLD}{art.bcolors.OKRED}sanity{art.bcolors.ENDC} is now {art.bcolors.BOLD}{art.bcolors.OKRED}{sanity}{art.bcolors.ENDC}!")
                puzzle_choices()
            elif puzzle_answer == "back":
                func.spacer(0.5)
                print("OK then...")
                func.spacer(1)
                number_puzzle()
            else:
                func.spacer(0.5)
                print("You're not getting this!")
                sanity -= 2
                sanity_check()
                func.spacer(0.5)
                print(f"I hope you know how much this is effecting your {art.bcolors.BOLD}{art.bcolors.OKRED}sanity{art.bcolors.ENDC}!")
                puzzle_choices()
    elif puzzle_choice == "b" and "terminator hand" not in inventory:
        print(f"If you're sure, this will take a lot of {art.bcolors.BOLD}{art.bcolors.OKRED}strength{art.bcolors.ENDC} though")
        func.spacer(1)
        print("Rolling your strength check...")
        hard_skill(strength_mod)

        if skill_check == True:
            func.spacer(3)
            print("YOU'VE RIPPED IT RIGHT OFF THE HOLDER")
            func.spacer(1)
            print("Let's Go!")
            rooftop()
        else:
            func.spacer(3)
            print("Well you've messed that up.")
            func.spacer(0.5)
            print("You've even cut your hand")
            health -= 2
            health_check()
            sanity -= 1
            sanity_check()
            func.spacer(0.5)
            print(f"Your health is now {art.bcolors.BOLD}{art.bcolors.OKRED}{health}{art.bcolors.ENDC}HP! Your sanity is {art.bcolors.BOLD}{art.bcolors.OKRED}{sanity}{art.bcolors.ENDC}!")
            puzzle_choices()
    elif puzzle_choice == "b" and "terminator hand" in inventory:
        print(f"If you're sure, this will take a lot of {art.bcolors.BOLD}{art.bcolors.OKRED}strength{art.bcolors.ENDC} though")
        func.spacer(1)
        print("That Terminator hand you found should give you a bonus though!")
        func.spacer(1)
        print(f"Rolling your {art.bcolors.BOLD}{art.bcolors.OKRED}strength{art.bcolors.ENDC} check...")
        hard_skill(strength_mod)

        if skill_check == True:
            func.spacer(3)
            print("YOU'VE RIPPED IT RIGHT OFF THE HOLDER")
            func.spacer(1)
            print("Let's Go!")
            func.spacer(1)
            rooftop()
        else:
            func.spacer(3)
            print("Well you've messed that up.")
            func.spacer(0.5)
            print("You've even cut your hand")
            health -= 2
            health_check()
            sanity -= 1
            sanity_check()
            func.spacer(0.5)
            print(f"Your {art.bcolors.BOLD}{art.bcolors.HEADER}health{art.bcolors.ENDC} is now {art.bcolors.BOLD}{art.bcolors.OKRED}{health}{art.bcolors.ENDC}HP! Your {art.bcolors.BOLD}{art.bcolors.OKRED}sanity{art.bcolors.ENDC} is {art.bcolors.BOLD}{art.bcolors.OKRED}{sanity}{art.bcolors.ENDC}!")
            puzzle_choices()
    elif puzzle_choice == "c" and "zombie finger" in inventory:
        func.spacer(3)
        print("It looks like this needs the fingerprint of an employee...")
        func.spacer(0.5)
        print("Let's see if that finger you swiped earlier does anything...")
        func.spacer(1)
        art.zombiefinger_art()
        func.spacer(2.5)
        func.clear_screen()
        art. scanning_art()
        func.spacer(1)
        art.scanning_art()
        func.spacer(1)
        art.scanning_art()
        func.spacer(5)            
        func.clear_screen()
        art.success_art()
        func.spacer(1)
        print("It's unlocked! Let's go!")
        rooftop()
    elif puzzle_choice == "c" and "zombie_finger" not in inventory:
        func.spacer(3)
        print("It looks like this needs the fingerprint of an employee...")
        func.spacer(1)
        print("Shame you don't have anything like that...")
        func.spacer(0.5)
        puzzle_choices()
    
    elif puzzle_choice == "d" and "scalpel" in inventory:
        func.spacer(3)
        print(f"It will take a little {art.bcolors.BOLD}{art.bcolors.OKRED}dexterity{art.bcolors.ENDC}, but that {art.bcolors.BOLD}{art.bcolors.OKCYAN}scalpel{art.bcolors.ENDC} should help.")
        func.spacer(1)
        print("Rolling your dexterity check...")
        med_skill(dexterity_mod)
        if skill_check == True:
            func.spacer(0.5)
            print("Come on...")
            func.spacer(1)
            print("Nearly got it...")
            func.spacer(2)
            print("YOU DID IT! Let's go!")
            rooftop()
        else:
            func.spacer(2)
            print("Nice try, but you've messed it up.")
            func.spacer(0.5)
            health -= 2
            health_check()
            print(f"You've even managed to knick your finger, your {art.bcolors.BOLD}{art.bcolors.HEADER}health{art.bcolors.ENDC} is now {art.bcolors.BOLD}{art.bcolors.OKRED}{health}{art.bcolors.ENDC}HP!")
            sanity -= 1
            sanity_check()
            print(f"It's also driving you insane. Your {art.bcolors.BOLD}{art.bcolors.OKRED}sanity{art.bcolors.ENDC} is now {art.bcolors.BOLD}{art.bcolors.OKRED}{sanity}{art.bcolors.ENDC}!")
            puzzle_choices()
    elif puzzle_choice == "d" and "scalpel" not in inventory:
        func.spacer(3)
        print(f"It will take a little {art.bcolors.BOLD}{art.bcolors.OKRED}dexterity{art.bcolors.ENDC}.")
        func.spacer(1)
        print("Rolling your dexterity check...")
        med_skill(dexterity_mod)
        if skill_check == True:
            func.spacer(0.5)
            print("Come on...")
            func.spacer(1)
            print("Nearly got it...")
            func.spacer(2)
            print("YOU DID IT! Let's go!")
            rooftop()
        else:
            func.spacer(2)
            print("Nice try, but you've messed it up.")
            func.spacer(0.5)
            health -= 2
            health_check()
            print(f"You've even managed to knick your finger, your {art.bcolors.BOLD}{art.bcolors.HEADER}health{art.bcolors.ENDC} is now {art.bcolors.BOLD}{art.bcolors.OKRED}{health}{art.bcolors.ENDC}HP!")
            sanity -= 1
            sanity_check()
            print(f"It's also driving you insane. Your {art.bcolors.BOLD}{art.bcolors.OKRED}sanity{art.bcolors.ENDC} is now {art.bcolors.BOLD}{art.bcolors.OKRED}{sanity}{art.bcolors.ENDC}!")
            puzzle_choices()
    else:
        func.spacer(1)
        print("Now's not the time to waste time...")
        func.spacer(0.5)
        health -= 3
        health_check()
        sanity -=2
        sanity_check()
        print(f"Your {art.bcolors.BOLD}{art.bcolors.HEADER}health{art.bcolors.ENDC} is now {art.bcolors.BOLD}{art.bcolors.OKRED}{health}{art.bcolors.ENDC}HP with a {art.bcolors.BOLD}{art.bcolors.OKRED}sanity{art.bcolors.ENDC} of {art.bcolors.BOLD}{art.bcolors.OKRED}{sanity}{art.bcolors.ENDC}! Stop messing about!")
        func.spacer(0.5)
        puzzle_choices()

def rooftop():
    global health
    global sanity
    print("YOU WIN!")
    func.spacer(1)
    func.clear_screen()
    art.gamewin_art()
    func.spacer(2)
    print(f"You finished with {health}HP and {sanity} points")
    gamewin_screen()

def gamewin_screen():
    func.spacer(1)
    art.gamewin_art()
    play_again = input("""
    Would you like to play again?
    Yes  |  No \n
    """)
    play_again = play_again.lower()
    if play_again == "yes":
        func.spacer(2)
        stat_wipe()
        print("\033c")
        intro()
    if play_again == "no":
        func.spacer(2)
        print("Thanks for playing!")
        func.spacer(20)
        print("\033c")
    else:
        func.spacer(1)
        print("I'm just going to take that as a no.")
        func.spacer(20)
        print("\033c")
number_puzzle()