#Slot machine system
#6 symbol:"cherry",  "lemon","watermelon", "grape", "apple","lucky7"
#both lucky7 = 500, both same fruits = 200, 2 same fruits = 70, both different = -50
import random


#section list
#tool --> function --> ui --> main


#-----------------------tool section------------------------

#1.generate a random number variable
def randomise_system( reel1, reel2, reel3 ) :
    reel1 = random.randint ( 1 , 6 ) #random number between 1 to 6 for each reel
    reel2 = random.randint ( 1 , 6 )
    reel3 = random.randint ( 1 , 6 )
    return reel1, reel2 , reel3 #return 3 reels by number

#2.covert number to the responding symbol
def number_to_symbol( reel1, reel2, reel3 ) :
    #The way to use rule = { condition : result }
    SymCovert = {   
         1 : "cherry",  
         2 : "lemon",
         3 : "watermelon",
         4 : "grape",
         5 : "apple",
         6 : "lucky7",
        }

    #covert each num to the symbol 
    reel1 = SymCovert.get ( reel1 ) 
    reel2 = SymCovert.get ( reel2 )
    reel3 = SymCovert.get ( reel3 )

    return reel1, reel2, reel3 #return 3 reels by symbol
    
#3. update amount of the token
def update_token( token, result ) :
    token = token + result 
    return token 



#----------------------function---------------------------

#check result
def check_result( result, reel1, reel2, reel3) :
    #Jackpot 7
    if reel1 == reel2 == reel3 == 6 :
        result = 500

    #3 same fruits
    elif reel1 == reel2 == reel3 :
        result = 200

    #2 same fruits
    elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3 :
        result = 70

    #both different
    else :
        result = -50

    return result

#Main menu ui
def main_menu( token,result ,reel1 , reel2 , reel3, r1 , r2 , r3 ):
        
    reel1 , reel2 , reel3 = randomise_system( reel1, reel2, reel3 ) #tool 1, randomise both reel number
    r1 , r2 , r3 = number_to_symbol( reel1, reel2, reel3 ) #tool 2, covert reel number to the symbol

    
    main_menu_ui ()
        
    choice = input("Choose number to enter (1-5): ")
        
    if choice == '1':
        rule_book() #ui 2
        input()
        return token,False
        

    elif choice == '2':
        print("Your balance is ", token , " token." )
        print("Press anything to return.")
        input()
        #balance will be viewed
        return token,False

    elif choice == '3':
        token - 50 #entry fees
        result = check_result( result, reel1, reel2, reel3) #function 1, to get the result by the reel number
        token = update_token( token, result )
        after_roll( r1,r2,r3,result,token )
        print("Press anything to return.")
        input()
        return token,False
        #game will be started

    elif choice == '4':
        token = 1000
        print("Press anything to return.")
        input()
        return token,False
        #game will be reset

    elif choice == '5':
        input("Are you sure to quit?(y to quit):")
        if input == "y":
            return token,True

        else :
           return token,False

     
    
# ----------------------- ui section -------------------------

#1. mainmenu ui
def main_menu_ui ():
    print("\n--- Main Menu ---")
    print("1. Check The Rulebook :3")
    print("2. Check your Balance >w<")
    print("3. Start Betting >o<")
    print("4. Reset the Game 0~0")
    print("5. Exit the Game TwT")

    return

#2. rulebook ui
def rule_book () :
    print("rule are here:")
    print("Each entry fees: 50 tokens")
    print ("If you get 3 Jackpot 7, you will earn 500 tokens,")
    print ("If you get 3 of the same fruits, you will earn 200 tokens,")
    print ("If you get 2 of the same fruits, you will earn 70 tokens,")
    print ("Or else, you got nothing.")
    print("Press anything to return.")
    
    return

#3. game done result ui
def after_roll ( r1, r2, r3 ,result,token ) :
    print("result: " ,r1 ,",", r2, "," , r3)
    print("You had won", result )
    print("Your total token right now:", token )

    return result

#4.end ui
def end( token ) :
    print("Thanks for playing, your final earn:", token - 1000 , " tokens") #1000 is initialise tokens amount
    print("Total tokens:",token)

    return

#----------------------main function-----------------------

#have to put the token number outside the loop to prevent reset 
token = 1000 #initialise the token number

#initialise the both reel
reel1 = 0 
reel2 = 0 
reel3 = 0 
    
#show the symbol result to the user    
r1 = "" 
r2 = "" 
r3 = "" 

#initialise the result amount   
result = 0 

while True:
    endCode = False
    #show to main menu
    token ,endCode = main_menu( token,result,reel1 , reel2 , reel3,r1 , r2 , r3 )

    if endCode == True:
        break


end( token )
    
#application ended









