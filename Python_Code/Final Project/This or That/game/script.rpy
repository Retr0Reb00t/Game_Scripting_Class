# Defines all characters
define Ash = DynamicCharacter("[Ash_name]", color = "#808080")
define Barry = DynamicCharacter("[Barry_name]", color = "#e6e6e6")
define Mindy = DynamicCharacter("[Mindy_name]", color = "#000000")
define Jade = DynamicCharacter("[Jade_name]", color = "#17e617")
define Finn = DynamicCharacter("[Finn_name]", color = "#e617e6")
define Announcer = Character("Announcer", color = "#e61717")


# Stores images
image Barry_Whitter = "images/Barry Whitter.png"
image Mindy_Blackburn = "images/Mindy Blackburn.png"



# The game starts here.

label start:
    # Declares all neede variables
    $ Ash_name = "Me"
    $ Barry_name = "???"
    $ Mindy_name = "???"
    $ Jade_name = "Participant 2"
    $ Finn_name = "Participant 3"
    $ attempts = 3
    $ found_box = False
    $ read_publicFile = False
    $ read_privateFile = False
    $ code = ""
    

    # Intro dialogue
    Ash "{i}(I wake up on the cold, wet floor.)"
    Ash "{i}(As I get up, I feel my head ringing as you try to recall where I was.)"
    Ash "{i}(I search my surrondings, however they're completely foreign to me.)"
    Ash "{i}(However, I realized that I wasn't alone.)"

    show Barry_Whitter at left with fade
    show Mindy_Blackburn at right with fade

    Ash "{i}(Two people stood at the opposite corner of the room; a guy and a girl.)"
    Mindy "Finnally you woke up. Enjoyed your beauty rest?"
    Barry "Sorry for not waking you, {i}SOMEBODY{/i} though it would be better to not wake you."
    Mindy "Oh please. If something important were to happen, I would have woken him."
    Ash "{i}(The two started to bicker, I guess I should figure out this two's names.)"


    menu:
        "Who do you talk to first?"

        "Ask the guy's name":
            $ Barry_name = "Barry Whitter"

            Barry "I'm Barry Whitter. I'm a Sanitation Worker."
            Mindy "Who's surprised, the filth messes around with filth."
            Barry "Excuse me!? I provide a public service!"
            Mindy "Maybe for people who don't know how to take care after themselves, garbage boy."
            Barry "And what the hell do you do exactly?"
            Mindy "I'm though you'd never ask."

            $ Mindy_name = "Mindy Blackburn"

            Mindy "Mindy Blackburn, Money Lendor."
            Barry "Oh, so a loan shark is saying I'm worthless? That's rich."
            Mindy "So we've resorted to name calling now? How beneath you."
            Barry "YOU'RE THE ONE WHO CALLED ME- you know what, nevermind."
            Barry "So, what's your name?"

        "Ask the girl's name":
            $ Mindy_name = "Mindy Blackburn"

            Mindy "Mindy Blackburn, Money Lendor."
            Barry "Oh, so you're a loan shark; should've known from your shitty attitude."
            Mindy "Loan shark? I am no such thing. I provide a wonderful service."
            Barry "Sure, if that service was robbing people blind."
            Mindy "And who are you to think you can judge my business ventures?"

            $ Barry_name = "Barry Whitter"

            Barry "...I'm Barry Whitter. I'm a Sanitation Worker."
            Mindy "Who's surprised, the filth messes around with filth."
            Barry "Excuse m-"
            Mindy "Whatever. You, what's your name?"

    
    $ Ash_name = "Ash Grawert"

    Ash "My name's Ash Grawert. I am a Funeral Attendant."
    Mindy "Well Grawert, welcome to your new, disgusting home."
    Mindy "Oh Whitter, maybe you can put yourself to use and clean up."
    Barry "Ugh..."
    Ash "{i}(She's not wrong. The room is almost entirley destitute, everything is either cracked, or rusted.)"
    Ash "{i}(Everything, except a machine dead center in the room.)"

    scene background

    Ash "{i}(The machine has a single monitor, two files laying on top of it, an intercom system with mic and speaker, & two buttons.)"
    Ash "{i}(One is labled: Participant 2; the other: Participant 3.)"
    Ash "{i}(As I try to understand what I are looking at. A voice comes over the intercom's speaker.)"


    Announcer "{b}ROUND 2 SHALL NOW BEGIN. PARTICIPANTs 4, 5, & 6, IN FRONT OF YOU IS A MONITER THAT LINKS TO ANOTHER ROOM."
    Announcer "{b}IN SAID ROOM CONTAINS TWO OTHER PARTICIPANTS. ALL YOU HAVE TO DO IS MAKE SURE SOMETHING DIES IN THAT ROOM WITHIN 15 MINUTES."
    Announcer "{b}FALLIURE TO DO SO WILL CAUSE AN UNWANTED OUTCOME. YOU MAY USE THE PROVIDED PUBLIC & PRIVATE RECORDS ON THE PARTICIPANTS & SPEAK TO THE PARTICIAPNTS TO MAKE YOUR DECISION."
    Announcer "{b}ONCE YOU'VE MADE YOUR DECISION, PRESS THE CORRESPODING BUTTON IN FRONT OF YOU. YOUR FIFTEEN MINUTES BEGINS NOW."

    Ash "{i}(As the voice cuts off, the monitor turns on to reveal another room with two other individuals.)"

    Jade "Hey! Can you hear us?! GET US OUT OF HERE!!"
    Finn "Quiet down! If we couldn't find a way out, what makes you think that someone else in another room could."
    Jade "Because if we don't get out of here in 15 minutes, then we'll die!"

    show Mindy_Blackburn at right

    Mindy "Well technically, only one of you will die."
    Jade "THAT'S BARELY ANY BETTER!!!"

    show Barry_Whitter at left

    Barry "Jesus Christ Mindy! Don't worry, well try to get you out of there."
    Ash "{i}(We only have a few minutes, but I should get to know who these two are.)"


    menu:
        "Who should you talk to first?"

        "Talk to Participant 2":
            $ Jade_name = "Jade Grunberg"

            Jade "Um.. I am Jade Grunberg... I work a-"
            Finn "We don't have time for idle chatter."
            Jade "Ahh!"

            $ Finn_name = "Finn Morricone"

            Finn "The names's Finn Morricone."
            Jade "Please, help us get out of here!!"

        "Talk to Participant 3":
            $ Finn_name = "Finn Morricone"
            $ Jade_name = "Jade Grunberg"

            Finn "The name's Finn Morricone. That's Jade Grunberg."
            Jade "Hey! Atleast let me say my own name?"
            Finn "We don't have time."
            Finn "Hey, you three. If you have any ideas on how to let us out, say it now."
            Finn "Otherwise, pick one of us to die already."
        

    Mindy "I suggest we should act quickly and use are resources effectivley."
    Barry "Ditto! We have to act fast if we want to save them."
    Mindy "Sure... save them...."
    Barry "You aren't seriously suggesting that we should kill one of them?!"
    Mindy "I'm just saying if the worst comes we should be perpared to due the unthinkable."
    Ash "{i}(As the two start arguing... again, I start thinking about what we need to do next.)"


    while attempts > 0:

        menu:
            "What do yo do"

            "Make your decision":
                Ash "{i}(I look at the buttons in front of me. We had to make this decision eventually.)"
                Jade "Don... Don't kill me!"
                Finn "Hey! I ain't dying; pick them, not me!"
                Ash"{i}(You try to drown out their screaming and pick who dies.)"


                while attempts > 0:
                    menu:
                        "Who do you choose to kill?"

                        "Kill Jade Grunberg":
                            ""
                        "Kill Finn Morricone":
                            ""
                        "Think of Somethin else":
                            ""


                    # removes an attempt and warns the player
                    $ attempts = attempts - 1

                    if attempts == 2:
                        Announcer "{b}YOU HAVE 7 MINUTES LEFT."
                    if attempts == 1:
                        Announcer "{b}WARNING, YOU HAVE 1 MINUTE LEFT. I SUGGEST YOU DECIDE WHO DIES QUICKLY."
                        Mindy "Stop goofing around. We need to make a decision now!"
                        Ash "I guess there is nothing else we can do."


                Finn "Fuck this shit. I ain't dying here!"
                Ash "{i}(Finn rips a rusty pipe from the wall and starts swinging at Participant 2.)"
                Ash "{i}(In defense, Participant 2 grabs a broken tile and swings back.)"
                Ash "{i}(After stabbing and blundgeoning each other a few times, they both collapsed, lying in a pool of their own blood.)"
                Announcer "{b}ROUND 2 RESULTS: BOTH PARTICIPANT 2 & 3 ARE DEAD."
                Announcer "{b}PARTICIPANT 4, 5, &, WE ARE RATHER DISAPPOINTED IN YOUR INABILITY TO PICK SOMEONE TO DIE."
                Barry "Ho-holy Hell! What The Fuck!?!"
                Mindy "Ugh. What a waste of life..."
                Ash "{i}(I slump to the ground. I just killed to people. I just stood here and watched them kill each other.)"
                Ash"{i}(As I drown in your sorrow & cowardice, I here the intercom's speaker crackle again.)"
                Announcer "{b}ROUND 3 SHALL NOW BEGIN. PARTICIPANTS 7, 8, 9, & 10, IN FRONT OF YOU IS A MONITER THAT LINKS TO ANOTHER ROOM."
                Announcer "{b}IN SAID ROOM CONTAINS THREE OTHER PARTICIPANTS. ALL YOU HAVE TO DO IS MAKE SURE SOMETHING DIES IN THAT ROOM WITHIN 15 MINUTES."
                Announcer "{b}FALLIURE TO DO SO WILL CAUSE AN UNWANTED OUTCOME. YOU MAY USE THE PROVIDED PUBLIC & PRIVATE RECORDS ON THE PARTICIPANTS & SPEAK TO THEM TO MAKE YOUR DECISION."
                Announcer "{b}ONCE YOU'VE MADE YOUR DECISION, PRESS THE CORRESPODING BUTTON IN FRONT OF YOU. YOUR FIFTEEN MINUTES BEGINS NOW."

                scene black

                "{b}{i}Ending C: A Cowards Way Out."

            "Read the Public Records" if (not read_publicFile and attempts > 1):
                Ash "We should read the Public Records."
                Ash "{i}(I grabbed the Public Records and open it.)"
                Barry "It says that here that Jade is a Lapidarist."
                Mindy "And Morricone is a Malacologist."
                Ash "{i}(...I have no idea what those jobs are, let alone how to pronounce them.)"
                Ash "Uhm.. can you two give us some details on your jobs."
                Jade "Oh, sure!"
                Jade "I cut, shape, & polish gemstones. I work with celebirties and fashion designers to make gemed accessories and decorations."
                Jade "I also work as a Trail Guide on the side."
                Barry "What about you Finn."
                Finn "*Sigh* Fine."
                Finn "I study mollusks such as snails and cephalopods. My research helps create medicine, conservation efforts, and improve aquaculture practices."
                Finn "I also teach kids how to surf and swim nearby my house."
                Mindy "Hmmm, intresting."
                Mindy "Well, I think we can make are decision easily."
                Ash "Uh, what are you talking about?"
                Barry "Yeah, what are you talking about Mindy?"
                Mindy "Well..."
                Mindy "Shouldn't you save the person you activley helps people than the gemcutter."
                Jade "Wha-What the hell!"
                Mindy "I'm just saying. Someone has to die, so shouldn't it be the least useful one?"
                Barry "That's a horrible way to think!"
                Barry "We're talking about a person! How can you be so reckless with someone's life!!"
                Ash "{i}(As they began to argue, I continued to keep reading the records.)"
                Ash "{i}(Hmm, nothing else in this seems that notable.)"
                Ash "{i}(I put down the record and thought about what to do next.)"

                $ read_publicFile = True # Notes that the player read the public records

            "Read the Private Records" if (not read_privateFile and attempts > 1):
                Ash "We should read the Private Records."
                Ash "{i}(I grabbed the Private Records and open it.)"
                Ash "{i}(...Most of these doesn't seem that imporant.)"
                Ash "{i}(But, the last page: Crimes, catches my eye.)"
                Mindy "Participant 2: Verbally berated and left a client during a trail."
                Barry "Participant 3: ...Assualted a co-worker over reaserch?!"
                Ash "Okay, I'm sure there is a logical reason for this."
                Ash "Jade, Finn, can you explain this?"
                Jade "This is just a big misunderstanding."
                Jade "We just started a trail. It was an old creep who was making perverted comments to some of the other trail goers."
                Jade "I yelled at them and said if they can't behave then the rest of the group will go on without them. They didn't stop, so we left."
                Finn "Participant 3: A co-worker tried to steal my research and sell it to a company that would only use for there self-intrest and not for the betterment of the world."
                Finn "What I did was the correct thing to do."
                Jade "Well... I'm not shocked that the only thing you know is violence."
                Finn "Participant 3: What did you just say?!"
                Ash "{i}(That was an odd thing for them to say. I kept reading the record to see if I can under stand.)"
                Ash "{i}(And then... I reached it.)"
                Ash "{i}(Participant 2 and 3 had killed Participant 1 in Round 1.)"
                Ash "Jade, Finn! what happened in the first round?!"
                Finn "We were told the same thing as you, someone in the room our machine was linked to must die in 15 minutes."
                Jade "Yeah, and you were really eager to kill them. You could have at least waited and think of something"
                Finn "think of what? they were the only one in the room, they stated that the door was locked."
                Finn "We don't know what will happen to us if the time ran out. I saved us."
                Barry "Well, if we  have to kill one person... I know who I'm choosing."
                Mindy "Oh? and who do you choose."
                Barry "I picking Finn Morricone."
                Finn "...."
                Barry "They clearly have no respect for human life. It would be the moral choice to choose them to die."
                Mindy "Oh, shut it. If I wanted to be preached to I'd go to my local church."
                Ash "{i}(As they began to argue, I put down the record and thought about what to do next.)"

                $ read_privateFile = True # Notes that the player read the private records

            "Ask them to look around their surrondings" if (attempts > 1):
                Ash "Can you tell us what your room is liked."
                if not found_box:
                    Barry "How would that help them?"
                    Ash "We should try to get as much information as we can. You want to save them, right?"
                    Barry "Yes..."
                    Mindy "Whatever, it's not my funeral."
                    Finn "Our room is probably the same as yours." 
                    Finn "It's decrepit and wet. We have a door, but our side doesn't have a handle, and it doesn't budge."
                    Jade "Participant 2: There really isn't anythin else in the room, it's pretty barre-"
                    Jade "*Thump* - Ow! what they?"
                    Ash "{i}(I check the monitor and see that Jade tripped on the tiled floor.)"
                    Jade "Huh? Hey, the floor here is loose!"


                    menu:
                        "What should you do?"

                        "Remove the tiles":
                            Ash "You should remove the tiles."
                            Ash "{i}(They started digging through the tiles.)"
                            Jade "Hey, there's something down here.... is that a mannequin."
                            Finn " Yeah, but it's locked in a box. there is nothing more that we can do."
                            $ found_box = True # notes that the player found the box

                            menu:
                                "What should you do?"

                                "Try to open the box":
                                    Ash "Let's try to open the box."
                                    Finn "There is a six digit lock on it. It seems to use only letters."
                                    Jade "Participant 2: There is also text above the lock. Let me read it out:"

                                    # loops till player runs out of attempts
                                    while (attempts > 0):
                                        "WE ARE SIX OF A KIND AND FILL THE WORLD WITH VIVID LIFE."
                                        "YOU NEED ONLY ARE INITIALS AND NOTHING MORE."
                                        "ORDER THE PRIMARIYS OF THE LIGHT BEFORE THE PRIMARYS OF THE INK."
                                        "FINALLY LINE EACH GROUP FROM LIGHTEST TO DARKEST."
            
                                        # stores and transforms user's input
                                        $ code = renpy.input("What is the passcode?", length = 6)
                                        $ code = code.upper()
            
                                        # if player is correct
                                        if code == "GRBYCM":
                                            Jade "It worked! Now what?"
                                            Mindy "Yeah... What are we supposed to do with a mannequin?"
                                            Ash "..."
                                            Ash "You need to stab the Mannequin."
                                            Barry "...What?"
                                            Ash "All we were asked to do is make sure something in that room dies."
                                            Ash "We were never told that the thing that needs to dies has to be human."
                                            Finn "It's better than nothing."
                                            Ash "{i}(Finn grabs a shard of floor tile and stabs the mannequin.)"
                                            Announcer "ROUND 2 RESULTS: THE MANNEQUIN IS DEAD."
                                            Announcer "PARTICIPANT 2: JADE GRUNBERG & PARTICIPANT 3: FINN MORRICONE HAVE SURVIVED. PLEASE EXIT YOUR TRIAL ROOM."
                                            Announcer "WELL DONE PARTICIPANTS."
                                            Jade "Thank you so much for saving us!"
                                            Finn "Ditto. We would be dead without you. We will do are best to try to get you out of here."
                                            Mindy "I'm... actually suprised that it was that easy."
                                            Barry "Yeah, but I'm glad that we could save them!"
                                            Ash "{i}(I took a sigh of relief. We saved them both; nobody had to die.)"
                                            Ash "{i}(But then you here the intercom's speaker crackle again.)"
                                            Announcer "{b}ROUND 3 SHALL NOW BEGIN. PARTICIPANTS 7, 8, 9, & 10, IN FRONT OF YOU IS A MONITER THAT LINKS TO ANOTHER ROOM."
                                            Announcer "{b}IN SAID ROOM CONTAINS THREE OTHER PARTICIPANTS. ALL YOU HAVE TO DO IS MAKE SURE SOMETHING DIES IN THAT ROOM WITHIN 15 MINUTES."
                                            Announcer "{b}FALLIURE TO DO SO WILL CAUSE AN UNWANTED OUTCOME. YOU MAY USE THE PROVIDED PUBLIC & PRIVATE RECORDS ON THE PARTICIPANTS & SPEAK TO THEM TO MAKE YOUR DECISION."
                                            Announcer "{b}ONCE YOU'VE MADE YOUR DECISION, PRESS THE CORRESPODING BUTTON IN FRONT OF YOU. YOUR FIFTEEN MINUTES BEGINS NOW."

                                            scene black

                                            Ash "{i}(It took us a while to realize what was said, but we said calm. All we have to do is find and kill the mannequin.)"
                                            Ash"{i}(And so, we started searching for the mannequin in our room.)"
                                            "{b}{i}Ending E: Another Way Out."
                                            return
                                        else: # if player is wrong
                                            Finn "Shit! It didn't work"
                    
                                        # removes an attempt and warns the player
                                        $ attempts = attempts - 1

                                        if attempts == 2:
                                            Announcer "{b}YOU HAVE 7 MINUTES LEFT."
                                        if attempts == 1:
                                            Announcer "{b}WARNING, YOU HAVE 1 MINUTE LEFT. I SUGGEST YOU DECIDE WHO DIES QUICKLY."
                                            Mindy "Stop goofing around!"

                                "Think of something else":
                                    Ash "I try to think of something else to do."

                        "Search the room more":
                            Ash "{i}(They searched the room again, but they came up empty-handed.)"
                else:
                    Ash "{i}(They searched the room again, but they came up empty-handed.)"

            "Try to open the box" if (found_box and attempts > 1):
                Ash "Let's try to open the box."
                Finn "There is a six digit lock on it. It seems to use only letters."
                Jade "Participant 2: There is also text above the lock. Let me read it out:"

                # loops till player runs out of attempts
                while (attempts > 0):
                    "WE ARE SIX OF A KIND AND FILL THE WORLD WITH VIVID LIFE."
                    "YOU NEED ONLY ARE INITIALS AND NOTHING MORE."
                    "ORDER THE PRIMARIYS OF THE LIGHT BEFORE THE PRIMARYS OF THE INK."
                    "FINALLY LINE EACH GROUP FROM LIGHTEST TO DARKEST."
            
                    # stores and transforms user's input
                    $ code = renpy.input("What is the passcode?", length = 6)
                    $ code = code.upper()
            
                    # if player is correct
                    if code == "GRBYCM":
                        Jade "It worked! Now what?"
                        Mindy "Yeah... What are we supposed to do with a mannequin?"
                        Ash "..."
                        Ash "You need to stab the Mannequin."
                        Barry "...What?"
                        Ash "All we were asked to do is make sure something in that room dies."
                        Ash "We were never told that the thing that needs to dies has to be human."
                        Finn "It's better than nothing."
                        Ash "{i}(Finn grabs a shard of floor tile and stabs the mannequin.)"
                        Announcer "ROUND 2 RESULTS: THE MANNEQUIN IS DEAD."
                        Announcer "PARTICIPANT 2: JADE GRUNBERG & PARTICIPANT 3: FINN MORRICONE HAVE SURVIVED. PLEASE EXIT YOUR TRIAL ROOM."
                        Announcer "WELL DONE PARTICIPANTS."
                        Jade "Thank you so much for saving us!"
                        Finn "Ditto. We would be dead without you. We will do are best to try to get you out of here."
                        Mindy "I'm... actually suprised that it was that easy."
                        Barry "Yeah, but I'm glad that we could save them!"
                        Ash "{i}(I took a sigh of relief. We saved them both; nobody had to die.)"
                        Ash "{i}(But then you here the intercom's speaker crackle again.)"
                        Announcer "{b}ROUND 3 SHALL NOW BEGIN. PARTICIPANTS 7, 8, 9, & 10, IN FRONT OF YOU IS A MONITER THAT LINKS TO ANOTHER ROOM."
                        Announcer "{b}IN SAID ROOM CONTAINS THREE OTHER PARTICIPANTS. ALL YOU HAVE TO DO IS MAKE SURE SOMETHING DIES IN THAT ROOM WITHIN 15 MINUTES."
                        Announcer "{b}FALLIURE TO DO SO WILL CAUSE AN UNWANTED OUTCOME. YOU MAY USE THE PROVIDED PUBLIC & PRIVATE RECORDS ON THE PARTICIPANTS & SPEAK TO THEM TO MAKE YOUR DECISION."
                        Announcer "{b}ONCE YOU'VE MADE YOUR DECISION, PRESS THE CORRESPODING BUTTON IN FRONT OF YOU. YOUR FIFTEEN MINUTES BEGINS NOW."

                        scene black

                        Ash "{i}(It took us a while to realize what was said, but we said calm. All we have to do is find and kill the mannequin.)"
                        Ash"{i}(And so, we started searching for the mannequin in our room.)"
                        "{b}{i}Ending E: Another Way Out."
                        return
                    else: # if player is wrong
                        Finn "Shit! It didn't work"
                    
                    # removes an attempt and warns the player
                    $ attempts = attempts - 1

                    if attempts == 2:
                        Announcer "{b}YOU HAVE 7 MINUTES LEFT."
                    if attempts == 1:
                        Announcer "{b}WARNING, YOU HAVE 1 MINUTE LEFT. I SUGGEST YOU DECIDE WHO DIES QUICKLY."
                        Mindy "Stop goofing around!"
                

        # removes an attempt and warns the player
        $ attempts = attempts - 1

        if attempts == 2:
            Announcer "{b}YOU HAVE 7 MINUTES LEFT."
        if attempts == 1:
            Announcer "{b}WARNING, YOU HAVE 1 MINUTE LEFT. I SUGGEST YOU DECIDE WHO DIES QUICKLY."
            Mindy "Stop goofing around. We need to make a decision now!"
            Ash "I guess there is nothing else we can do."


