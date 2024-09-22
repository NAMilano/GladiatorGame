import time
import random
from threading import Timer #used to timeout the user input for defenseMenu()

class gladiator:
    # gladiator class 
    def __init__(player, name):
        player.name = name
        player.health = 100
        player.money = 0
        player.attackBuff = 1.0
        player.defenseBuff = 1.0
        player.fightNum = 1
        player.revived = False

# intro message for the game 
def intro(player):
    print("\nPress enter to continue through the dialogue breaks.\n")
    print("\nGreetings " + player.name + ", you have been selected through the royal lottery to participate in the upcoming gladiator tournament."
          "\nAs you know when you are chosen you MUST participate or be subject to death by the emperor...")
    input()
    print("\nYou will have to win 5 battles to be allowed to retire."
          "\nIf you are successful the emperor will pay for you to live a life of luxury."
          "\nThese are battles to the death, but you will be able to purchase one revive throughout the tournament."
          "\nYou will be able to purchase a small defense or attack buff before each match."
          "\nYou will start with 100hp and at the end of each battle you will be able to purchase 25hp or a full heal."
          "\nThe opponents will gradually get harder so spend your money wisely.")
    input()
    print("\nYou have two weeks to get your affairs in order and to train for battle. Good Luck!")
    input()
    playerStatus(player)
    input()
    

# story message for fight one
def storyOne(player):
    player.fightNum = 1
    print("\nYou wake from sleep in the early morning to pounding on your door."
          "\nWhen you open the door and see the guards you realize the day has come for your first fight."
          "\nThey wait for you to get ready and escort you to the colosseum.")
    input()
    print("\nThe fight organizer Lucius enters the your room."
          "\nLucius: Greeting " + player.name + " I hope you are ready for your first battle!"
          "\nYou will be fighting a farmer who was also chosen by the royal lottery."
          "\nThis will be the first battle for both of you."
          "\nYou both have a medium build with a decent amount of muscle, so it is anyone's match."
          "\nBoth of you will be provided with a sword and shield with some metal armor for protection."
          "\nYou have a few minutes before your match so prepare yourself." 
          "\nThe guards will come and escort you to the entrance of the arena when it is your turn"
          "\nAnd between us my money is on you! So don't stress to much.")
    input()
    print("\nAround ten minutes passes and the guards come and get you."
          "\nYou are equipped with your armor, sword and shield"
          "\nThey take you to the final doors to the arena waiting for you to be announced.")
    input()
    print("\nYou hear muffled through the doors the arena announcers voice:"
          "\nFor our next fight we have some fresh meat!"
           "\nWe have two royal lottery winners who have never fought before."
          "\nI introduce to you our first contest " + player.name + ".")
    input()
    print("\nThe doors open and you walk out to the middle of the arena."
          "\nThe announcer continues:"
          "\nHe has a medium build with a decent amount of muscle."
          "\nHe is definitely capable of being an underdog for the season."
          "\nThe crowd cheers loudly.")
    input()
    print("\nYou stand there as your opponent is introduced."
          "\nYou are so nervous that you don't even realize what the announcer or crowd is saying."
          "\nAll you know is that a man is walking towards you from the opposing doors."
          "\nWhen he reaches you it snaps you back into reality and you hear the announcer:"
          "\nAlright ladies and gentlemen this fight is ready to begin!"
          "\nThe fighters will now bump shields and take 15 steps backwards."
          "\nOnce they are apart the emperor with begin the fight with the gong.")
    input()
    print("\nYou bump shields with your opponent and begin walking backwards."
          "\nAnnouncer: Let the fight begin!\n")
    input()
    fight(player)

