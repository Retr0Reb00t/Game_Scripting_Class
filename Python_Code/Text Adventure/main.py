# Name: Calrence Isaiah Franklin
# Date: Jul-22-2025
# Description: A text adventrue where the player must choice between to people to kill

# import necessary files
import sys
from colorama import Fore, Back, Style

# declare neede variables
choice = ""
attempts = 3
foundBox = False
readPublic = False
readPrivate = False

# Title of the game
print("\n------------------------------ THIS OR THAT ------------------------------\n\n")

# Intro Dialouge
print("You wake up on the cold, wet floor. As you get up, you feel your head ringing as you try to recall where you were.")
print("You search your surrondings, however they're completely foreign to you.")
print("The room is almost entirley destitute, everything is either cracked, or rusted; everything, except a machine dead center in the room.")
print("The machine has a single monitor, two files laying on top of it, an intercom system with mic and speaker, & two buttons.")
print("One is labled: " + Fore.GREEN + "Participant 2" + Style.RESET_ALL + "; the other: " + Fore.MAGENTA + "Participant 3." + Style.RESET_ALL)
print("As you try to understand what you are looking at. A voice comes from the intercom's speaker.")
print(Style.BRIGHT + Back.RED + "ANNOUNCER: ROUND 2 SHALL NOW BEGIN. PARTICIPANT 4, IN FRONT OF YOU IS A MONITER THAT LINKS TO ANOTHER ROOM.")
print("IN SAID ROOM CONTAINS TWO OTHER PARTICIPANTS. ALL YOU HAVE TO DO IS MAKE SURE SOMETHING DIES IN THAT ROOM WITHIN 15 MINUTES.")
print("FALLIURE TO DO SO WILL CAUSE AN UNWANTED OUTCOME. YOU MAY USE THE PROVIDED PUBLIC & PRIVATE RECORDS ON THE PARTICIPANTS & SPEAK TO THE PARTICIAPNTS TO MAKE YOUR DECISION.")
print("ONCE YOU'VE MADE YOUR DECISION, PRESS THE CORRESPODING BUTTON IN FRONT OF YOU. YOUR FIFTEEN MINUTES BEGINS NOW." + Style.RESET_ALL)
print("As the voice cuts off, the monitor turns on to reveal another room with two other individuals.")
print(Fore.GREEN + "Participant 2: Hey! Can you hear us?! GET US OUT OF HERE!!")
print(Fore.MAGENTA + "Participant 3: Quiet down! If we couldn't find a way out, what makes you think that someone else in another room could.")
print(Fore.GREEN + "Participant 2: Because if we don't get out of here in 15 minutes, then we'll die!")
print(Fore.MAGENTA + "Participant 3: No, only one of us will die.")
print( Fore.GREEN + "Participant 2: THAT'S BARELY ANY BETTER!!!")
print(Style.RESET_ALL + "The two continued to agrue amounst themselves. You might as well try and do what the announcer said and use what you can to come to a result.\n")

