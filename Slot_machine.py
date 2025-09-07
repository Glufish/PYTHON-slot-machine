#Slot machine system
#6 symbol:"cherry",  "lemon","watermelon", "grape", "apple","lucky7"
#both lucky7 = 500, both same fruits = 200, 2 same fruits = 70, both different = -50
import random


#section list
#tool --> function --> ui --> main


#-----------------------tool section------------------------

#1.generate a random number variable
def randomise_system( reel1, reel2, reel3 ) :
    reel1, reel2 , reel3 = random.randint ( 1 , 6 ) #random number between 1 to 6 for each reel
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

    return reel1, reel2, reel3 #return 3 reels by syumbol
    
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

#-----------------------ui section------------------------

#main menu ui
def main_menu():
    print


     

#----------------------main function-----------------------
#have to put the token number outside the loop to prevent reset 
token = 1000
while True: #only when user exit then the application ended( with break )
    main_menu() #show to main menu(waiting shrimpy)

    reel1 , reel2 , reel3 = 0 #initialise the both reel
    reel1 , reel2 , reel3 = randomise_system( reel1, reel2, reel3 ) #tool 1, randomise both reel number

    result = 0 #initialise the result amount
    result = check_result( result, reel1, reel2, reel3) #function 1, to get the result by the reel number

    token = update_token( token, result )

    