# story message for fight two
def storyTwo(player):
    player.fightNum = 2
    print("\nYou know this fight will be even harder than the last."
          "\nAfter a few days of recovery you get to training."
          "\nSparring and wrestling with other combatants to learn."
          "\nYou are starting to gain some confidence in your physical capabilities."
          "\nHappy with your preparations and not wanting to over strain your body you take the final day before your fight off.")
    input()
    print("\nYou woke up early on fight day."
          "\nEat a good meal and prepare for the fight."
          "\nAfter waiting what seems like forever the guards knock on the door."
          "\nYou greet them and start walking to the colosseum."
          "\nWhile you are walking you here the other citizens remarking about you and that they are rooting for you."
          "\nYou have quickly become the underdog favored by the people."
          "\nEveryone wants you to be the first royal lottery winner to win all five fights."
          "\nOnce you arrive at the colosseum you are taken to a private room again."
          "\nThis time your room has a table of food, wine, and other beverages."
          "\nNow you must wait for Lucius.")
    input()
    print("\nLucius enters your room."
          "\n" + player.name + ", It is great to see you!"
          "\nI watched your last fight you were magnificent."
          "\nIf I didn't know better I would have thought you were an experienced fighter."
          "\nNow I am sure that you know, but each fight will be against a harder and harder opponent."
          "\nSo don't get to confident because you can quickly be knocked down."
          "\nThey need me out there, so good luck in your fight the guards will come get you when it is your turn.")
    input()
    print("\nIt feels like ten seconds passes by before the guards are knocking on your door."
          "\nYou take one final breath and follow them down the hall to the big arena doors."
          "\nThey hand you your sword, shield, and armor."
          "\nA few seconds after finishing putting on your armor you hear the announcer."
          "\nAnnouncer: Ladies and gentlemen for the second battle of the day we have a returning underdog."
          "\nThe peoples champion " + player.name + " is back and they is back for blood."
          "\n" + player.name + " is in even better shape than last time."
          "\nThey have been training hard and is definitely prepared to put on a show for us today.")
    input()
    print("\nThe gates across from you open and your opponent begins walking towards you."
          "\nThe announcer continues: " + player.name + "'s opponent is no joke."
          "\nHe is a person not afraid of a fight."
          "\nHe has a lengthy record with the law from pub fights to random physical brawls."
          "\nThe gracious emperor is giving him a chance to get out of jail by competing in two gladiator fights."
          "\nAlready having won his first match he must win one more fight to earn his freedom.")
    input()
    print("\nYou bump shields with your opponent and begin the walk backwards."
          "\nA few moments after finishing the 15 step walk the emperor bangs the gong."
          "\nAnnouncer: Let the fight begin!\n")
    input()
    fight(player)