# main loop, loops till player runs out of attempts
while (attempts > 0):
    # loops while the player hasn't inputted a vaild anwser
    while (choice != "READ AND ASK ABOUT THE PUBLIC RECORDS" and choice != "READ AND ASK ABOUT THE PRIVATE RECORDS" and choice != "ASK THEM TO DESCRIBE THEIR SURRONDINGS" and choice != "MAKE YOUR DECISION" and choice != "TRY TO OPEN BOX"):
        print("What do you do: ")
        if readPublic == False:
            print("> [READ AND ASK ABOUT THE PUBLIC RECORDS]")
        if readPrivate == False:
            print("> [READ AND ASK ABOUT THE PRIVATE RECORDS]")
        if foundBox :
            print("> [TRY TO OPEN BOX]")
        else:
            print("> [ASK THEM TO DESCRIBE THEIR SURRONDINGS]")
        print("> [MAKE YOUR DECISION]")
        
        # stores and transforms user's input
        choice = input("> ")
        choice = choice.upper()
        
        # gives error message if the user inputs an invalid input
        if (choice != "READ AND ASK ABOUT THE PUBLIC RECORDS" or readPublic) and (choice != "READ AND ASK ABOUT THE PRIVATE RECORDS" or readPrivate) and (choice != "ASK THEM TO DESCRIBE THEIR SURRONDINGS" or foundBox == True) and choice != "MAKE YOUR DECISION" and (choice != "TRY TO OPEN BOX" or foundBox == False):
            print("Invalid answer, please try again.\n")
            choice = ""
            
    if choice == "READ AND ASK ABOUT THE PUBLIC RECORDS": # the player looks at the public records
        print("\nYou grab the public records and open it.")
        print("Participant 2: Lapidarist. Also works as a Trail Guide on the side.")
        print("Participant 3: Malacologist. Also teaches kids to surf & swim.")
        print("You ask the to eleaborate on their jobs")
        print(Fore.GREEN + "Participant 2: I cut, shape, & polish gemstones. I work with celebirties and fashion designers to make gemed accessories and decorations.")
        print(Fore.MAGENTA + "Participant 3: I study mollusks such as snails and cephalopods. My research helps create medicine, conservation efforts, and improve aquaculture practices.")
        print("...Shouldn't you save the person you activley helps people than the gemcutter.")
        print(Fore.GREEN + "Participant 2: Wha-What the hell!")
        print(Fore.MAGENTA + "Particiapnt 3: I'm just saying. Someone has to die, so shouldn't it be the least useful." + Style.RESET_ALL)
        print("As they began to argue, you put down the record and thought about what to do next.")
        readPublic = True # player reads records
    elif choice == "READ AND ASK ABOUT THE PRIVATE RECORDS": # the player looks at the private records
        print("\nYou grab the private records and open it.")
        print("Participant 2: Verbally berated and left a client during a trail.")
        print("Participant 3: Assualted a co-worker over reaserch.")
        print("You ask the to eleaborate on what they have done.")
        print(Fore.GREEN + "Participant 2: We just started a trail. It was an old creep who was making perverted comments to some of the other trail goers.")
        print("I yelled at them and said if they can't behave then the rest of the group will go on without them. They didn't stop, so we left.")
        print(Fore.MAGENTA + "Participant 3: A co-worker tried to steal my research and sell it to a company that would only use for there self-intrest and not for the betterment of the world.")
        print("What I did as the correct thing to do.")
        print(Fore.GREEN + "Participant 2: Well... I'm not shocked that the only thing you know is violence.")
        print(Fore.MAGENTA + "Participant 3: What did you just say?!" + Style.RESET_ALL)
        print("You are confused as to why Participant 2 would say that, and then you read the rest of the record.")
        print("Participant 2 and 3 had killed Participant 1 in Round 1.")
        print("You ask them what happened in Round 1.")
        print(Fore.MAGENTA + "Participant 3: We were told the same thing as you, someone in the room our machine is linked must die in 15 minutes.")
        print(Fore.GREEN + "Yeah, and you were really eager to kill them. You could have at least waited and think of something")
        print(Fore.MAGENTA + "think of what? they were the only one in the room, they stated that the door was locked.")
        print("We don't know what will happen to us if the time ran out. I saved us." + Style.RESET_ALL)
        print("As they began to argue, you put down the record and thought about what to do next.")
        readPrivate = True # player reads records
    elif choice == "ASK THEM TO DESCRIBE THEIR SURRONDINGS": # the player wants to search their surrondings
        print("\nYou ask them to search the area and describe it to you.")
        print(Fore.MAGENTA + "Participant 3: Our room is probably the same as yours. It's decrepit and wet. We have a door, but our side doesn't have a handle, and it doesn't budge.")
        print(Fore.GREEN + "Participant 2: There really isn't anythin else in the room, it's pretty barre- *Thump* - Ow! what they?" + Style.RESET_ALL)
        print("You check the monitor and see that Participant tripped on the tiled floore.")
        print(Fore.GREEN + "Participant 2: Huh? Hey, the floor here is loose!" + Style.RESET_ALL + "\n")
        # loops while the player hasn't inputted a vaild anwser
        while(choice != "REMOVE THE TILES" and choice != "SEARCH THE ROOM MORE"):
            print("What do you do:")
            print("> [REMOVE THE TILES]")
            print("> [SEARCH THE ROOM MORE]")
            
            # stores and transforms user's input
            choice = input("> ")
            choice = choice.upper()
            
            # gives error message if the user inputs an invalid input
            if choice != "REMOVE THE TILES" and choice != "SEARCH THE ROOM MORE":
                print("Invalid answer, please try again.\n")
                
        if choice == "REMOVE THE TILES": # the player wants to remove the tiles
            print("\nYou tell them to remove the tiles.")
            print(Fore.GREEN + "Participant 2: Hey, there's something down here.... is that a mannequin.")
            print(Fore.MAGENTA + "Participant 3: Yeah, but it's locked in a box. there is nothing more that we can do." + Style.RESET_ALL + "\n")
            foundBox = True # the player found the box
            # loops while the player hasn't inputted a vaild anwser
            while(choice != "TRY TO OPEN BOX" and choice != "THINK OF SOMETHING ELSE"):
                print("What do you do:")
                print("> [TRY TO OPEN BOX]")
                print("> [THINK OF SOMETHING ELSE]")
                
                # stores and transforms user's input
                choice = input("> ")
                choice = choice.upper()
                
                # gives error message if the user inputs an invalid input
                if choice != "TRY TO OPEN BOX" and choice != "THINK OF SOMETHING ELSE":
                    print("Invalid answer, please try again.\n")
            
            if choice == "THINK OF SOMETHING ELSE": # if the player wants to think of somethin else 
                print("\nYou try and think of something else to do.")
            
        else: # the player wants to search the room more
            print("\nYou tell them to search the room more, but there search comes back fruitless.")
        
    elif choice == "MAKE YOUR DECISION": # the player chose to make a choice
        print("\nYou look at the buttons in front of you. you had to make this decision eventually.")
        print(Fore.GREEN + "Participant 2: Don... Don't kill me!")
        print(Fore.MAGENTA + "Participant 3: Hey! I ain't dying; pick them, not me!" + Style.RESET_ALL)
        print("You try to drown out their screaming and pick who dies.\n")
        
        # loops till player runs out of attempts
        while(attempts > 0):
            # loops while the player hasn't inputted a vaild anwser
            while(choice != "PARTICIPANT 2" and choice != "PARTICIPANT 3" and choice != "THINK OF SOMETHING ELSE"):
                print("Who do you choose to die:")
                print("> [PARTICIPANT 2]")
                print("> [PARTICIPANT 3]")
                print("> [THINK OF SOMETHING ELSE]")
                
                # stores and transforms user's input
                choice = input("> ")
                choice = choice.upper()
                
                # gives error message if the user inputs an invalid input
                if choice != "PARTICIPANT 2" and choice != "PARTICIPANT 3" and choice != "THINK OF SOMETHING ELSE":
                    print("Invalid answer, please try again.\n")
            
            if choice ==  "PARTICIPANT 2": # the player chooses to kill participant 2
                print("\nYou press Participant 2's button.")
                print(Style.BRIGHT + Back.RED + "ANNOUNUCER: PARTICIPANT 2 HAS BEEN CHOSEN FOR DEATH. PREPARE FOR EXECUTION." + Style.RESET_ALL)
                print(Fore.GREEN + "Participant 2: WHAT! No! No no no no no no! Please don- " + Style.BRIGHT + "*KA-BOOM*" + Style.RESET_ALL)
                print("You look at the monitor to the the origins of the loud boom, and you find it. Participant 2's head had exploded.")
                print(Style.BRIGHT + Back.RED + "ANNOUNCER: ROUND 2 RESULTS: PARTICIPANT 2 HAS DIED.")
                print("PARTICIPANT 3: FINN MORRICONE HAS SURVIVED. PLEASE EXIT YOUR TRIAL ROOM." + Style.RESET_ALL)
                print(Fore.MAGENTA + "Thanks for not killing me. Maybe we can meet up when you get out of here." + Style.RESET_ALL)
                print("You sit on the floor and thought about what just happened. You just killed someone, but at least you saved someone and yourself.")
                print("But then, you here the intercom's speaker crackle again.")
                print(Style.BRIGHT + Back.RED + "ANNOUNCER: ROUND 3 SHALL NOW BEGIN. PARTICIPANT 5 & PARTICIPANT 6, IN FRONT OF YOU IS A MONITER THAT LINKS TO ANOTHER ROOM.")
                print("IN SAID ROOM CONTAINS ONE OTHER PARTICIPANT. ALL YOU HAVE TO DO IS MAKE SURE SOMETHING DIES IN THAT ROOM WITHIN 15 MINUTES.")
                print("FALLIURE TO DO SO WILL CAUSE AN UNWANTED OUTCOME. YOU MAY USE THE PROVIDED PUBLIC & PRIVATE RECORDS ON THE PARTICIPANT & SPEAK TO THEM TO MAKE YOUR DECISION.")
                print("ONCE YOU'VE MADE YOUR DECISION, PRESS THE CORRESPODING BUTTON IN FRONT OF YOU. YOUR FIFTEEN MINUTES BEGINS NOW." + Style.RESET_ALL + "\n")
                print(Style.BRIGHT + Fore.MAGENTA + "Ending A: Survival of the Fittest." + Style.RESET_ALL)
                sys.exit()
            elif choice == "PARTICIPANT 3": # the player choses to kill participant 3
                print("\nYou press Participant 3's button.")
                print(Style.BRIGHT + Back.RED + "ANNOUNUCER: PARTICIPANT 3 HAS BEEN CHOSEN FOR DEATH. PREPARE FOR EXECUTION." + Style.RESET_ALL)
                print(Fore.MAGENTA + "Participant 3: You Fuck! You think I'm going to let you kill me think ag-" + Style.BRIGHT + "*KA-BOOM*" + Style.RESET_ALL)
                print("You look at the monitor to the the origins of the loud boom, and you find it. Participant 3's head had exploded.")
                print(Style.BRIGHT + Back.RED + "ANNOUNCER: ROUND 2 RESULTS: PARTICIPANT 3 HAS DIED.")
                print("PARTICIPANT 2: JADE GRUNBERG HAS SURVIVED. PLEASE EXIT YOUR TRIAL ROOM." + Style.RESET_ALL)
                print(Fore.GREEN + "Th... Thank you for saving me. I hope you get out of here" + Style.RESET_ALL)
                print("You sit on the floor and thought about what just happened. You just killed someone, but at least you saved someone and yourself.")
                print("But then, you here the intercom's speaker crackle again.")
                print(Style.BRIGHT + Back.RED + "ANNOUNCER: ROUND 3 SHALL NOW BEGIN. PARTICIPANT 5 & PARTICIPANT 6, IN FRONT OF YOU IS A MONITER THAT LINKS TO ANOTHER ROOM.")
                print("IN SAID ROOM CONTAINS ONE OTHER PARTICIPANT. ALL YOU HAVE TO DO IS MAKE SURE SOMETHING DIES IN THAT ROOM WITHIN 15 MINUTES.")
                print("FALLIURE TO DO SO WILL CAUSE AN UNWANTED OUTCOME. YOU MAY USE THE PROVIDED PUBLIC & PRIVATE RECORDS ON THE PARTICIPANT & SPEAK TO THEM TO MAKE YOUR DECISION.")
                print("ONCE YOU'VE MADE YOUR DECISION, PRESS THE CORRESPODING BUTTON IN FRONT OF YOU. YOUR FIFTEEN MINUTES BEGINS NOW." + Style.RESET_ALL + "\n")
                print(Style.BRIGHT + Fore.GREEN + "Ending B: Judgement Day." + Style.RESET_ALL)
                sys.exit()
            else: # if the player wants to think of somethin else
                print("\nYou suggest that they should try something else instead of pushing the button.")
                print(Fore.GREEN + "Participant 2: Easy for you to say! Your life isn't on the line!")
                print(Fore.MAGENTA + "Participant 3: What else is their for us to do? Just push a button already!" + Style.RESET_ALL)
                if foundBox: # if the player finds the box
                    print("\nYou told the to try and open the box.")
                    print(Fore.MAGENTA + "Participant 3: There is a six digit lock on it. It seems to use only letters.")
                    print(Fore.GREEN + "Participant 2: There is also text above the lock. Let me read it out:" + Style.RESET_ALL)
                    # loops till player runs out of attempts
                    while (attempts > 0):
                        print(Back.WHITE + Fore.BLACK + "WE ARE SIX OF A KIND AND FILL THE WORLD WITH VIVID LIFE.")
                        print("YOU NEED ONLY ARE INITIALS AND NOTHING MORE.")
                        print("ORDER THE PRIMARIYS OF THE LIGHT BEFORE THE PRIMARYS OF THE INK.")
                        print("FINALLY LINE EACH GROUP FROM LIGHTEST TO DARKEST." + Style.RESET_ALL + "\n")
                        print("what is the passcode?")
                        
                        # stores and transforms user's input
                        choice = input("> ")
                        choice = choice.upper()
                        
                        # if player is correct
                        if choice == "GRBYCM":
                            print(Fore.GREEN + "\nParticipant 2: It worked! Now what?" + Style.RESET_ALL)
                            print("You tell them to 'kill' the mannequin.")
                            print(Fore.MAGENTA + "Participant 3: It's better than nothing." + Style.RESET_ALL)
                            print("Participant 3 grabs a shard of floor tile and stabs the mannequin.")
                            print(Style.BRIGHT + Back.RED + "ANNOUNCER: ROUND 2 RESULTS: THE MANNEQUIN IS DEAD.")
                            print("PARTICIPANT 2: JADE GRUNBERG & PARTICIPANT 3: FINN MORRICONE HAVE SURVIVED. PLEASE EXIT YOUR TRIAL ROOM.")
                            print("WELL DONE PARTICIPANT 4: ASH GRAWERT." + Style.RESET_ALL)
                            print(Fore.GREEN + "Thank you so much for saving us!")
                            print(Fore.MAGENTA + "Ditto. We would be dead without you. We will do are best to try to get you out of here." + Style.RESET_ALL)
                            print("You took a sigh of relief. You saved them both; nobody had to die.")
                            print("But then you here the intercom's speaker crackle again.")
                            print(Style.BRIGHT + Back.RED + "ANNOUNCER: ROUND 3 SHALL NOW BEGIN. PARTICIPANT 5 & PARTICIPANT 6, IN FRONT OF YOU IS A MONITER THAT LINKS TO ANOTHER ROOM.")
                            print("IN SAID ROOM CONTAINS ONE OTHER PARTICIPANT. ALL YOU HAVE TO DO IS MAKE SURE SOMETHING DIES IN THAT ROOM WITHIN 15 MINUTES.")
                            print("FALLIURE TO DO SO WILL CAUSE AN UNWANTED OUTCOME. YOU MAY USE THE PROVIDED PUBLIC & PRIVATE RECORDS ON THE PARTICIPANT & SPEAK TO THEM TO MAKE YOUR DECISION.")
                            print("ONCE YOU'VE MADE YOUR DECISION, PRESS THE CORRESPODING BUTTON IN FRONT OF YOU. YOUR FIFTEEN MINUTES BEGINS NOW." + Style.RESET_ALL)
                            print("It took you a while to realize what was said, but you said calm. All you have to do is find and kill the mannequin.")
                            print("And so, you start searching for the mannequin in your room.\n")
                            print(Style.BRIGHT + Fore.CYAN + "Ending E: Another Way Out." + Style.RESET_ALL)
                            sys.exit()
                        else: # if player is wrong
                            print(Fore.MAGENTA + "\nParticipant 3: Shit! It didn't work" + Style.RESET_ALL)
                        
                        # subtracts an attempt    
                        attempts = attempts -1
                        
                        # tells the player their losing of an attempt
                        if attempts == 1:
                            print(Style.BRIGHT + Back.RED + "ANNOUNCER: WARNING, YOU HAVE 1 MINUTE LEFT. I SUGGEST YOU DECIDE WHO DIES QUICKLY." + Style.RESET_ALL + "\n")
                
                # if the player is about to lose all attempts        
                elif attempts - 1 > 0:
                    print("They're right, we don't have anything else to work with. Maybe I should just think about this more.")
                    if readPublic: # if the player read the public record
                        print("Based on the public records, it would be the best if I save Participant 3 & kill Participant 2.")
                        print("Participant 3's research in Malacology can help people, in medicne, culinary, and other areas.")
                        print("On the other hand, all Participant 2 does is cut and polish gems.")
                    if readPrivate: # if the player read the private record
                        print("The private records does not put Participant 3 in a good light; assualting a co-worker just cause they thought that they work.")
                        print("Not only that, but they were way to insistant on killing Participant 1 & didn't even try to find a way for them to escape.")
            
            # resets choice and subtracts an attempt
            attempts = attempts -1
            choice = ""
            
            # tells the player their losing of an attempt
            if attempts == 2:
                  print(Style.BRIGHT + Back.RED + "ANNOUNCER: YOU HAVE 7 MINUTES LEFT." + Style.RESET_ALL + "\n")
            if attempts == 1:
                print(Style.BRIGHT + Back.RED + "ANNOUNCER: WARNING, YOU HAVE 1 MINUTE LEFT. I SUGGEST YOU DECIDE WHO DIES QUICKLY." + Style.RESET_ALL + "\n")
            
            # if the user can't pick between Jade & Finn to die in time
            if foundBox == False:
                print(Fore.MAGENTA + "Fuck this shit. I ain't dying here!" + Style.RESET_ALL)
                print("Participant 3 rips a rusty pipe from the wall and starts swinging at Participant 2. In defense, Participant 2 grabs a broken tile and swings back.")
                print("After stabbing and blundgeoning each other a few times, they both collapsed, lying in a pool of their own blood.")
                print(Style.BRIGHT + Back.RED + "ANNOUNCER: ROUND 2 RESULTS: BOTH PARTICIPANT 2 & 3 ARE DEAD.")
                print("PARTICIPANT 4: ASH GRAWERT, WE ARE RATHER DISAPPOINTED IN YOUR INABILITY TO PICK SOMEONE." + Style.RESET_ALL)
                print("You slump to the ground. You just killed to people. You just stood here and watched them kill each other.")
                print("As you drown in your sorrow & cowardice, you here the intercom's speaker crackle again.")
                print(Style.BRIGHT + Back.RED + "ANNOUNCER: ROUND 3 SHALL NOW BEGIN. PARTICIPANT 5 & PARTICIPANT 6, IN FRONT OF YOU IS A MONITER THAT LINKS TO ANOTHER ROOM.")
                print("IN SAID ROOM CONTAINS ONE OTHER PARTICIPANT. ALL YOU HAVE TO DO IS MAKE SURE SOMETHING DIES IN THAT ROOM WITHIN 15 MINUTES.")
                print("FALLIURE TO DO SO WILL CAUSE AN UNWANTED OUTCOME. YOU MAY USE THE PROVIDED PUBLIC & PRIVATE RECORDS ON THE PARTICIPANT & SPEAK TO THEM TO MAKE YOUR DECISION.")
                print("ONCE YOU'VE MADE YOUR DECISION, PRESS THE CORRESPODING BUTTON IN FRONT OF YOU. YOUR FIFTEEN MINUTES BEGINS NOW." + Style.RESET_ALL + "\n")
                print(Style.BRIGHT + Fore.YELLOW + "Ending C: A Cowards Way Out." + Style.RESET_ALL)
                sys.exit()
    
    
    # if the player chooses to try to open the box
    if choice == "TRY TO OPEN BOX":
        print("\nYou told the to try and open the box.")
        print(Fore.MAGENTA + "Participant 3: There is a six digit lock on it. It seems to use only letters.")
        print(Fore.GREEN + "Participant 2: There is also text above the lock. Let me read it out:" + Style.RESET_ALL)
        # loops till player runs out of attempts
        while (attempts > 0):
            print(Back.WHITE + Fore.BLACK + "WE ARE SIX OF A KIND AND FILL THE WORLD WITH VIVID LIFE.")
            print("YOU NEED ONLY ARE INITIALS AND NOTHING MORE.")
            print("ORDER THE PRIMARIYS OF THE LIGHT BEFORE THE PRIMARYS OF THE INK.")
            print("FINALLY LINE EACH GROUP FROM LIGHTEST TO DARKEST." + Style.RESET_ALL + "\n")
            print("what is the passcode?")
            
            # stores and transforms user's input
            choice = input("> ")
            choice = choice.upper()
            
            # if player is correct
            if choice == "GRBYCM":
                print(Fore.GREEN + "\nParticipant 2: It worked! Now what?" + Style.RESET_ALL)
                print("You tell them to 'kill' the mannequin.")
                print(Fore.MAGENTA + "Participant 3: It's better than nothing." + Style.RESET_ALL)
                print("Participant 3 grabs a shard of floor tile and stabs the mannequin.")
                print(Style.BRIGHT + Back.RED + "ANNOUNCER: ROUND 2 RESULTS: THE MANNEQUIN IS DEAD.")
                print("PARTICIPANT 2: JADE GRUNBERG & PARTICIPANT 3: FINN MORRICONE HAVE SURVIVED. PLEASE EXIT YOUR TRIAL ROOM.")
                print("WELL DONE PARTICIPANT 4: ASH GRAWERT." + Style.RESET_ALL)
                print(Fore.GREEN + "Thank you so much for saving us!")
                print(Fore.MAGENTA + "Ditto. We would be dead without you. We will do are best to try to get you out of here." + Style.RESET_ALL)
                print("You took a sigh of relief. You saved them both; nobody had to die.")
                print("But then you here the intercom's speaker crackle again.")
                print(Style.BRIGHT + Back.RED + "ANNOUNCER: ROUND 3 SHALL NOW BEGIN. PARTICIPANT 5 & PARTICIPANT 6, IN FRONT OF YOU IS A MONITER THAT LINKS TO ANOTHER ROOM.")
                print("IN SAID ROOM CONTAINS ONE OTHER PARTICIPANT. ALL YOU HAVE TO DO IS MAKE SURE SOMETHING DIES IN THAT ROOM WITHIN 15 MINUTES.")
                print("FALLIURE TO DO SO WILL CAUSE AN UNWANTED OUTCOME. YOU MAY USE THE PROVIDED PUBLIC & PRIVATE RECORDS ON THE PARTICIPANT & SPEAK TO THEM TO MAKE YOUR DECISION.")
                print("ONCE YOU'VE MADE YOUR DECISION, PRESS THE CORRESPODING BUTTON IN FRONT OF YOU. YOUR FIFTEEN MINUTES BEGINS NOW." + Style.RESET_ALL)
                print("It took you a while to realize what was said, but you said calm. All you have to do is find and kill the mannequin.")
                print("And so, you start searching for the mannequin in your room.\n")
                print(Style.BRIGHT + Fore.CYAN + "Ending E: Another Way Out." + Style.RESET_ALL)
                sys.exit()
            else: # if player is wrong
                print(Fore.MAGENTA + "\nParticipant 3: Shit! It didn't work" + Style.RESET_ALL)
            
            # subtracts an attempt
            attempts = attempts -1
            
            # tells the player their losing of an attempt
            if attempts == 2:
                print(Style.BRIGHT + Back.RED + "ANNOUNCER: YOU HAVE 7 MINUTES LEFT." + Style.RESET_ALL + "\n")
            if attempts == 1:
                print(Style.BRIGHT + Back.RED + "ANNOUNCER: WARNING, YOU HAVE 1 MINUTE LEFT. I SUGGEST YOU DECIDE WHO DIES QUICKLY." + Style.RESET_ALL + "\n")
        
        
    # resets choice and subtracts an attempt        
    attempts = attempts -1
    choice = ""
    
    # tells the player their losing of an attempt
    if attempts == 2:
        print(Style.BRIGHT + Back.RED + "ANNOUNCER: YOU HAVE 7 MINUTES LEFT." + Style.RESET_ALL + "\n")
    if attempts == 1:
        choice = "MAKE YOUR DECISION"
        print(Style.BRIGHT + Back.RED + "ANNOUNCER: WARNING, YOU HAVE 1 MINUTE LEFT. I SUGGEST YOU DECIDE WHO DIES QUICKLY." + Style.RESET_ALL)

