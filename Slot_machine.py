#To randomise the number
import random


#section list
#tool --> function --> ui --> main


#-----------------------tool section------------------------

#1.generate a random number variable
def randomise_system( number ) :
    number = random.randint ( 1 , 3 )
    return number

    
    
#----------------------function---------------------------

#game rule
def game_rule() :
    rules = {

        }

#-----------------------ui section------------------------

#main menu ui
def main_menu ( ) :
    print("Guess the number:3")
    print("Made by Fishyyy gluuu")
    

     

#----------------------main function-----------------------

number = 0 #random number
inputNumber = 0 #to let user input
counter = 0 #to count the attempt of guess
fishBool = False #bool to fix the bug wuwuwu
main_menu() #ui 1
while True:
        
        number = randomise_system( number ) #tool 1
        inputNumber = number_range( inputNumber ) #tool 3     
        fishBool, counter = compare_number( inputNumber, number, counter ) #tool 2
        if fishBool :
            break

#application ended