# story message for fight three
def storyThree(player):
    player.fightNum = 3
    print("\nHappy with your preparations for your last fight you decide to follow the same protocol."
          "\nAfter three days of recovery you start training hard."
          "\nYou challenge the biggest and best sparring partners."
          "\nNo matter how badly you lose to them you know that the loss in training is worth the knowledge gained through the fight."
          "\nWhen you go into the fights with this mindset you win no matter the result.")
    input()
    print("\nOn your second day of training you challenge a man twice your size in muscle and height."
          "\nYou don't know who he is, but when other people in the training arena overhear your challenge everyone gets quiet"
          "\nThis mysterious man stares at you and accepts to fight."
          '\nOf in the distance you hear someone say "I cannot believe it he just challenged Crixus"'
          "\nAfter hearing this you are overcome with regret as you know exactly who he is."
          "\nCrixus is the emperors prized fighter."
          "\nHe is currently undefeated with a record of 18 wins 0 losses."
          "\nCrixus is the fifth and final opponent for the royal lottery tournaments."
          "\nHe ensures that the emperor will not have to financially support anyone because he is unbeatable."
          "\nIn return for this the emperor pays him greatly to train and fight.")
    input()
    print("\nWith all this in mind you don't back out and start the fight."
          "\nWhen the fight starts Crixus doesn't attack or block your punches."
          "\nYou can tell that his is playing with you."
          "\nThis one sided fight goes on for about a minute with your blows doing nothing to him."
          "\nThen Crixus smirks at you realizing you aren't going to be an issue in the gladiator tournament."
          "\nIf you even make it to him..."
          "\nHe then quickly strikes you in the face knocking you to the ground out cold."
          "\nYou wake up after a minute to a crowd of other trainees hovering around you."
          "\nDeciding not to push your luck especially with your fight being so close you head home."
          "\nWhen you wake up the next morning you are still hurting from your fight with Crixus."
          "\nSo, you decide to spend the last two days before your fight resting.")
    input()
    print("\nThe day of the fight has come and the guards escort you to a private room at the colosseum."
          "\nAfter waiting a few minutes Lucius enters your room."
          "\nGreetings " + player.name + "!"
          "\nI have heard whispers of your run in with Crixus."
          "\nDon't let that rattle you just focus on your current opponent."
          "\nAnyways I only had a free minute, but good luck out there.")
    input()
    print("\nThe guards come and escort you the doors of inner arena."
          "\nEquip you with the standard sword, shield, and armor."
          "\nYou are still doubting yourself after such a bad loss to Crixus earlier this week."
          "\nWithout a moment to calm your doubt you hear the announcer start to introduce you."
          "\nThe doors open and you walk to the center of the arena."
          "\nYou are still the people underdog and they go wild when the announcer introduces you.")
    input()
    print("\nThe doors in front of you open and your opponent begins walking towards you while the announcer introduces him."
          "\nHe was a munifex in the Roman army."
          "\nFor five years he has been training and preparing for battle, but was never apart of any wars."
          "\nAfter serving his time in the army his need for physical conflict has drove him to fight as a gladiator for money."
          "\nHe is a very dangerous opponent with his combat knowledge from the Roman army.")
    input()
    print("\nAnnouncer: Ladies and gentlemen this fight is about to begin."
          "\nSit back in your seats and prepare a spectacle!")
    input()
    print("\nThe emperor bangs the gong beginning the fight.\n")
    input()
    fight(player)

# story message for fight four
def storyFour(player):
    player.fightNum = 4
    print("\nAfter your last victory you have gained back your lost confidence."
          "\nYou spend the next three days resting and recovering from the fight."
          "\nAfter recovering you return back to the training arena for the first time since your fight with Crixus."
          "\nLuckily Crixus is not there and you can train in peace for the first day."
          "\nHalf way through training on your second day Crixus walks in and starts training."
          "\nNo matter how badly you want to challenge Crixus again to regain your pride and confidence you don't."
          "\nYou don't want to be potentially injured for your fourth fight."
          "\nYou finish your second and third training day with no issues.")
    input()
    print("\nAfter a refreshing day of rest it is fight day."
          "\nThe guards arrive and begin escorting you to the arena."
          "\nAs you are walking many fans are waiting along the way and cheer you on."
          "\nYou have become a household name as the peoples underdog."
          "\nEveryone is rooting for you to be the first royal lottery winner to win all five fights."
          "\nYou arrive at the private room in the colosseum."
          "\nThis room is much fancier than the last have been and has expensive food and drinks on a buffet table.")
    input()
    print("\nA little while later Lucius enters your room."
          "\nIt is great to see you " + player.name + "!"
          "\nThe colosseum is packed today with your fans."
          "\nEveryone really believes that you will be the first royal lottery winner, so tickets to see you in action are in high demand."
          "\nYou still have a little bit of time before your match begins, so relax and take advantage of the free food and drinks."
          "\nGood luck out there!")
    input()
    print("\nAbout ten minutes passes before the guards come and take you to the arena doors."
          "\nYou are fitted with the usual sword, shield, and armor."
          "\nYou are announced and walk out to the middle of the arena as the crowd goes wild."
          "\nPeople are screaming and chanting your name.")
    input()
    print("\nThe announcer introduces your opponent and he meets you in the middle of the arena."
          "\nYour opponent is a trained assassin."
          "\nHe was a very successful centurion in the roman armor."
          "\nFrom time to time he fights in the colosseum for money and fun."
          "\nHis status in the Roman army and his record in the colosseum has made him feared by many.")
    input()
    print("\nAnnouncer: This is going to be a great fight today."
          "\nWe have two very successful and skilled fighters ready to battle to the death."
          "\nGet ready to be entertained!")
    input()
    print("\nThe emperor strikes the gong commencing the fight.\n")
    input()
    fight(player)

