import random
while True:
    print("Menu:")
    print("1. Guess Number Game")
    print("2. Rock Paper Scisors Game ")
    select = input('Select Any Game : ')
    if select== "1":
        
        def guess_number_game():
            comp = random.randint(1,100)
            print(f"Welcome to guess number game.")
            print(f"guess a number from 1 to 100")
            
            while True :
                
                user_input = int(input("Enter your guess: "))
                if user_input < comp :
                    print("guess higher ")
                elif user_input > comp :
                    print("guess lower ")
                else:
                    print("congratulations!! you won ")
                    choice = input("do you want to continue(y/n): ")
                    if choice== "n": break
        guess_number_game()
    else:
        
        def rock_paper_scissor():
            choices = ["rock", "paper", "scissor"]
            print("wlecome to rock, paper,scissor game.")
            
            while True:
                user_input = input("Enter rock, paper, scissor: ")
                comp_choice = random.choice(choices)
                print(f"computer chose:{comp_choice}")
                
            
                if user_input == comp_choice:
                    print("its a draw")
                elif (user_input == "rock" and comp_choice == "scissor") or \
                    (user_input == "paper" and comp_choice == "rock") or \
                    (user_input == "scissor" and comp_choice == "paper"):
                    print("congratulations!! you won")       
                else :
                    print("you lost")

                
                choose=input('Do You Want to play again? y/n : ')
                if choose=='n': break
    
                    
            

        rock_paper_scissor() 
