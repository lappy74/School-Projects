#CS115 Vinci Jahniel Aure
#Game = Concept similar to The Legend of Zelda BOTW only here you'd only need 16 hearts to fight Ganon whereas in the original Game you'd need to defeat 4 mini bosses + reach a certian number of accolades to fight Ganon
import math
import random
import time
import sys
import os

print("""                                                                                                                                            
\033[36m**\033[0m\033[37m+++\033[0m\033[33m=-===+===+\033[0m\033[37m********++++======-------::..............................................:::--=----=+\033[0m
\033[36m**\033[0m\033[37m+==---=-+\033[0m\033[33m***********+++++=====-------:::::........................:..::.......:::.....:-----====\033[0m
\033[36m++++\033[0m\033[37m=--=+\033[0m\033[33m**************++=-::-----=--------:::::.........................:::..........:-----======+=\033[0m
\033[36m=====+\033[0m\033[37m***++=+\033[0m\033[33m*=-+++****++=-::..::..:--------::::::...................::................::--======+=:-\033[0m
\033[36m=+********+\033[0m\033[37m=-:+\033[0m\033[33m**+=++++=-::.::-======------:::::....:.................................:--=====++--:
\033[36m++======++++\033[0m\033[37m--==:-\033[0m\033[33m=++====::..:-=====--=-----::::.................................::..:---======++=-=
\033[36m*+++==========+\033[0m\033[37m=----======-===\033[0m\033[33m----==-::.:::::..:::...........................:::::-:-==-========++++
\033[36m###**++****+\033[0m\033[37m=+++++======---\033[0m\033[33m::-::::::::::.......:...........................::::--:::--========----==
\033[36m***##********\033[0m\033[37m++++=-::::-===\033[0m\033[33m-::--::--:::........:.:.........................:::::-::-=======+=--------
\033[36m####******+++++++\033[0m\033[37m=---:.:..:--=\033[0m\033[33m==-----:::::.................................:..:-::-============---==-
\033[36m#######*****+====\033[0m\033[37m----:::...:=\033[0m\033[33m=+%*--+:::....................................:::::--====-:----=====-==
\033[36m**********+++======\033[0m\033[37m---::::.:-+\033[0m\033[33m%%%+=::::....:.:::::........................:::::----------==-==-=====
\033[36m++++++++++++=====----\033[0m\033[37m::::::::+\033[0m\033[33m##%%#+-.:......::.::..........................:::::------==-=--=========
\033[36m+++++++++======-----::::....+\033[0m\033[33m##%%%%-....................:........:.......:::----------==----========
\033[36m=-+++++=========-------::::\033[0m\033[33m%##@@@@%+:::::::::::::.:..............:.......::::----------------========
\033[36m+==+++++++++=======---\033[0m\033[33m-+@@@%%%%%%*%+::::::::::::::::::........::::.....::::::-------------------====
\033[36m**+=-+++++++++========--+\033[0m\033[33m@@@%@@@%@##%#-::::::::::::..::::::::.::::::::::..:::::::::------------------
\033[36m+----=**++++++++++++++++\033[0m\033[33m@@%%%%###%%@%=====------::----:::---:-------------:::--::-=========---------
\033[36m**+-::-+++*********+****\033[0m\033[33m@@%%%%###%%@%=====------::----:::---:-------------:::--::-=========---------
\033[36m*#**+===+==++++===+*****\033[0m\033[33m%@%#*@%%%%#**+---:----:::::--::::==------------==-=---=============+++++====
\033[36m***+**++=+********++=++++\033[0m\033[33m**++%#++%++**+*-++++=+++===-+==+==+=-==-+==-----------===++++++++++++++++++
\033[36m::=***++++***********++*****\033[0m\033[33m#%+**#*+*****+=+++==+=+*++--+++**++*+=+=::---==+++++++++++***+***+******
\033[36m-==+++===++************++++*\033[0m\033[33m%#+**%#*********=+*+***++=+*++*++**=+=-++=--==+=+++++***++-=+***********
\033[36m-=+==****************++***=\033[0m\033[33m#%+==+%%+********+=+++=---=+*+***********+*+*+++++**+****++++++**********
\033[36m****+*+***#####*#***********\033[0m\033[33m%++=-#*--=++****++=+*****************+=+**+=***+************************
\033[36m*****+***########**#**+**+=\033[0m\033[33m#%=+++%%#*+*******+++++******##******+****==+===+++++***+**####*****##***
\033[36m***+++*********###**##%@##%%%\033[0m\033[33m####%%%*+=*==*********++++++++****###*###********+******************###
\033[36m###**#*******##*****%@%%%%%%%%%@@%%%%%%%#=*\033[0m\033[31m+*******#=----:-+*########**#*******###############***###
\033[36m####*##**#########%%@##%%%%@@@@%%%%%%%%%%%%*\033[0m\033[31m=*%=*##*+*###=+#########################*****###*+====-=
\033[36m#*#####******+++##%%#%%%%%%%%%%%%%%@@@%%%%%%%%#@+####++*-==**#####***######################*******##*******##%
\033[36m*+**++++*++=+#%%#@@%#%%%%%%%%@@%%%%%@%%%%%%%%%##=#*#******++**##+***#######*+++*########*+++====*##%\033[0m
\033[32m+++++++=+==##%*#@@####%%%%%@%%%%%%%%@%%%%%%%%%%++********************#####+===+++*###*#****+*++**+##\033[0m
\033[32m=-*++#-+-*##%%@@@#**%%%%%%%%%%%@@@%%%%%@%%%%%###+=***+******+**+*********+**#****##########***===+==\033[0m
\033[32m+###+++-++#%%@@%###@@%+#%%%%%#%%@@%%%%%%%%%%%%##+=++=++****+++++++*****####################****+++++\033[0m
\033
""") #Opening Art for the game, the image was converted to ascii using a website
print("WWelcome to the Expedition of Link, a game derived from the \033[32mLegend of Zelda BOTW.\n\033[0mIn this game you're supposed to get \033[31m16 hearts\033[0m to pull out the Master Sword and then defeat \033[31mGANON to save the Kingdom of Hyrule.\n\033[0mDo you think you have what it takes to succeed? You better!\n\033[32mThis is where your Story Begins, Link!")
#print statement welcoming the player into the game, shows who the player is playing as
def display_inventory(inv):
    print(f"Inventory: {', '.join(inv) if inv else 'Empty'}")
#prints the content of the inventory at all times