# story message for fight five
def storyFive(player):
    player.fightNum = 5
    print("\nYou are one fight away from being free of your royal lottery obligations."
          "\nIf you are successful your life will be changed forever."
          "\nUnlimited funds to live however you want for the rest of your life.")
    input()
    print("\nYou continue your usual routine of spending the three days after a fight resting and recovering."
          "\nOn the third day you are surprisingly approached by guards who tell you that you have been requested by the emperor."
          "\nThey escort you to the palace."
          "\nWhile walking through the halls of the palace you see expensive paintings, sculptures, and other rare items."
          "\nThe entire palace is full of magnificent items that you never have dreamed of seeing in person.")
    input()
    print("\nFinally you reach the emperors quarters."
          "\nEmperor: It is good to finally meet you face to face " + player.name + "."
          "\nI have been impressed with your skills in the arena."
          "\nYou certainly have quite the underdog story."
          "\nBeing a royal lottery winner making it to their fifth fight still standing is very impressive."
          "\nI am actually starting to want you to win even if that costs me a bit of gold."
          "\nUnfortunately for you your next fight is against Crixus my strongest fighter."
          "\nIt would look quite bad on my army if my best fighter is beaten by a royal lottery winner."
          "\nSo even you must succumb to your fate of losing.")
    input()
    print("\nI just wanted to meet you before your defeat and let you know that you were one of the best royal lottery winners I have every seen."
          "\nYou are free to leave now."
          "\nGood bye.")
    input()
    print("\nYou are escorted back to your home by the guards.")
    input()
    print("\nThe next three days you spend training the hardest you ever have."
          "\nYou are determined to win not only for the prize and to live, but to prove the emperor wrong.")
    input()
    print("\nFight day comes and you are escorted to the colosseum by the guards."
          "\nOn the walk there the streets were lined with residents cheering for the cities underdog."
          "\nYou are taken to a fancy private room with a buffet of food and drinks.")
    input()
    print("\nTen minutes pass and Lucius enters your room."
          "\nLucius: " + player.name + "!"
          "\nI still cannot believe you have made it this far!"
          "\nIt is very impressive you have really turned into a great fighter."
          "\nI have to get going, but just know that I along with the rest of the city is rooting for you.")
    input()
    print("\nIt seems like hours pass before the guards come and get you for your fight."
          "\nThey escort you to the arena doors and hand you the sword, shield, and armor."
          "\nThe doors open and you walk to the middle of the arena."
          "\nThe crowd goes crazy as you are walking screaming and chanting your name."
          "\nWhen you get to the center of arena it really hits you that this is your last fight for better or worse."
          "\nYou are determined to win.")
    input()
    print("\nThe announcer: For " + player.name + "'s final opponent we have the emperors prized fighter Crixus!"
          "\nThe crowd goes silent when the announcer is introducing Crixus."
          "\nThe announcer continues: A man needing no introduction the current final boss of the royal lottery."
          "\nHis current record is 18 wins and 0 loses and he is here to make it 19 wins.")
    input()
    print("\nCrixus stares at you the whole time."
          "\nYou go to bump shields, but Crixus turns his back and starts walking the 15 steps."
          "\nAfter a moment you take your 15 steps back and prepare for the fight.")
    input()
    print("\nAnnouncer: Get ready for one of the best fights of our lifetime.")
    input()
    print("\nThe emperor bangs the gong starting your final fight.\n")
    input()
    fight(player)

