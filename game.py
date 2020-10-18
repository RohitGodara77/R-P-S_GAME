import random

# used 'random' module to give computer liberty to choose randomly a number between 1,2 and 3:
# with the help of the function 'randint(num1,num2)'
n = random.randint(1,3)
if n == 1:
    comp='r'                  # Here,we simply initialized variable comp with 
elif n == 2:                  # 'r' , 'p' or 's' according to randomly chosen number
    comp='p'
else:
    comp='s'

you = input("player's turn! enter 'r' for rock, 'p' for paper,'s' for scissors : ")

#logic of the game

def game(comp,you):

    if you == comp:
        return None      

    # checking possible outcomes when comp chose 'r'           # 'None' is a data type in python repesenting nothing/Null/void
    elif comp == 'r':                                        
        if you == 'p':                                         
            return True
        else:
            return False
    # checking possible outcomes when comp chose 'p' 
    elif comp == 'p':
        if you == 's':
            return True
        else:
            return False
    # checking possible outcomes when comp chose 's' 
    else:
        if you == 'r':
            return True
        else:
            return False

print(f'\nplayer chose :{you}\ncomputer chose :{comp}\n')
game_result = game(comp,you)                # 'game_result' variable used to store result of the game 

if game_result == None:
    print("oh! it's a tie\n")
elif game_result:
    print("congrats! you win\n")
else:
    print("sorry! you lost\n")