def final_fight(hearts, inventory): #Function that will handle the final boss battle against Ganon with the hearts and inventory parameter to carry the stats into the function
        print("You've gathered the required strength and the \033[33mMaster Sword!\033[0m The final battle begins!")
        final_boss_health = 500 #Health of the boss = 500 points
        while hearts > 0 and final_boss_health > 0:
            action = input("Attack or Defend? ").lower() #.lower allows for input of lowercase or uppercase input since it automatically translates it
            if action == "attack":
                damage = random.randint(20, 150) #Random Player Damage
                if hearts <= 4:
                    print("The Master Sword has recognized how dire the situation is and has entered \033[31mAnnihilation Mode.\033[0m")
                    damage = damage * 2 #If player is critically low HP, Triggers Master Sword Special Ability
                if "Strength Potion" in inventory:
                    damage = damage * 3 #If player has buff potion for higher ATK
                final_boss_health -= damage
                print(f"You dealt \033[32m{damage}\033[0m damage! Boss health: \033[31m{final_boss_health}\033[0m")
            elif action == "defend":
                hearts -= 1
                print(f"Invalid input, the boss attacked you, you lost \033[31m1\033[0m heart")
                print("You defended!") #Blocks some damage
            else:
                damageh = random.randint(2,6)
                if "Armor" in inventory: #Reduces the damage received
                    damageh = damageh - 2
                if "Bokoblin Shield" in inventory: #Blocks some damage but since it's a low level shield, leaks 1 hp of damage
                    damageh = damageh - 1
                hearts -= damageh
                print(f"Invalid input, the boss attacked you, you lost \033[31m{damage}\033[0m hearts") #If you give an incorrect input the boss takes it as a moment of weakness and hits you
 
            if final_boss_health > 0: #Until the boss is still alive, keep going
                boss_damage = random.randint(2, 6)
                if "Armor" in inventory:
                    boss_damage = boss_damage - 2
                if "Bokoblin Shield" in inventory:
                    boss_damage = boss_damage - 1
                hearts -= boss_damage
                print(f"The boss dealt \033[31m{boss_damage}\033[0m damage! Your health: \033[31m{hearts}\033[0m") #shows how much damage you take and how much hearts you have left like a turn based system
            
        if hearts <= 0:
            print("You were defeated by the final boss.") #If you die to the boss, when you lose all hearts
            if "savegame.txt" == True:
                os.remove("savegame.txt")
            print("\033[31mGame Over!\033[0m")
            time.sleep(5) #if you lose you get 5 seconds to read the death message
            sys.exit() #GGs
        else:
            print("Congratulations! You defeated the final boss!") #If you win against Ganon and become the hero
            time.sleep(3) #3 second delay before showing the stars
            print("""\033[33m
           .    ==                 .              ==                                ==                
             . -::=              .               =::-                              =::=               
              --:.:-=          .                =:..:=                            =:..:-              
             =-:::::-                          =::::::=                          =-:::::=             
            =-:::::::-                        =::::::::=                        =-:::::::=            
    ======--::::::::::----====  .    ======---::::::::::---======       ======---:::::::::--=====-    
=-:.::::::::::::::::::::::::::::-===:..:::::::::::::::::::::::::::-==-:..:::::::::::::::::::::::::::-=
  =-:.::::::::::::::::::::::::--.   =-::::::::::::::::::::::::::-=    =-:.::::::::::::::::::::::::-=  
    =-::::::::::::::::::::::-=        =-::::::::::::::::::::::-=        =-::::::::::::::::::::::-=    
      =-::::::::::::::::::-=            =-::::::::::::::::::-=            ==::::::::::::::::::-=      
        =::::::::::::::::-                =::::::::::::::::-                -::::::::::::::::=        
        =::::::::::::::::-               =-::::::::::::::::-=               -::::::::::::::::-=       
       =-::::::::::::::::-=              =-:::::::::::::::::=              =-:::::::::::::::::=       
       =:::::::-==--::::::=              -::::::--==--::::::-              =:::::::-==--::::::=       
      =-:.:-==      ==-::.-=            =-:.:-==      ==-:::-=             =..:-==      ==-:::-=      
      =--=              =--=            ====              ====            =--=              ==-=      \033[0m""")
            #ASCII art generated from website, printed using six quotation marks
            time.sleep(3)
            print("You have now completed the game and now the Kingdom of Hyrule has been saved by \033[33mYOU!\033[0m\nCongratulations on this achievement and if you want to try again, feel free to do so.\n\033[33mI HOPE YOU ENJOYED!\033[0m")
            time.sleep(8) #8 seconds delay so that the user can read what was printed to the screen
            sys.exit()


def can_begin_final_fight(hearts, inventory): #Function that handles whether or not the player is worthy enough to fight the final Boss Ganon
    required_hearts = 16  # Number of hearts required
    if hearts >= required_hearts:
        print("\033[32mKorok\033[0m:You can now fight Ganon and you've obtained the \033[33mMaster Sword!\033[0m\n") 
        print("""    
             _
           .!=!.
           \===/
           |>X<|
           |>X<|
           |>X<|
           |>X<|
           |>X<|
           |>X<|
           |>X<|
           |>X<|
           |>X<|
           |>X<|
          .-----.
      /\__:-----:__/\.
    ./ ._. \.-./ ._. \.
  ./ ./  -.  V  .-  \. \.
 /__/      \   /      \__\.
           |! !|
           |! !|
         ./ . . \.
         |!.V V.!|
         \.\ V /./
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
         | |   | |
          \.\ /./
            \V/             """) #Prints ASCII Art of Master Sword from DevianArt
        inventory.append("Master Sword") #Adds Master Sword to user inventory allowing you to fight the final Boss
        final_fight(hearts, inventory) #Calls the function to fight the final Boss
        return True
    else:
        print(f"You aren't worthy enough\nCome back when you can actually fight! Also, you need {16 - hearts} more hearts.") #SHows how much more hearts you need to become worthy of fighting Ganon.
        return False #Returns back to Start since there's nothing to do besides gain more experience to be worthy
    

def file(fp, mode, hearts=None, inventory=None): #Handles the file writing/saving/deleting of the game
    if mode == 'save':
        if hearts is None or inventory is None:
            return None #If there's nothing that has begun and the player is already trying to save, how will you save something that has nothing in it?
        try:
            with open(fp, 'w') as f: #Try and except aids in the error management of the program so that it doesn't crash, instead allows possibilities within the program to see if it can run or not.
                f.write(f"{hearts}\n")
                f.write(','.join(inventory)) #Writes into a txt file that can be read by the game later if the user decides to load said file.
            return None
        except OSError: #Returns a system error such as not finding the file that should be read.
            return None
    elif mode == 'load':
        if not os.path.exists(fp): #if the file doesn't exist, gets ignored and prints and error message
            return None
        try:
            with open(fp, 'r') as f:
                hearts = int(f.readline().strip()) #Reads the content of the TXT file
                inv_str = f.readline().strip()
                inventory = inv_str.split(',') if inv_str else [] #initializes a list called inventory, prevents errors from the inventory being empty
            return hearts, inventory
        except (OSError, ValueError): #ValueError = Handles an error wherein the function gives a correct value type but inappropriate amount.
            return None
    else:
        return None

def mob_fight(hearts, inventory): #Handles the Mob Fight with a Bokoblin
    bokoblin_health = 35 #HP of Bokoblin
    while hearts > 0 and bokoblin_health > 0: #While player and bokoblin hearts aren't 0 continue fighting
        linput = input("You're now trapped in the room and now facing against a Bokoblin!\nAttack, Dodge: \n") #Begin
        action = linput.lower() #Action lower = can type in mix of uppercase or lowercase but then the .lower converts all to lowercase
        if action == "attack":
            player_damage = random.randint(5, 25) #Random damage from player to the bokoblin
            bokoblin_health -= player_damage #Bokoblin hp - player_damage
            print(f"You attacked the Bokoblin! It lost \033[31m{player_damage}\033[0m hp.")
        elif action == "dodge": #if you Dodge the bokoblin you receive no damage and the function continues to be ran
            print("You dodged! The Bokoblin missed you.")
        else:
            mob_damage = random.randint(1, 3) #Bokoblin damage to player(Lowest possible and highest possible)
            hearts -= mob_damage
            print(f"Invalid action. Choose Attack or Dodge. You lost \033[31m{mob_damage}\033[0m hearts.")
        if bokoblin_health > 0 and action in ("attack", "dodge"):
            print(f"Bokoblin's Health: {bokoblin_health}")
            print(f"Your Health: \033[31m{hearts}\033[0m") #Shows bokoblin and your health after the attack or dodge happens
    if hearts <= 0: #If you die to the bokoblin
        print("\033[31mYou were defeated!")
        if "savegame.txt" == True:
            os.remove("savegame.txt") #Deletes save file
        print("\033[31mGame Over!\033[0m") #Game over
        time.sleep(5)
        sys.exit() #Exits the game entirely
    else:
        print("You defeated the Bokoblin!") #You won
        inventory.append("Bokoblin Shield")
        inventory.append("Meat") #Loot from the bokoblin
        return dungeon(hearts, inventory) #Calls back the main dungeon function and locks this area