# story end after player wins all five fights
def storyEnd(player):
    print("\nAs soon as you land the final blow to Crixus winning the entire tournament the crowd goes wild."
          '\nAfter a few moments of celebration the emperor screams out "SILENCE"'
          "\nEveryone goes silent."
          "\nThe emperor begins: Ladies and gentlemen we have our first royal lottery winner."
          "\nWe have witnessed five of the most intense, close, and entertaining matches."
          "\nWhile the emperor is speaking the guards escort you to his viewing platform."
          "\nWhen you arrive the emperor continues."
          "\nIt is my honor to bestow " + player.name + " with this golden crown as a symbol for his tremendous victory."
          "\nNot only will " + player.name + " receive this crown they also will be financially covered by me personally."
          "\nThey have become one of the most wealthy individuals in the city."
          "\nLet this be a reminder that the royal lottery can turn anyone's dreams into a reality.")
    input()
    print("\nThe next royal lottery drawings will be held in 30 days."
          "\nGood luck and may the odds be in your favor\n")

# used to get the name for the main character 
def getName():
    # prompt user for name input
    print("Hello player! What do you wish the main characters name to be? The default name is 'Spartacus'.\n"
          "Enter your name of choice or leave the prompt blank to use the default.")
    charName = input()
    # if user inputs nothing defaults the name to "Spartacus"
    if(charName == ""):
        charName = "Spartacus"
    return charName

# prints the current statistics of the users character - Player name, health, money, attack buff, and defense buff
def playerStatus(player):
    print("\n" + player.name + "'s Current Stats\nHealth: " + str(player.health) + "\nMoney: " + str(player.money) +
        "\nAttack Stat: " + str(player.attackBuff) + "\nDefense Stat: " + str(player.defenseBuff))
    
# displays the attack prompt and gets the users desired target
def attackMenu():
    target = ''
    while (target != '1' and target != '2' and target != '3' and target != '4'): # loops till valid value is entered
        print("Attack Menu: (1)Head, (2)Torso, (3)Arms, or (4)Legs")
        target = input()
    return target

# displays defense menu prompt and has a time limited user input prompt for their defense 
def defenseMenu():
    print("Defense Menu: (1)Head, (2)Torso, (3)Arms, or (4)Legs")
    inputTimer = Timer(2, print, ["\nYou ran out of time. Please press enter to continue."]) #creating Timer variable inputTimer - A timer for 2 seconds that outputs the message if not canceled before the 2 seconds.
    inputTimer.start() # starts the timer inputTimer
    start = time.time() # gets current time
    protect = input()
    inTime = inputTimer.is_alive() # if program reaches this while the timer is still alive it means the user entered their answer within the two seconds - Returns true if timer still active False if timer is off
    if(inTime == False or protect == ''): # if the user inputs after the timer expires set protect to 0 - if user enters nothing set protect to 0
        protect = 0
    inputTimer.cancel() # stops the timer inputTimer if reached within the two seconds
    finish = time.time() # gets current time
    timeElapsed = finish - start # gets the total time that was elapsed between the two times
    return protect, timeElapsed