# If they player fails to anwser the box
print(Style.BRIGHT + Back.RED + "ANNOUNCER: TIME IS UP. INITIATING PUNISHIMENT." + Style.RESET_ALL)
print(Style.BRIGHT + "*KA-BOOM*" + Style.RESET_ALL)
print("You check the monitor to see what made that sound, and find it. Both Particiapnts head exploded")
print(Style.BRIGHT + Back.RED + "ANNOUNCER: ROUND 2 RESULTS: BOTH PARTICIPANT 2 & 3 ARE DEAD.")
print("PARTICIPANT 4: ASH GRAWERT, WE ARE RATHER DISAPPOINTED IN YOUR INABILITY TO SOLVE THE PUZZLE." + Style.RESET_ALL)
print("You slump to the ground. You were so close to saving them, and yet, it was all for nought.")
print("As you drown in your sorrow, you here the intercom's speaker crackle again.")
print(Style.BRIGHT + Back.RED + "ANNOUNCER: ROUND 3 SHALL NOW BEGIN. PARTICIPANT 5 & PARTICIPANT 6, IN FRONT OF YOU IS A MONITER THAT LINKS TO ANOTHER ROOM.")
print("IN SAID ROOM CONTAINS ONE OTHER PARTICIPANT. ALL YOU HAVE TO DO IS MAKE SURE SOMETHING DIES IN THAT ROOM WITHIN 15 MINUTES.")
print("FALLIURE TO DO SO WILL CAUSE AN UNWANTED OUTCOME. YOU MAY USE THE PROVIDED PUBLIC & PRIVATE RECORDS ON THE PARTICIPANT & SPEAK TO THEM TO MAKE YOUR DECISION.")
print("ONCE YOU'VE MADE YOUR DECISION, PRESS THE CORRESPODING BUTTON IN FRONT OF YOU. YOUR FIFTEEN MINUTES BEGINS NOW." + Style.RESET_ALL)
print("It took you a while to realize what was said...the mannequin...that is the way out of here.")
print("And so, you start searching for the mannequin in your room.\n")
print(Style.BRIGHT + Fore.BLUE + "Ending D: Savior Complex." + Style.RESET_ALL)
sys.exit()