def wep_check(inventory): #Checks for prescence of weapon, if there's no weapon, you can't fight the bokoblin
    linput = input("Check for weapon? Y/N: \n").upper() #.upper immediately turns inputs into uppercase
    if linput == "Y":
        if "Royal Broadsword" in inventory or "Bomb" in inventory or "Royal Bow" in inventory or "Rusty Sword" in inventory:
            return "Granted" #If any weapon is present in the inventory you're granted with a key "Granted" to enter further
        else:
            return "Denied" #No weapon = yikes
    elif linput == "N":
        print("See you")
        return "Denied" #You went but went back
    else:
        print("Invalid Input")
        return wep_check(inventory)

def access(ok, inventory, hearts): #Checks access key
    if ok == "Granted":
        print("You may enter the room") #Determines whether you can fight the bokoblin
    else:
        print("You can't go in yet.") #No fight, sad, get weapon first
        return dungeon(hearts, inventory)

def heart_elixir(hearts, inventory, elixir_id): 
    locked_areas[elixir_id] = True # lock the specific reward after it's been taken
    print("""
                     #############                     
                     #############                     
                 ####*************####                 
               ######+=---======+*######               
               ######+=-----====+*######               
               ######+=-----====+*######               
               %%%%%%*=:::::----=*%%%%%%               
               %%%%%%*=...::----=*%%%%%%               
               %%%%%%*=::::-----+*%%%%%%               
                %%%%%#############%%%%%                
                     %%%%%%%%%%%%%                     
                 #####################                 
               ######*+++++++++++*######               
               ######*+=========+*######               
           %%%%#*****++=========++****##%%%%           
          %%%%%#+=----::::::----==+++**#%%%%%          
          %%%%%#+=---::...::----==++++*#%%%%%          
          %%%%%#+=-----::::-----=++++*##%%%%%          
           %%%%######************#######%%%%%          
               %%%%%%#############%%%%%%               
           %%%%%%%%%%#############%%%%%%%%%%           
          %%%%%%#######################%%%%%%          
          %%%%%%#######################%%%%%%          
      %%%%#######****#####%%%%%%#############@@@@      
    %%%%%%*=:::--=+++**###%%%%%%%%%%%#+-:::=*@@@@@@    
    %%%%%%*=....-====+*###%%%%%%%%%%%#=:...-*@@@@@@    
%%%%######+-...:-=++++*####%%%%%%%%%%#+-:::=*%%%%%@@@@@
%%%%#+-:::--====+****########%%%%%%%%%#####*+===+*%@@@@
%%%%#=:...:-===+**##############%%%%%%%%%%%*+---=*%@@@@
%%%%#+:...:-++++*###############%%%%%%%%%%%#+---=*%@@@@
%%%%%*=---=+***#################%%%%%%%%%%%#+===+*%@@@@
@@@@%*=---=*####################%%%%%%%%%%%#*===+#%@@@@
@@@@%*+===+*####################%%%%%%%%%%%#*++++#%@@@@
@@@@%%%%%%#+====*################%%%%%######%%%%%%%@@@@
    @@@@@@#+---=+*###############%%%%%######%@@@@@@    
    @@@@@@#*====+*################%%%%######%@@@@@@    
     @@@@@%%%%%#*+++++*###############%%%%%@@@@@@@     
          @@@@@%#+===+*###############%%@@@@@          
          @@@@@%#+++++*###############%@@@@@@          
           @@@@@%%%%%%###########%%%%@@@@@@@@          
               @@@@@@%###########%@@@@@@               
               @@@@@@%%##########%@@@@@@               
                @@@@@@@%%%%%%%%%@@@@@@@                
                     @@@@@@@@@@@@@                     
                     @@@@@@@@@@@@@                     """) #Ascii art of Heart Potion from terraria
    print("You've discovered a heart elixir!")
    linput = input("Consume/Use elixir?: \n").lower()
    if linput in ("consume", "use"):
        hearts += 4 #Adds 4 health points to user
        time.sleep(0.5)
        print("You just earned 4 hearts!")
        return dungeon(hearts, inventory) #Returns to dungeon
    elif linput == "store":
        inventory.append("Heart Elixir") #Stores it if the user doesn't want to use it yet
        return dungeon(hearts, inventory)
    else:
        print("What?")
        return heart_elixir(hearts, inventory, elixir_id)

def heart_elixirn(hearts, inventory, elixir_id): 
    locked_areas[elixir_id] = True # lock the specific reward from a different area but same item
    print("""
                     #############                     
                     #############                     
                 ####*************####                 
               ######+=---======+*######               
               ######+=-----====+*######               
               ######+=-----====+*######               
               %%%%%%*=:::::----=*%%%%%%               
               %%%%%%*=...::----=*%%%%%%               
               %%%%%%*=::::-----+*%%%%%%               
                %%%%%#############%%%%%                
                     %%%%%%%%%%%%%                     
                 #####################                 
               ######*+++++++++++*######               
               ######*+=========+*######               
           %%%%#*****++=========++****##%%%%           
          %%%%%#+=----::::::----==+++**#%%%%%          
          %%%%%#+=---::...::----==++++*#%%%%%          
          %%%%%#+=-----::::-----=++++*##%%%%%          
           %%%%######************#######%%%%%          
               %%%%%%#############%%%%%%               
           %%%%%%%%%%#############%%%%%%%%%%           
          %%%%%%#######################%%%%%%          
          %%%%%%#######################%%%%%%          
      %%%%#######****#####%%%%%%#############@@@@      
    %%%%%%*=:::--=+++**###%%%%%%%%%%%#+-:::=*@@@@@@    
    %%%%%%*=....-====+*###%%%%%%%%%%%#=:...-*@@@@@@    
%%%%######+-...:-=++++*####%%%%%%%%%%#+-:::=*%%%%%@@@@@
%%%%#+-:::--====+****########%%%%%%%%%#####*+===+*%@@@@
%%%%#=:...:-===+**##############%%%%%%%%%%%*+---=*%@@@@
%%%%#+:...:-++++*###############%%%%%%%%%%%#+---=*%@@@@
%%%%%*=---=+***#################%%%%%%%%%%%#+===+*%@@@@
@@@@%*=---=*####################%%%%%%%%%%%#*===+#%@@@@
@@@@%*+===+*####################%%%%%%%%%%%#*++++#%@@@@
@@@@%%%%%%#+====*################%%%%%######%%%%%%%@@@@
    @@@@@@#+---=+*###############%%%%%######%@@@@@@    
    @@@@@@#*====+*################%%%%######%@@@@@@    
     @@@@@%%%%%#*+++++*###############%%%%%@@@@@@@     
          @@@@@%#+===+*###############%%@@@@@          
          @@@@@%#+++++*###############%@@@@@@          
           @@@@@%%%%%%###########%%%%@@@@@@@@          
               @@@@@@%###########%@@@@@@               
               @@@@@@%%##########%@@@@@@               
                @@@@@@@%%%%%%%%%@@@@@@@                
                     @@@@@@@@@@@@@                     
                     @@@@@@@@@@@@@                     """)
    print("You've discovered a heart elixir!")
    linput = input("Consume/Use elixir?: \n").lower()
    if linput in ("consume", "use"):
        hearts += 4
        time.sleep(0.5)
        print("You just earned 4 hearts!")
        return cliff(hearts, inventory)
    elif linput == "store":
        inventory.append("Heart Elixir")
        return cliff(hearts, inventory)
    else:
        print("What?")
        return heart_elixirn(hearts, inventory, elixir_id) #Same as the previous item merely a different id and use case
    