# gets the current weak point of the enemy and outputs one of three messages per body part to help the player choose the correct target
def enemyWeakness():
    weakness = random.randint(1,4) # gets which limb will be the weak point - 1 head, 2 torso, 3 arms, 4 legs
    option = random.randint(1,3) # gets which of the three output messages will be displayed 
    if(weakness == 1):
        if(option == 1):
            print("\nAttack Hint: Your opponents helmet doesn't fit correctly.")
        if(option == 2):
            print("\nAttack Hint: Your opponents helmet is badly damaged.")
        if(option == 3):
            print("\nAttack Hint: Your opponent is keeping his hands too low and he wont be able to defend his head.")
    if(weakness == 2):
        if(option == 1):
            print("\nAttack Hint: Your opponents chest plate doesn't fit correctly.")
        if(option == 2):
            print("\nAttack Hint: Your opponents chest plate is badly damaged.")
        if(option == 3):
            print("\nAttack Hint: Your opponent is keeping his hands too high and he wont be able to defend his lower torso.")
    if(weakness == 3):
        if(option == 1):
            print("\nAttack Hint: Your opponents arm armor doesn't fit correctly.")
        if(option == 2):
            print("\nAttack Hint: Your opponents arm armor is badly damaged.")
        if(option == 3):
            print("\nAttack Hint: Your opponent is holding their arms incorrectly allowing you to hit through gap in between their arm armor.")
    if(weakness == 4):
        if(option == 1):
            print("\nAttack Hint: Your opponents leg armor doesn't fit correctly.")
        if(option == 2):
            print("\nAttack Hint: Your opponents leg armor is badly damaged.")
        if(option == 3):
            print("\nAttack Hint: Your opponent is standing incorrectly allowing you to hit through gap in between their leg armor.")
    return weakness

# Full combat sequence 
# All player damage values are calculated randomly between two values. 
# The min and max damage values are chosen using random.choices weighted randomization. 
def fight(player):
    oppHealth = 100 # sets the opponents health to 100 before every fight
    while(oppHealth > 0 and player.health > 0): # loops while both characters have more than 0 health
        damageOne = 0
        damageTwo = 0
        weakness = enemyWeakness()
        target = attackMenu()
        minMax = [15, 20, 25, 30, 35, 40] # all possible min and max damage values
        while(damageOne == damageTwo): # loops till the min and max values are not the same 
            damageOne, damageTwo = random.choices(minMax, weights=(15, 40, 35, 5, 3, 2), k=2) # Gets the Min and Max values for the range of player damage - Weighted damage values are 15=15% 20=40% 25=35% 30=5% 35=3% 40=2%
        damage = random.randint(min(damageOne, damageTwo), max(damageOne, damageTwo)) # gets a random value between the two values for the players damage
        if(weakness == int(target)): # checks if the player target matches the opponents weakness
            damage += 5 # if player chose correctly add 5 bonus damage
        damage *= player.attackBuff # adjusts the damage based on players current attack buff
        damage = int(round(damage, 0)) # rounds damage to keep it a whole number and convert it back to int
        oppHealth -= damage 
        damageOutput(player, damage, oppHealth)
        if(oppHealth > 0): # if the opponent is still alive after the players last attack start the defense cycle
            print("\nRemember the faster you defend the more damage you block.")
            print("You have 2 seconds to defend yourself.\n")
            time.sleep(2)
            defenseSeq(player, oppHealth)
    player.attackBuff = 1.0 # resets attack buff after the fight is over
    player.defenseBuff = 1.0 # resets defense buff after the fight is over

    checkHealth(player)

# Full defense cycle 
def defenseSeq(player, oppHealth):
    timeElapsed = 0.0
    damageOne = 0
    damageTwo = 0
    target = oppAttack()
    protect, timeElapsed = defenseMenu()
    protect = int(protect)
    # changes the min and max values based on each fight - the higher the fight number the harder the opponent will hit
    if(player.fightNum == 1):
        damageList = [5, 10, 15, 20]
    if(player.fightNum == 2):
        damageList = [15, 20, 25, 30]
    if(player.fightNum == 3):
        damageList = [25, 30, 35, 40]
    if(player.fightNum == 4 or player.fightNum == 5):
        damageList = [35, 40, 45, 50]
    while(damageOne == damageTwo): # loops until damageOne and damageTwo are not the same
        damageOne, damageTwo = random.choices(damageList, weights=(40,35,20,5), k=2) # gets the Min and Max values using weighted randomization
    damage = random.randint(min(damageOne, damageTwo), max(damageOne, damageTwo)) # gets a random value between the values as the opponents damage
    damage = blockDamage(protect, target, damage, timeElapsed)
    defenseBuff = (damage * (player.defenseBuff - 1)) # get the amount of damage that the player is negating with their current defense buff
    if(damage >= round(defenseBuff)): # if statement to make sure that the damage value wont go into the negative
        damage -= round(defenseBuff)
    else:
        damage = 0
    player.health -= round(damage)
    damageTaken(player, damage, oppHealth) 

