def pokemon_binder_manager():
    pokemon_binder = {}
    max_pokedex = 1025
    cards_per_page = 64
    rows = 8
    columns = 8
    score = 0
    def get_card_position(pokedex_number):
        "Given a pokedex_number, calculate its page, row, and column."
        
        "Page numbering starts at 1."
        "Card positions are filled left-to-right, top-to-bottom."
        index = pokedex_number - 1  # zero-based index
        page = index // cards_per_page + 1
        position_in_page = index % cards_per_page
        row = position_in_page // rows
        col = position_in_page % columns
        return page, row, col
    def add_card():
    
        pokedex = int(input("Enter Pokedex Number (1-1025): "))
        if not (1 <= pokedex <= max_pokedex):
            print("Invalid Pokedex number! Must be between 1 and 1025.\n")
            return
        
        if pokedex in pokemon_binder:
            page, row, col = pokemon_binder[pokedex]
            print(f"Card already in binder - Page: {page}, Row: {row}, Column: {col}, Status: Pre-existing\n")
        else:
            page, row, col = get_card_position(pokedex)
            pokemon_binder[pokedex] = (page, row, col)
            print(f"Page: {page}\nPosition: Row {row+1}, Column {col+1}\n Status: Added Pokedex #{pokedex} to binder\n")


    #reset function
    def reset():
        print("WARNING: you want to delete all the cards?")
        choice = input("Type 'confirm' to reset or 'exit' to return to Main Menu: ").lower().strip()
        if choice == "confirm":
            nonlocal pokemon_binder
            pokemon_binder.clear()
            print("The binder reset was successfull! All cards have been removed.\n")
        elif choice == "exit":
            print("Returning to main menu...\n")
            print("Welcome to Pokemon Card Binder Manager!\n")
            print("Main Menu:")
            print("1. Add a Pokemon Card")
            print("2. Reset Binder ")
            print("3. View Binder Placements")
            print("4. Exit \n")
        else:
            print("Invalid choice.\n")

    def status():
        print(f"Current Binder Contents: \n{"-"*20}\n")
        count = len(pokemon_binder)
        if count!=0:
            for i in pokemon_binder:
                print(f"Pokedex #{i}\n    Page: {pokemon_binder[i][0]}\n    Position: Row {pokemon_binder[i][1]}, Column {pokemon_binder[i][2]}\n")
            print("-"*20)

        else: print("The binder is empty.")

        completion = (count / max_pokedex) * 100
        print(f"Total Cards in Binder: {count}")
        print(f"% Completion: {completion:.2f}%")
        if count == max_pokedex:
            print("You have Caught them all!!")
        print("")
        nonlocal score
        pokeScore= completion

    def exit():
        print("Thank you for using Pokemon Card Binder Manager!")
    
        # exit()
    # --- Main Menu Loop ---
    print("Welcome to Pokemon Card Binder Manager!\n")
    print("Main Menu:")
    print("1. Add a Pokemon Card")
    print("2. Reset Binder ")
    print("3. View Binder Placements")
    print("4. Exit \n")
    while True:
        
        mode = int(input("Select option (1-4): "))

        if mode == 1:
            add_card()
            
        elif mode == 2:
            reset()
        elif mode == 3:
            status()
        elif mode == 4:
            exit()
            break
        else:
            print("Invalid mode selected. Please choose 1-4.\n")
pokemon_binder_manager()


