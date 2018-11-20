'''
 rock paper scissor ;)
 the input should be a number 1 : paper 2 : scissors 3 : rock
 to exit enter any string
'''
import random
cases = {1 : "paper",2 : "scissor",3 : "rock"}
print("ENTER any string to exit")
try :
    while True:
        print(" your turn ")
        print("1 : paper 2 : scissors 3 : rock")
        first = int(input())
        if first in [1,2,3]:
            second = random.randint(1, 3)  # generating random integer
            second_val = cases[second]  # its value any (rock ,paper,scissors)
            first_val = cases[first]  # its value any (rock ,paper,scissors)
            print("---------------------------------------------------------------------------------------------------------------------------")
            print('______________________',first_val.upper(), " VS ", second_val.upper(),'______________________')
            if(first > second):
                if(first == 3 and second == 1 ):
                    print("______________________ YOU LOST :( ______________________")
                else:
                    print("______________________ YOU WON :) ______________________")
            elif first < second :
                if (first == 1 and second == 3):
                    print("______________________ YOU WON :) ______________________")
                else:
                    print("______________________ YOU LOST :( ______________________")
            else:
                print("______________________ ITS A DRAW :0 ______________________")

        else:
            print("______________________ enter valid input :/ ______________________")
except ValueError:
    print("THANK YOU FOR JOINING US :)")