# gets a random target 1-4 for the opponent then displays the body part selected
def oppAttack():
    target = random.randint(1,4)
    if(target == 1):
        print("Your opponent attacks your head.")
    if(target == 2):
        print("Your opponent attacks your torso.")
    if(target == 3):
        print("Your opponent attacks your arms.")
    if(target == 4):
        print("Your opponent attacks your legs.")
    return target

# reduces the damage of the attack based on the speed of the players inputs
def blockDamage(protect, target, damage, timeElapsed):
    if(target == protect):
        if(timeElapsed <= 0.5): # if the player correctly inputs defense within 0.5 seconds reduce the damage by 80 percent
            print("Perfect block! 80 percent of the damage was blocked.")
            damage *= 0.2
        if(timeElapsed <= 0.75 and timeElapsed > 0.5): # if the player correctly inputs defense between 0.75 seconds and 0.5 seconds reduce the damage by 60 percent
            print("Great block! 60 percent of the damage was blocked.")
            damage *= 0.4
        if(timeElapsed <= 1 and timeElapsed > 0.75): # if the player correctly inputs defense between 1 seconds and 0.75 seconds reduce the damage by 40 percent
            print("Good block! 40 percent of the damage was blocked.")
            damage *= 0.6
        if(timeElapsed <= 1.5 and timeElapsed > 1): # if the player correctly inputs defense between 1.5 seconds and 1 seconds reduce the damage by 20 percent
            print("Decent block! 20 percent of the damage was blocked.")
            damage *= 0.8
    else: # if player doesn't meet any of the above time requirements player takes full damage
        print("You did not block your opponents attack.")
    return damage

# Standard output message for dealing damage. Displays amount of damage dealt, your health, and opponents health
def damageOutput(player, damage, oppHealth):
    if(damage >= 25):
        print("Critical Hit!\nDamage Dealt: " + str(int(damage)) + "\nYour Health: " + str(int(player.health)) + "\nOpponents Health: " + str(int(oppHealth)) + "\n")
    if(damage >= 15 and damage < 25):
        print("Good Hit.\nDamage Dealt: " + str(int(damage)) + "\nYour Health: " + str(int(player.health)) + "\nOpponents Health: " + str(int(oppHealth)) + "\n")
    if(damage >= 0 and damage < 15):
        print("Weak strike.\nDamage Dealt: " + str(int(damage)) + "\nYour Health: " + str(int(player.health)) + "\nOpponents Health: " + str(int(oppHealth)) + "\n")

# Standard output messages for taking damage. Displays amount of damage taken, your health, and opponent health
def damageTaken(player, damage, oppHealth):
    if(damage >= 25):
        print("You will definitely feel that...\nDamage Taken: " + str(int(damage)) + "\nYour Health: " + str(int(player.health)) + "\nOpponents Health: " + str(int(oppHealth)) + "\n")
    if(damage >= 15 and damage < 25):
        print("You could take a couple of these blows.\nDamage Taken: " + str(int(damage)) + "\nYour Health: " + str(int(player.health)) + "\nOpponents Health: " + str(int(oppHealth)) + "\n")
    if(damage >= 0 and damage < 15):
        print("Barely made a mark.\nDamage Taken: " + str(int(damage)) + "\nYour Health: " + str(int(player.health)) + "\nOpponents Health: " + str(int(oppHealth)) + "\n")