def chest(hearts, inventory): #Handles opening the chest in the dungeon if you reach this far (YOU NEED TO)
    visited_areas["chest"] = True
    print("""\033[33m
       ___________________________________
      /                                   \.
     /_____________________________________\ 
    /                                       \.
   /_________________________________________\.
  |   _____________________________________   |
  |  |                                     |  |
  |  |           ______________            |  |
  |  |          |              |           |  |
  |  |          |              |           |  |
  |  |          |______________|           |  |
  |  |                                     |  |
  |  |_____________________________________|  |
  |___________________________________________|
     /                                     \.
    /_______________________________________\.
\033[0m""") #ASCII art of a chest
    linput = input("If you wish to open the chest, type 'Open Chest'. If not, type 'Move Along': \n").title()
    if linput == "Open Chest":
        items = ["Rusty Sword", "Royal Bow", "Royal Broadsword", "Bomb"]
        x = random.choice(items) #Random items from the 4 above, initially submitted as mutltiple if statements, optimized into a list, all do the same amount of damage but a different level of satisfaction
        
        if x == "Rusty Sword":
            print("""
=-------=---------------------------------------------
=-------------:---------------------------------------
=-----------------------------------------------------
=-----------------------------------------------------
=----------------------------------:------------------
=----------------------------------+++++++++++--------
=---------------------------------=#####%%##%#=-------
=------------------------------===+*******##%#=-------
=-----------------------------=*##*:::-:::+###=-------
=------------------------:-===+*#*+----:::*###=-------
=-------------------------=#%%#+==+***=:--*###=-------
=-------------------------=*##*+==++++=---+###=-------
=----------------------*###+==+***+-::+###=-----------
=--------------====---=*###+=++++++---+###=-----------
=----------+%%%%%%%%%%#+==++**+-::=#%#*-::------------
=----------+%%%%%%%%###+++++**=---=###+---------------
=-------+++*%%%#***#%%%***+===*###*-------------------
=-------+++*%%%#**##%%%****+==+###*---:---------------
=-------+++++++*%%%#**#%%%%##%*-----------------------
=------=+++++++*%%%#**#%%%%%#%*-----------------------
=----------+%%%#+*+#%%%##*#%%%*=:---------------------
=---------:+%%%#+++#%%%##*#%%%*=----------------------
=------=*%######%#%****#%%%%%%*-:---------------------
=------=#%%#**##%%%*+++#%%%%%%*=:---------------------
=---=++*#%%%%%%*-===+++++++=--------------------------
=---=++*%%%%%%%*:--=+++++*+---------------------------
=---++++****====----=--===----------------------------
=---+++++++=------------------------------------------
=---========------------------------------------------
=-----------------------------------------------------""") #From Stardew Valley
        
        if x == "Royal Bow":
            print("""
     %%%%%%%%%%@@%%%@@                                
     %%%%%%%%%%@@%%%@@                                
     %%%%%%%%%%@@%%%@@                                
%%%%%##******#%@@%%%@@                                
%%%%%#*=::::=+#@@%%%@@                                
%%%%%#*=::::-+#@@%%%@@                                
%%%%%#*=::::-+#@@%%%@@                                
%%%%%#+=----=+*#####**++++++                          
     =======+++****+++++++++                          
     =======+++****+++++++++                          
     ========+++++++++++++++++++++      ########      
     ==========++++=--::::-=+++++++    ##########     
     -------========-:....-=+++++++    ##########     
     -------========-:....-=+++++++    ##########     
     -------========-:::::--====++*@@@%%#********     
     ==========    -------------=+#@@@%%#*+++++++     
     ==========    -------------=+#@@%%%*+=======     
     ==========    -------------=+#@@%%%*+=======     
     ----------    --------=======+++++==-----=+#%%%%%
     ----------           +++++++=-:::::::::::-*#%%%%%
     ----------           +++++++=-:::::::::::-*#%%%%%
     ----------           +++++++=-:::::::::::=+#%%%%%
     ==========           ++++++++=======-----=+******
     ==========                 ++++++++=======+++++++
     ==========                 ++++++++=======+++++++
     ==========           #######*++++++++++++++++++++
     ==========           #######*+====+*#%%%%%%%     
     ==========           #######*+====+*#%%%%%%%     
     ==========           #######*+====+*#%%%%%%%     
     ==========           ######**=----=+*%%%%%%%     
     ==========           ######*+=-------            
     ==========           ######*+=-------            
     ==========           ######*+=-------            
     ==========           ######*+=-------            
     ----------           ######*+=-------            
     ----------           ######*+=-------            
     ==========           ######*+=----=+*%%%%%%@     
     ==========           #######*+====+*#%%%%%%%     
     ==========           #######*+====+*#%%%%%%%     
     ==========           #######*+====+*#%%%%%%%     
     ==========           #######**************#%%%%%%
     ==========                 #######*+=====+*#%%%%%
     ==========                 #######*+=====+*#%%%%%
     ==========            ++++++*******+=----+*#%%%%%
     ==========           +++++++========-----=++*****
     +======+==           ++++++=======---::::-=++++++
     ++=====+==           ++++++=======---::::-=++++++
     ==========    *******++=====+++++++==-----=++++++
     ----------    *******++=====+#%%%%#*+=======     
     ----------    *******++=====+#%%%%#*+=======     
     ----------    *******++=====+#%%%%#*+=======     
     +=============++++++++******##%%%%#*++++++++     
     ++++++++++===========+#%%%%%%%    ++++++++++     
     ++++++++++===========+#%%%%%%%    ++++++++++     
     ++++++++++===========+*%%%%%%%    ++++++++++     
     *******++=============+#%%%%%%     ++++++++      
     *******++==============                          
     *******++==============                          
%%%%%#**++++++++++++========                          
%%%%%%*+=====+********                                
%%%%%%*+=====+********                                
%%%%%%*+=====+********                                
%%%%%%##****##########                                
     @@@@@@@%%%######%                                
     @@@@@@@%%%######%                                
     @@@@@@@%%%######%                                """) #From Terraria = Ice Bow
            
        if x == "Royal Broadsword":
            print("""
                                                  ****
                                                **++**
                                              **==**  
                                          ****==**    
                                      ****==--****    
                                    **++==----**      
                                  **++==----++**      
                                **++==----==**        
                                **==----==++**        
                              **++==--==++**          
                              **==--==++**            
                          **++++--==****              
                          ++==--++**                  
              **      **++==--==++                    
            ****    **++----==++**                    
        %%  **++****++--::--++                        
    %%%%##  **++**++--::--++**                        
  %%++++++%%##++++--::--++**                          
%%++%%%%**++%%--=-::--++**                            
%%##%%%%##**%%====--++****                            
%%%%  %%##++####++--++**++****                        
  %%  %%##****##********++****                        
      %%##**++**######******                          
    %%%%**++##++##++####%%                            
    %%**++##%%##%%##++##%%                            
  %%**++**%%  %%%%%%++%%                              
%%++****%%        %%++%%                              
%%##++%%      %%%%++%%                                
%%%%%%          %%%%                                  """)#From Terraria = Volcano or Lava Greatsword
       
        if x == "Bomb":
            print("""
                                  #######              
                                  #######              
                             ############              
                             #######                   
                             #######                   
                        ############                   
                        #######                        
                        #######                        
                        %%%%%%%                        
                        @@@@@@@                        
                    %%%%%@@@@@%%%%%                    
                   %%%%%%%%%%%%%%%%%                   
                   %%%%%%%%%%%%%%%%%                   
         %%%%%%######%%%%%%%%%%%%%%%%%%%%%%%%%         
         %%%%%%####################%%%%%%%%%%%         
         %%%%%%####################%%%%%%%%%%%         
    %%%%%%######**************###############%%%%%%    
    %%%%%%#####***************###############%%%%%%    
    %%%%%%#####***************###############%%%%%%    
    ######*****+++++++++++*********##########%%%%%%    
    ######****++========++*********##########%%%%%%    
%%%%######*++++=========++++++*****##########%%%%%%%%%%
%%%%%####*+====-----=========++****#####%%%%%#####%%%%%
%%%%%####*+====-----=========++****#####%%%%%#####%%%%%
%%%%%####*++++==---======++++++****#####%%%%%#####%%%%%
%%%%%#####****++========++*********#####%%%%%#####%%%%%
%%%%%#####****++========++*********#####%%%%%#####%%%%%
%%%%%######****+++++++++++********######%%%%%#####%%%%%
%%%%%##########***************##########%%%%%#####%%%%%
%%%%%##########***************##########%%%%%#####%%%%%
%%%%%%%%%###########################%%%%#####%%%%%%%%%%
    %%%%%%#########################%%%%%#####%%%%%%    
    %%%%%%##########################%%%%#####%%%%%%    
    %%%%%%%%%%%#####%%%%%%%%%%%%%%%#####%%%%%%%%%%%    
    %%%%%%%%%%%#####%%%%%%%%%%%%%%%#####%%%%%%%%%%%    
    %%%%%%%%%%%%#######################%%%%%%%%%%%%    
         %%%%%%%%%%%###############%%%%%%%%%%%         
         %%%%%%%%%%%###############%%%%%%%%%%%         
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%         
                   %%%%%%%%%%%%%%%%%                   
                   %%%%%%%%%%%%%%%%%                   """) #Terraria Bomb
        print(f"You've taken {x}!\n")
        inventory.append(x) #Adds what you took into the Inventory
        return dungeon(hearts, inventory) #Calls back the dungeon function
    elif linput == "Move Along": #You can access the chest again later
        print("You decided to move along without opening the chest.")
        return dungeon(hearts, inventory)
    else:
        print("I don't know what you mean.\n")
        return chest(hearts, inventory)

