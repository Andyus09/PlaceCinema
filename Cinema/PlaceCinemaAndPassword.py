
ticket_minor = 8
ticket_major = 16
popcorn_price = 5

def wallet_balance():
    global wallet
    
    wallet = int(input("Wallet: "))
    print(f"Balance: {wallet} €.")


def charge_wallet():
    # account
    global new_wallet
    
    wallet_balance()
    
    wallet_verification = ("Purchase is possible", "Purchase is not possible")[wallet <= ticket_major + popcorn_price]
    print(wallet_verification)
    print(f"You have {wallet} € in your wallet.")
    
    if wallet < 21:
        wallet_question1 = input("Do you want to charge the wallet ? (Yes/No) ").capitalize()
        if wallet_question1 == "Yes":
            print(f"You must complete minimum {(ticket_major + popcorn_price) - wallet} €.")
            print("How much do you want to put in the card ? ")
            new_wallet = int(input())
            new_wallet = wallet + new_wallet
            print(f"The Card was credited.\nYour new account is: {new_wallet} €.\nBalance: {new_wallet} €.")
            while new_wallet < ticket_major + popcorn_price:
                print("Purchase is not possible !\n"
                      f"Please charge the wallet.\nYou must complete minimum {(ticket_major + popcorn_price) - new_wallet} €.")
                new_wallet1 = int(input())
                new_wallet = new_wallet + new_wallet1
                print(f"You have now {new_wallet} € in your wallet.")
        else:
            new_wallet = wallet
            print(f"You have {new_wallet} € in your wallet.\nPlease charge your wallet !\nBalance: {new_wallet} €.")
            charge_wallet()
        
        # Enter the password in system:
        password = input("Choose your password: ")
        password_lenght = len(password)

        # Check if the password is less than 8 characters:
        if password_lenght <= 8:
            print("Password too short !")
        elif 8 < password_lenght <= 12:
            print("Average password !")
        else:
            print("Perfect password !")
        print(password_lenght)
    
    else:
        new_wallet = wallet


def cinema():
    
    charge_wallet()
    
    global account
    # Cinema ticket
    ticket_old = ticket_major - (ticket_major * 10 / 100)   # 10% reduction for old man/woman

    name = input("What's your name ? ")
    film = input("What movie do you want to see ? ")
    age = int(input("How old are you ? "))

    # It's checking if the age is between 0 and 18
    if 0 < age < 18:
        print(f"You are young.\nThe ticket costs you {ticket_minor} €.")
        choice_popcorn = input("Do you want some popcorn ? (Yes/No) ").capitalize()
        if choice_popcorn == "Yes":
            bill = ticket_minor + popcorn_price
            print(f"Name: {name}\nFilm: {film}\nYour bill is {bill} €.")
            account = new_wallet - bill
            print(f"New account: {account} €.")
        else:
            print(f"Name: {name}\nFilm: {film}\nYour bill is {ticket_minor} €.")
            account = new_wallet - ticket_minor
            print(f"New account: {account} €.")
            
        bill_created = input("Is it fertig ? (Yes/No) ").capitalize()
        if bill_created == "Yes":
            print("--------------New client--------------")
        else:
            print("You have to start data entry again ! ")
        print(60 * "-")
        return cinema()

    # It's checking if the age is between 18 and 200.
    elif 18 <= age <= 200:
        if age < 65:
            print(f"Name: {name}\nFilm: {film}\nYou are major and young. The ticket costs you  {ticket_major} €.")
            account = new_wallet - ticket_major
            print(f"New account: {account} €.")
        elif 65 >= age <= 200:
            print(f"Name: {name}\nFilm: {film}"
                  f"\nYou are major and old. As advantage you have 10% reduction for the ticket and popcorn."
                  f" The ticket costs you  {ticket_old} €.")
            account = new_wallet - ticket_old
            print(f"New account: {account} €.")

        choice_popcorn = input("Do you want some popcorn ? (Yes/No) ").capitalize()
        if choice_popcorn == "Yes":
            bill = (ticket_major + popcorn_price,
                    (ticket_major + popcorn_price)-((ticket_major + popcorn_price) * 10 / 100))[age >= 65]
            print(f"Name: {name}\nFilm: {film}\nYour bill is {bill} €.")
            account = new_wallet - bill
            print(f"New account: {account} €.")
        else:
            ticket = (ticket_major, ticket_old)[age >= 65]
            print(f"Name: {name}\nFilm: {film}\nYour bill is {ticket} €.")
            account = new_wallet - ticket
            print(f"New account: {account} €.")
        
        bill_created = input("Is it fertig ? (Yes/No) ").capitalize()
        if bill_created == "Yes":
            print("--------------New client--------------")
        else:
            print("You have to start data entry again ! ")
            print(60 * "-")
        return cinema()
        

    else:
        print("Enter a real age !")
        return cinema()


cinema()