# compares health at the end of fights for various outcomes
def checkHealth(player):
    if(player.health > 0 and player.fightNum != 5): # displays win message for the first four fights and gives the player their gold for winning
        print("Congratulations " + player.name + " you won your battle! You have been awarded 6 gold. Rest up your next fight is in a week...\n")
        player.money += 6
    if(player.health > 0 and player.fightNum == 5): # if player wins the fifth fight calls the storyEnd() function and returns out of function
        storyEnd(player)
        return
    if(player.health > 0): # opens player shop
       shop(player) 
    if(player.health <= 0 and player.revived == True): # message for when a player dies and already purchased the revive then quits the program ending the game completely 
        print("You have died! Unfortunately you can only purchase one revive better luck next time.")
        quit()
    if(player.health <= 0 and player.money < 5 and player.revived == False): # message for when a player dies and doesn't have enough money for the revive then quits the program ending the game completely 
        print("You have died! Unfortunately you don't have enough money for a revive better luck next time.")
        quit()
    if(player.health <= 0 and player.money >= 5 and player.revived == False): # calls revive function when the player dies and has enough money and hasn't already purchased the revive
        revive(player)
        if(player.health > 0): # after being revived make player redo the last fight
            print("\nRedoing last fight")
            fight(player)
        else: 
            print("\nThanks for playing.") # message when the player chooses to decline the revive when offered
            quit() # quits the program ending the game completely 

# Shop of all items that are available after each battle
def shop(player):
    choice = "0"
    print("Greetings " + player.name + " welcome to the shop!")
    while(choice != "5" and player.money >= 0): # loops till player chooses option 5 to exit or has less than or equal to zero gold
        print("Enter the corresponding number for the item you wish to purchase or 5 to exit shop."
          "\n(1) A health kit for 25 life - Cost 3 gold"
          "\n(2) A full heal to 100 life - Cost 9 gold"
          "\n(3) A small attack buff for the next fight - Cost 2 gold"
          "\n(4) A small defense buff for the next fight - Cost 2 gold"
          "\n(5) Exit the shop")
        playerStatus(player) # displays current play statistics to help the player choose what to buy
        choice = input()
        if(choice == "1"): # if statements for each purchasable item
            if(player.money >= 3): # checks if the player has enough money to be able to purchase the item
                if(player.health < 75): # checks current health so player doesn't go above 100 health
                    player.health += 25
                else:
                    player.health = 100
                player.money -= 3
            else: # print message when the player doest have enough gold for the purchase
                print("Sorry you don't have enough money for the 25 healthkit.\n")
                time.sleep(2)
        if(choice == "2"):
            if(player.money >= 9):
                player.health = 100
                player.money -= 9
            else:
                print("Sorry you don't have enough money for the full heal.\n")
                time.sleep(2)
        if(choice == "3"):
            if(player.money >= 2):
                player.attackBuff += 0.20
                player.money -= 2
            else:
                print("Sorry you don't have enough money for the attack buff.\n")
                time.sleep(2)
        if(choice == "4"):
            if(player.money >= 2):
                player.defenseBuff += 0.20
                player.money -= 2
            else:
                print("Sorry you don't have enough money for the defense buff.\n")
                time.sleep(2)
        player.attackBuff = round(player.attackBuff, 2) 
        player.defenseBuff = round(player.defenseBuff, 2)

# Allows the user to revive their character and continue the game after losing a battle if they have enough gold. Only purchasable once.
# Player revives with full health (100) and the player must redo their last battle
def revive(player):
    # purchase message
    print("Hello " + player.name + " it looks like you have died. You can purchase a revive for 5 gold."
          "\nThis will allow you to continue the game with 100 health only purchasable once. You will also have to redo you last match."
          "\nWould you like to purchase this revive or end the game? (yes or no): ")
    answer = input()
    if(answer == "yes"):
        player.health = 100
        player.money -= 5
        player.revived = True # used to only allow player to purchase once
        print("\nYou have been revived!")
        playerStatus(player)
        
def main():
    name = getName()
    player = gladiator(name)
    intro(player)
    storyOne(player)
    storyTwo(player)
    storyThree(player)
    storyFour(player)
    storyFive(player)




if __name__ == "__main__":
    main()