def dungeon_d(hearts, inventory): #Just making sure you want to go further north
    visited_areas["dungeon_d"] = True
    linput = input("Do you want to go deeper?\nYes or No: \n").title()
    if linput == "Yes":
        print("You've found a chest!") 
        chest(hearts, inventory)
        return dungeon(hearts, inventory)
    elif linput == "No":
        print("Aw, you missed out on something good\nReturning to dungeon.") #Immediately gets sent back to the beginning of the function Dungeon
        return dungeon(hearts, inventory)
    else:
        print("What?")
        return dungeon_d(hearts, inventory)

def dungeon(hearts, inventory): #The main dungeon function if the user goes north 
    visited_areas["dungeon"] = True #Updates the list that you've visited the dungeon
    linput = input("You're now in a \033[33mDungeon\033[0m.\nYou can choose to go back or go deeper into the dungeon.\n\033[34mBack\033[0m, \033[34mForward\033[0m, \033[34mLeft\033[0m, \033[34mRight\033[0m, \033[32mInventory:\033[0m \n").title()
    if linput == "Back":
        print("You've gone out of the Dungeon!") #returns you to starting location
        return start(hearts, inventory)
    elif linput == "Forward": #Calls one of the two functions for the Heart Elixir
        if locked_areas["dungeon_forward_elixir"]:
            print("You've already visited this area. This area is now locked.") #if you've gone to the area before
            return dungeon(hearts,inventory)
        print("You've gone even deeper and discovered a heart elixir!") #if the area hasn't been explore before, will call the function for one of the heart elixirs
        return heart_elixir(hearts, inventory, "dungeon_forward_elixir")
    elif linput == "Left":
        if visited_areas["chest"]: #calls function to go deeper and also handles the chest execution
            print("You've already visted this area. This area is now locked.")
            return dungeon(hearts, inventory)
        return dungeon_d(hearts, inventory) #calls function if it's still unlocked
    elif linput == "Right":
        if locked_areas["dungeon_right"]: #If the mob has been fought before it becomes locked
            print("This area is now locked.")
            return dungeon(hearts, inventory)
        ok = wep_check(inventory)
        if ok == "Granted": #If weapon is present then you can enter and proceed to fight
            print("You may enter the room")
            locked_areas["dungeon_right"] = True #locks the area after
            return mob_fight(hearts, inventory)
        else:
            print("You can't go in yet.") #You don't have a weapon yet
            return dungeon(hearts, inventory)
    elif linput == "Inventory": #checks inventory
        display_inventory(inventory) 
        return dungeon(hearts, inventory)
    else:
        print("Invalid Input")
        return dungeon(hearts, inventory)

def npc_bb(hearts, inventory): #Talks to an NPC that would either give you a Blueberry jam or End your session
    locked_areas["npc_bb"] = True #locks area after
    visited_areas["npc_bb"] = True #Adds to visited areas
    linput = input("Shaney: Hi! Do you want some \033[34mBlueberry Jam?\033[0m\nI picked the blueberries myself! Y/N: \n").upper()
    if linput == "Y":
        inventory.append("Blueberry Jam") #Adds blueberry jam if the user agrees
        print("I hope you enjoy it, goodluck in your travels!")
        return cliff(hearts, inventory)
    elif linput == "N": #If you refuse
        linput2 = input("Shaney: Are you sure? Y/N: \n").upper()
        if linput2 == "Y":
            print("Shaney: You dare say no to grace?\nEnjoy the \033[31mAbyss!\033[0m")
            print("\033[31mGame Over!\033[0m")
            if "savegame.txt" == True: #Your game ends because you didn't want Blueberry Jam, silly world
                os.remove("savegame.txt") #Deletes txt file
            time.sleep(5)
            sys.exit()
        elif linput2 == "N": #if you change your mind and want to take the jam
            inventory.append("Blueberry Jam")
            print("Glad you made up your mind!\nI hope you enjoy it, goodluck in your travels!") #She lets you go
            return cliff(hearts, inventory)
        else:
            print("Shaney: I don't have the best hearing, can you repeat that for me?")
            return npc_bb(hearts, inventory)
    else:
        print("Shaney:I don't have the best hearing, can you repeat that for me?")
        return npc_bb(hearts, inventory)

