import random
import time

t1 = time.time()
input_num = int(input("enter your guess_number : "))
winning_num = random.randint(1,2)
guess = 1
game_over = False

while not game_over :
    if input_num == winning_num :
        print(f"congratulation you are win! and your guess is : {guess}")
        game_over = True

    else :
        if input_num > winning_num :
            print("enter to low!")
            input_num = int(input("enter again your guess number : "))
            guess += 1

        else :
            print("enter to high!")
            input_num = int(input("enter again your guess number : "))
            guess += 1 
t2 = time.time()
print(f"time cost : {t2-t1}!")