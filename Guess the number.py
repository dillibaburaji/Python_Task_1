#Guess the number
import random

computer_Random_num = random.randint(1, 10) #computer getting some random input from 1 to 10

while True:    #Allow multiple guesses untill the correct number is found
    
    user_guess_num = int(input()) #user guess random number (user input)
     
    if user_guess_num < computer_Random_num: #checking the user number, wethere the user input is low or not
        print("To low,try again")
    elif user_guess_num > computer_Random_num: #checking the user number, wethere the user input is  high or not
        print("To high,try again")
    else:
        print("correct answer, Congratulation") #checking the user number, is correct or not
        break
