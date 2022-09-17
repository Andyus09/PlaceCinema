# It's a function that I created.
def cinema():
    # Account
    wallet = 500
    computer_price = 50000
    global Account
    # Cinema ticket
    ticket_minor = 8
    ticket_major = 16
    ticket_old = ticket_major - (ticket_major * 10 / 100)   # 10% reduction for old man/woman
    popcorn_price = 5

    text = ("Purchase is possible", "Purchase is not possible")[computer_price <= 1000]
    print(text)
    print(f"You have {wallet} € in your wallet.")

    # Password verification system:
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
            Account = wallet - bill
            print(f"New Account: {Account} €.")
        else:
            print(f"Name: {name}\nFilm: {film}\nYour bill is {ticket_minor} €.")
            Account = wallet - ticket_minor
            print(f"New Account: {Account} €.")
            
        choice_client = input("Is it a new client ? (Yes/No) ").capitalize()
        if choice_client == "Yes":
            print("--------------New client--------------")
        else:
            print("You have to start data entry again ! ")
        return cinema()
        print(20 * "-")
        return cinema()

    # It's checking if the age is between 18 and 200.
    elif 18 <= age <= 200:
        if age < 65:
            print(f"Name: {name}\nFilm: {film}\nYou are major and young. The ticket costs you  {ticket_major} €.")
            Account = wallet - ticket_major
            print(f"New Account: {Account} €.")
        elif 65 >= age <= 200:
            print(f"Name: {name}\nFilm: {film}"
                  f"\nYou are major and old. As advantage you have 10% reduction for the ticket and popcorn."
                  f" The ticket costs you  {ticket_old} €.")
            Account = wallet - ticket_old
            print(f"New Account: {Account} €.")

        choice_popcorn = input("Do you want some popcorn ? (Yes/No) ").capitalize()
        if choice_popcorn == "Yes":
            bill = (ticket_major + popcorn_price,
                    (ticket_major + popcorn_price)-((ticket_major + popcorn_price) * 10 / 100))[age >= 65]
            print(f"Name: {name}\nFilm: {film}\nYour bill is {bill} €.")
            Account = wallet - bill
            print(f"New Account: {Account} €.")
        else:
            ticket = (ticket_major, ticket_old)[age >= 65]
            print(f"Name: {name}\nFilm: {film}\nYour bill is {ticket} €.")
            Account = wallet - ticket
            print(f"New Account: {Account} €.")
        
        choice_client = input("Is it a new client ? (Yes/No) ").capitalize()
        if choice_client == "Yes":
            print("--------------New client--------------")
        else:
            print("You have to start data entry again ! ")
        return cinema()
        print(20 * "-")

    else:
        print("Enter a real age !")
        return cinema()


cinema()

