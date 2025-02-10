#Word scramble
import random

words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium'] #Taking word list
 
computer_Random_list = random.choice(words) # get some random  elements from given list

while True:
    user_guess_list = input() # userinput for guess list element
    if user_guess_list == computer_Random_list: # compare both elements
        print("correct, congratulation")
        break                               # break the loop, the given word is found
    else:
        print("incorrect, Try again")