def trap_s(hearts, inventory): #TRoll trap for the area wherein you have to guess a number until they let you go
    locked_areas["trap_s"] = True #locks the area, no more trolls after one occassion
    try:
        linput = int(input("Troll: Guess a number between 1-10 to get out HEHEHE!: \n"))
    except ValueError: #If the supplied number is in a different type eg"STR or Float"
        print("Troll: That's not a number HEHEHE!")
        return trap_s(hearts, inventory)
    s = random.randint(1, 10)
    hearts_lost = 0 #You lose 1 heart every time you get a wrong guess but you regain it all in the end if you get it right
    while linput != s:
        print("Troll: Try AgAIn HEHEHE!")
        hearts -= 1
        hearts_lost += 1
        try:
            linput = int(input(f"Troll: Guess a number between 1-10 to get out HEHEHE!:\nYou have\033[31m{hearts}\033[0m\n"))
        except ValueError:
            print("Troll: That's not a number HEHEHE!")
            return trap_s(hearts, inventory)
        if hearts == 0:
            print("\033[31mYou were trolled!")
            if "savegame.txt" == True:
                os.remove("savegame.txt") #Deletes save file if you lose from the troll
            print("\033[31mGame Over!\033[0m")
            time.sleep(5)
            sys.exit()
    hearts += hearts_lost #combines the hearts you lost 
    print("Troll: You got it Right! You lucky traveller HEHEHE.")
    return cliff(hearts, inventory)

def cliff(hearts, inventory): #Cliff function if you decide to go east
    visited_areas["cliff"] = True #Becomes true and updates the value
    linput = input("You've discovered a cliff\nDo you want to go \033[31mForward\033[0m or \033[32mRemain\033[0m or Inventory?: \n").title()
    if linput == "Forward":
        print("You just killed yourself.")
        print("\033[31mGame Over!\033[0m")
        time.sleep(5)
        if "savegame.txt" == True:
            os.remove("savegame.txt") #If you decided to walk off the cliff, obviously you die
        sys.exit()
    elif linput == "Inventory":
        display_inventory(inventory)
        cliff(hearts, inventory)
    elif linput == "Remain":
        while True:
            linput2 = input("Wise choice, go \033[34mNorth/South/West/Back\033[0m: ").title() 
            if linput2 == "North":
                if locked_areas["cliff_north_elixir"]: #Different id for heart elixir
                    print("This area has already been explored.") #if the areas here are locked, they get their own print statements else they call the function that's supposed to be ran
                    continue # Use continue to loop again
                heart_elixirn(hearts, inventory, "cliff_north_elixir")
                return cliff(hearts, inventory)
            elif linput2 == "South":
                if locked_areas["trap_s"]:
                    print("You've already faced the troll, don't go there again.")
                    continue # Use continue to loop again
                trap_s(hearts, inventory)
                return cliff(hearts, inventory)
            elif linput2 == "West":
                if locked_areas["npc_bb"]:
                    print("You've faced with a Sweet lady before but now she's nowhere to be found.")
                    continue 
                npc_bb(hearts, inventory)
                return cliff(hearts, inventory)
            elif linput2 == "Back": # Added Back option
                return start(hearts, inventory) # Return to start
            else:
                print("Give a valid input please.")
    else:
        return cliff(hearts, inventory)

def camphos(hearts, inventory): #Calls a dangerous mob, the guardian 
    locked_areas["camphos"] = True #Updates the area to be locked after
    print("Uh-Oh you robbed the camp and got ambushed by a \033[31mGuardian!\033[0m")
    if not any(item in inventory for item in ["Royal Broadsword", "Bomb", "Royal Bow", "Rusty Sword"]): #Checks for weapon, if you don't have one, you die instantly
        print("You were defeated instantly!\nYou had no weapon \033[31mSilly\033[0m!")
        if "savegame.txt" == True:
            os.remove("savegame.txt")
        print("\033[31mGame Over!\033[0m")
        time.sleep(5)
        sys.exit()
    else: #if you have weapon you fight with guardian
        GuardianH = 100 #guardian hp
        while hearts > 0 and GuardianH > 0:
            linput = input("Attack, Dodge: ").lower()
            if linput == "attack":
                player_damage = random.randint(20, 55) #Player damage to the guardian 
                GuardianH -= player_damage
                print(f"You attacked the Guardian! It took {player_damage} hp.")
            elif linput == "dodge":
                print("You dodged! The Guardian missed you.") #no damage to you since you dodged
            else:
                mob_damage = random.randint(0, 6) #damage of the guardian
                hearts -= mob_damage
                print(f"Invalid action. Choose Attack or Dodge. You lost \033[31m{mob_damage}\033[0m hearts.")
            if GuardianH > 0 and linput in ("attack", "dodge"):
                print(f"Guardian's Health: \033[33m{GuardianH}\033[0m")
                print(f"Your Health: \033[31m{hearts}\033[0m")
        if hearts <= 0:
            print("You were defeated!")
            if "savegame.txt" == True:
                os.remove("savegame.txt")
            print("\033[31mGame Over!\033[0m")
            time.sleep(5)
            sys.exit()
        else:
            print("You defeated the Guardian!")
            inventory.append("Star Potion") #Overpowered potion
            inventory.append("Rusty Screw") #miscellaneous loot
            return start(hearts, inventory)

def camp(hearts, inventory): #Handles the camp function when the player goes west
    locked_areas["camp"] = True #updates the area to be locked afterwards
    visited_areas["camp"] = True #also updates the visited areas
    linput = input("You discovered an abandoned camp, you can take the loot here if you want to. Take/Dont? (Inventory): ").title()
    if linput == "Take":
        inventory.append("Apple")
        inventory.append("Mysterious Potion") #if you take this, you're kinda screwed subtly
        camphos(hearts, inventory) #Fight the Guardian
        return camp(hearts,inventory) 
    elif linput == "Inventory":
        display_inventory(inventory)
        camp(hearts, inventory)
    elif linput == "Dont":
        print("Nevermind") #Good Lad but you can't come back here anymore
        return start(hearts, inventory)
    else:
        print("What?")
        return camp(hearts, inventory)

def fieldw(hearts, inventory): #Calls the field west function if you go south and then west, this area will test you intuiton
    locked_areas["fieldw"] = True #locks the area afterwards
    visited_areas["field"] = True
    linput = input("You suddenly ran into a foggy section.\nDo you want to proceed Forward or go Back?: \n").title()
    if linput == "Forward":
        inventory.append("Poison")
        print("Consume the Poison or Die. Consume/Dont: \n") #You should consume the  not gonna lie
        linput2 = input().title()
        if linput2 == "Consume": 
            print("Good Job, you passed the test") #Nice
            hearts += 2 #You get more hearts, Yay
            return field(hearts, inventory)
        elif linput2 == "Dont":
            print("You failed the test.\nJoin the \033[31mFallen\033[0m and \033[31mUnworthy\033[0m down below.") #oopsie you weren't trusting enough
            if "savegame.txt" == True:
                os.remove("savegame.txt")
            print("\033[31mGame Over!\033[0m")
            time.sleep(5)
            sys.exit() #game over again
        else:
            print("Try a valid option?") 
            return fieldw(hearts, inventory)
    elif linput == "Back":
        print("You went back.") #you go back but you can't go back here
        return field(hearts, inventory)
    else:
        return fieldw(hearts, inventory)