# If the player fails to solve the box
    Announcer "{b}ANNOUNCER: TIME IS UP. INITIATING PUNISHIMENT."
    "{b}*KA-BOOM*" with vpunch
    Barry "W...what was that sound!?"
    Ash "{i}(We check the monitor to see what made that sound, and find it.)"
    Ash "{i}(Both Particiapnts' heads exploded.)"
    Announcer "{b}ROUND 2 RESULTS: BOTH PARTICIPANT 2 & 3 ARE DEAD."
    Announcer "{b}PARTICIPANT 4, 5 & 6, WE ARE RATHER DISAPPOINTED IN YOUR INABILITIY TO SOLVE THE PUZZLE."
    Barry "Ho-holy Hell! What The Fuck!?!"
    Mindy "Ugh. What a waste of life..."
    Ash "(I slumped to the ground. We were so close to saving them, and yet, it was all for nought.)"
    Ash "(As I drown in your sorrow, I here the intercom's speaker crackle again.)"
    Announcer "{b}ROUND 3 SHALL NOW BEGIN. PARTICIPANTS 7, 8, 9, & 10, IN FRONT OF YOU IS A MONITER THAT LINKS TO ANOTHER ROOM."
    Announcer "{b}IN SAID ROOM CONTAINS THREE OTHER PARTICIPANTS. ALL YOU HAVE TO DO IS MAKE SURE SOMETHING DIES IN THAT ROOM WITHIN 15 MINUTES."
    Announcer "{b}FALLIURE TO DO SO WILL CAUSE AN UNWANTED OUTCOME. YOU MAY USE THE PROVIDED PUBLIC & PRIVATE RECORDS ON THE PARTICIPANTS & SPEAK TO THEM TO MAKE YOUR DECISION."
    Announcer "{b}ONCE YOU'VE MADE YOUR DECISION, PRESS THE CORRESPODING BUTTON IN FRONT OF YOU. YOUR FIFTEEN MINUTES BEGINS NOW."

    scene black

    Ash "{i}(It took us a while to realize what was said...the mannequin...that is the way out of here.)"
    Ash "{i}(And so, we started to search for the mannequin in our room.)"
    Ash "{i}(...Please tell me we have a mannequin.)"
    "{b}{i}Ending D: Savior Complex."
    return