def flower_field(hearts, inventory): #Random flower field generator with random colors
    rows = 10 #number of rows
    cols = 25 #number of columns (instead of using numpy)
    colors = ["\033[91m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
    reset_color = "\033[0m"
    for _ in range(rows):
        row = ""
        for _ in range(cols):
            flower_type = random.choice(["*", "o", "."]) #these are the characters that give you the flower field, different each time
            color = random.choice(colors)
            row += color + flower_type + reset_color + " "
        print(row)

def east_f(hearts, inventory): #You get rupees here to shop, simple
    locked_areas["east_f"] = True
    print("You've found some rupees!\n")
    inventory.append(f"100 Rupee") #String of rupees
    return field(hearts, inventory)

def field(hearts, inventory): #If you go south, you go here
    visited_areas["field"] = True #You've visited this 
    linput = input("You stumbled upon a vast open field, you can go any direction.\n\033[34mNorth\033[0m, \033[34mEast\033[0m, \033[34mWest\033[0m, \033[34mSouth\033[0m or Inventory:\n").title()
    if linput == "North":
        return start(hearts, inventory) # you just go back to where you were
    elif linput == "West":
        if locked_areas["fieldw"]:
            print("You don't want to go back there.") #Locked when you accessed beforehand
            return field(hearts, inventory)
        return fieldw(hearts, inventory) #calls function if unlocked
    elif linput == "East":
        if locked_areas["east_f"]: #Locked when you already took the rupees
            print("There's nothing here besides a looted box.")
            return field(hearts, inventory) #calls function to return
        return east_f(hearts, inventory) #calls the rupees function
    elif linput == "South":
        print("You discovered a flowerfield, take a moment to relax.") #Flowerfield
        flower_field(hearts, inventory)
        return field(hearts, inventory)
    elif linput == "Inventory":
        display_inventory(inventory)
        field(hearts, inventory)
    else:
        print("Valid input please?")
        return field(hearts, inventory)

def consume(hearts, inventory): #consume function for your consumables
    linput = input("Do you want to consume a consumable? Y/N: \n").upper()
    if linput == "Y":
        if not inventory:
            print("Your inventory doesn't have consumables.") #checks your inventory if you have food 
            return start(hearts, inventory)
        s = len(inventory) #Reads contents of the inventory to the user
        linput2 = input(f"What do you want to consume? {inventory}: ").title()
        if linput2 == "Apple" and "Apple" in inventory: #if you have apples from loot or shop you can eat
            hearts += 2
            inventory.remove("Apple")
        elif linput2 == "Meat" and "Meat" in inventory:
            hearts += 4 #if you have meat from bokoblin
            inventory.remove("Meat")
        elif linput2 == "Star Potion" and "Star Potion" in inventory: #if you have a star potion you can consume it
            hearts += 10 #so OP
            inventory.remove("Star Potion")
        elif linput2 == "Mysterious Potion" and "Mysterious Potion" in inventory: #This wills be a bit nauseating
            time.sleep(0.5)
            hearts -= 2 #you lose some hearts
            print(f"You just lost 2 hearts and you're now feeling unwell\nThis won't affect your performance.")
            inventory.remove("Mystious Potion")
        elif linput2 == "Blueberry Jam" and "Blueberry Jam" in inventory:
            hearts += 4 #Very Nice 
            inventory.remove("Blueberry Jam")
        elif linput2 == "Unknown Item": #THIS WILL KILL YOU IF YOU CONSUME IT 
            if "savegame.txt" == True:
                os.remove("savegame.txt")
            print("""\033[31m
                  %%@@@%%@@@@%%@@@%%                  
              %%@@#+=-:........:-=+#@@%%%             
           %%@%+..::-----------:::....=#%@%           
         %@@+:-----------------------:...=@@@         
       %@%=:---------------------------::..-%@%       
      %@*-:::::::::::::::::::::::::::::::::.:*@%      
     %%+::::::::::::::::::::::::::::::::::::::-%@%    
    %@+::::::::::::::::::::::::::::::::::::::::=@%    
   %@#::::::::::::::::::::::::::::::::::::::::::#@%   
   %@*::::::::::::::::::::::::::::::::::::::::::*@%   
   #@#:#::::::::::::::::::::::::::::::::::::::#-#@@   
  @@@@%@@*..................................+@@%@@@@  
 @@#:::::-*+..............................=#=:::::#@@ 
@@#.....::...............................::......::#@@
@@-....:%+*:...............................+**=...:=@@
@@@@#=....#@@*..........:=::=:..........+@@%....=#@@@@
    @@@#:.:@@@@%-.......-:...-:......:%@@@@+.:#@@@    
       @@#.*%@@@@@%:    .#:.#...  .#@@@@@%#.#@@@      
        @@%::+*@@@@@@@@@%=..-%@@@@@@@@@#=-:%@@        
       @@%-..  :%@@%#=+=..:.:.-+=*%@@@-...-+%@@       
      @@%.    .  ..     .%@@@..      ..  .:--%@@      
      @@@:       .    . +@@@@#.  ..       ..=@@@      
       @@@@*=-.-*@@@*+. .-..-:..+*@@%*-.-=*@@@@       
          @@@@@@@@@#:.       ..--=%@@@@@@@@@          
                @@@=%*+*=%**@=***@=@@@                
               @@%.....::.  .:-. ...#@@               
                @@@@@@+=+-..:+++%@@@@@                
                     @@@@@@@@@@@@                     \033[0m""")
            print("\033[31mGame Over! What did you think would happen?\033[0m")
            time.sleep(5)
            sys.exit() #WOMP WOMP, the art is from google and converted using a website
        else:
            print("That item is not in your inventory.")
            return consume(hearts, inventory)
    elif linput == "N":
        return start(hearts, inventory)
    else:
        return consume(hearts, inventory)
    return start(hearts, inventory) #brings you back to the start 

def shop(hearts, inventory): #you can shop here if you stole some rupees
    print("Trader: Hey boy! Welcome to my shop, if you have some rupees you can \033[33mBUY\033[0m something \033[32museful\033[0m from me.")
    while True:
        linput = input("Trader: Do you want to Buy something? (Buy/Leave): \n").title() #Trader asking you
        if linput == "Buy":
            print("Trader: You can choose between: Strength Potion (100 Rupee), Armor (100 Rupee), Apples (25 Rupee), Unknown Item (50 Rupee)")
            linput2 = input("What would you like to buy? \n").title()
            if linput2 == "Strength Potion":
                if "100 Rupee" in inventory: #A strength potion is quite op in the late game
                    inventory.remove("100 Rupee")
                    inventory.append("Strength Potion")
                    print("You bought a Strength Potion.")
                else:
                    print("You don't have enough rupees.")
                    shop(hearts, inventory)
            elif linput2 == "Armor": #this is fairly useful too
                if "100 Rupee" in inventory:
                    inventory.remove("100 Rupee")
                    inventory.append("Armor")
                    print("You bought Armor.")
                else:
                    print("You don't have enough rupees.")
                    shop(hearts, inventory)
            elif linput2 == "Apples":
                if "25 Rupee" in inventory or "50 Rupee" in inventory or "75 Rupee" in inventory or "100 Rupee" in inventory:
                    num_apples = input("How many apples would you like to buy? (1-4): ").strip()
                    if num_apples.isdigit() and 1 <= int(num_apples) <= 4:
                        num_apples = int(num_apples)
                        cost = num_apples * 25  # Each apple costs 25 Rupees
                        if "100 Rupee" in inventory and cost <= 100:
                            inventory.remove("100 Rupee")
                            inventory.extend(["Apple"] * num_apples) #.extend is used to add multiple elements to a list that can be modified
                            change = 100 - cost #change = what you'll be left with
                            if change > 0:
                                inventory.append(f"{change} Rupee")
                            print(f"You bought {num_apples} apple(s).")
                        elif "75 Rupee" in inventory and cost <= 75:
                            inventory.remove("75 Rupee")
                            inventory.extend(["Apple"] * num_apples)
                            change = 75 - cost
                            if change > 0:
                                inventory.append(f"{change} Rupee")
                            print(f"You bought {num_apples} apple(s).")
                        elif "50 Rupee" in inventory and cost <= 50:
                            inventory.remove("50 Rupee")
                            inventory.extend(["Apple"] * num_apples)
                            change = 50 - cost
                            if change > 0:
                                inventory.append(f"{change} Rupee")
                            print(f"You bought {num_apples} apple(s).")
                        elif "25 Rupee" in inventory and cost <= 25:
                            inventory.remove("25 Rupee")
                            inventory.extend(["Apple"] * num_apples)
                            change = 25 - cost
                            if change == 0:
                                inventory.remove(f"{change} Rupee") #All the statements here simply check if you have enough money for the number of apples you want to purchase else you can't buy it or it'll keep you in the shop until you leave
                            print(f"You bought {num_apples} apple(s).")
                        else:
                            print("You don't have enough rupees for that many apples.")
                    else:
                        print("Invalid input. Please select between 1 and 4 apples.")
                else:
                    print("You don't have enough rupees.")

            elif linput2 == "Unknown Item": #this is the mysterious item that will kill you
                if "50 Rupee" in inventory or "100 Rupee" in inventory:
                    if "100 Rupee" in inventory:
                        inventory.remove("100 Rupee")
                        inventory.append("50 Rupee")
                    else:
                        inventory.remove("50 Rupee")
                    inventory.append("Unknown Item")
                    print("You bought an Unknown Item.")
                else:
                    print("You don't have enough rupees.")
            else:
                print("That item is not available.")
        elif linput == "Leave":
            print("Trader: Come back anytime!")
            start(hearts, inventory)
        else:
            print("Trader: Give me a valid answer silly!")


def progress(visited_areas): #Progress tracker for some of the areas you've visited
    if visited_areas["start"]:
        print("You've visited the Beginning.")
    if visited_areas["dungeon"]:
        print("You've visited the Dungeon.")
    if visited_areas["dungeon_d"]:
        print("You've visited the Deep Dungeon.")
    if visited_areas["camp"]:
        print("You've visited the Camp before.")
    if visited_areas["cliff"]:
        print("You've visited the Cliff.")
    if visited_areas["field"]:
        print("You've visited the Field.")
    if visited_areas["fieldw"]:
        print("You've visited the Western Field.")
    if visited_areas["east_f"]:
        print("You've Looted the Box in the Eastern Field.")
    if visited_areas["chest"]:
        print("You've visited the Dungeon Chest.")
    if visited_areas["npc_bb"]:
        print("You've seen Shaney!")
    return None#calls back the main start function again


def start(hearts, inventory):#The main function start that handles all the commands from the beginning of the game
    visited_areas["start"] = True
    linput = input(
        "\033[0mWhere do you want to go?\n"
        "\033[34mNorth\033[0m, \033[33mEast\033[0m, \033[31mWest\033[0m, \033[36mSouth\033[0m?\n"
        "By the way, you can enter \033[32mShop\033[0m, \033[35mSave\033[0m/\033[35mLoad\033[0m/\033[35mDelete\033[0m/ "
        "and see your \033[32mHearts\033[0m and \033[32mInventory\033[0m.\n"
        "Also you can \033[36mEat\033[0m: \n"
        "And of course, see if you can become the \033[33mHero of Hyrule!\033[0m (Worthiness)\n"
        "\033[31mExit\033[0m or \033[31mProgress.\n\033[0m"
    ).title()

    if linput == "North":
        return dungeon(hearts, inventory) #Calls the dungeon
    elif linput == "East":
        return cliff(hearts, inventory) #calls the Cliff function
    elif linput == "West":
        if locked_areas["camp"] == True: #locks the area if already visited
            print("This area is off limits as more guardians have spawned")
            start(hearts, inventory) #
        return camp(hearts, inventory) #Calls the camp function if the area hasn't been visited yet
    elif linput == "South":
        return field(hearts, inventory) #Calls the field function
    elif linput == "Eat":
        return consume(hearts, inventory) #allows you to eat consumables
    elif linput == "Shop":
        return shop(hearts, inventory) #lets you shop at the trader for only a few items
    elif linput == "Hearts":
        print(hearts) #shows hearts
        start(hearts, inventory)
    elif linput == "Save":
        file("savegame.txt", 'save', hearts, inventory) #saves the game to a txt file
        print("Game Saved")
        return start(hearts, inventory)
    elif linput == "Load":
        loaded = file("savegame.txt", 'load') #loads game from txt file
        if loaded:
            hearts, inventory = loaded
            print("Game Loaded")
            return start(hearts, inventory)
        else:
            print("No save game found.")
            return start(hearts, inventory)
    elif linput == "Delete": #Deletes the file if it exists and if the user wants to
        if os.path.exists("savegame.txt"):
            confirm = input("Are you sure you want to delete the save file? (yes/no): ").lower()
            if confirm == "yes":
                os.remove("savegame.txt")
                print("Save file deleted.")
                hearts = 4 #resets to beginning
                inventory = []
                for key in visited_areas:
                    visited_areas[key] = False
                for key in locked_areas:
                    locked_areas[key] = False #resets all areas that have been visited and locked back to false to start again
                print("Game reset to beginning state.")
            elif confirm == "no": #cancels the deletion
                print("Save file deletion cancelled.")
            else:
                print("Invalid confirmation. Save file not deleted.")
        else:
            print("No save file to delete.")
        return start(hearts, inventory)
    elif linput == "Inventory": #prints the inventory
        display_inventory(inventory)
        return start(hearts, inventory)
    elif linput == "Worthiness": #will test your worthiness
        can_begin_final_fight(hearts, inventory)
        return start(hearts, inventory)
    elif linput == "Progress":
        progress(visited_areas) #Will show the areas you've visited
        return start(hearts, inventory)
    elif linput == "Exit":
        sys.exit() #Kills the game
    else:
        print("Enter a valid input")
        return start(hearts, inventory)

hearts = 4 #initial Hearts amount, need 16 or more to get master sword
inventory = [] #initial inventory with nothing in it
visited_areas = {
    "start": False,
    "dungeon": False,
    "dungeon_d": False,
    "cliff": False,
    "camp": False,
    "field": False,
    "fieldw": False,
    "east_f": False,
    "chest":False,
    "npc_bb":False, 
} #areas to visit, will turn to true if visited


locked_areas = {
    "camp": False,
    "dungeon_right": False,
    "dungeon_forward_elixir": False, 
    "cliff_north_elixir": False, 
    "trap_s":False,
    "npc_bb":False,
    "camphos":False,
    "fieldw":False,
    "east_f":False,
} #also areas to visit but cannot be accessed again if visited

if __name__ == "__main__": #checks the script if it's being run as the main program 
    start(hearts, inventory) #main program