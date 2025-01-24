from db import add_to_database, display_all_current_information, update_information, delete_information, generate_password,check_if_account_name_already_exits,keyboard_restart
import os 
from time import sleep
import keyboard
from typing import Any

    
print("Welcome To cli password manager")

global running
running:bool = True

def restart_program() -> None:
    global running
    print("Programm is restarting")
    sleep(3)
    os.system("color 7")
    os.system("cls")
    running = False # once the loop ends here the programm restart the programm 
    keyboard.write("python main.py")
    keyboard.press_and_release('enter')

@lambda _: _()
def main() -> None:
    running:bool = True

    while running:
        # explain later
        display_counter = 0 
        #os.system("cls")
        message = """
    what do you want to do today

    [a]dd password
    [s]how all passwords
    [u]pdate a password or an information 
    [d]elete a password (deleting a password delete's it account_name and user_name)
    [g]enerate a password
    [r]estart the program
    [c]lear the screen
    [q]uit
    """
        print(message)
        user_input:str = input("> ").lower().strip()

        try:

            if user_input == "a" or user_input == "add":
                print("Would you like to generate a password y/n")
                _input:str = input("> ").lower().strip()

                match _input:
                    case 'y':
                        os.system("color 7")
                        try:
                            print("The len of the password")
                            pass_len:int = int(input("> ")) or 6
                            return_password:str = generate_password(password_lenght=pass_len)
                            acct_name:str = input("Enter account name: ")
                            user_name:str = input("Enter username: ")
                            result:int = check_if_account_name_already_exits(account_name=acct_name)

                            if result == -1:
                                print("{} alr exits programm will restart \n".format(acct_name))
                                restart_program()
                            
                            else:
                                c = add_to_database(account_name=acct_name, user_name=user_name, password=return_password)
                                if c == 0:
                                    print("information added succesfully")
                                    sleep(2) # give the user enough time to see that the information as been added 
                                    os.system("cls")
                                    os.system("color 7")
                        except ValueError:restart_program()
                    case 'n':
                        os.system("color 7")
                        acct_name:str = input("Enter account name: ")
                        user_name:str = input("Enter username: ")
                        password:str = input("Enter password: ")

                        result = check_if_account_name_already_exits(account_name=acct_name)

                        if result == -1:
                            print("{} alr exits programm will restart".format(acct_name))
                            restart_program()
                            
                        else:
                            c = add_to_database(account_name=acct_name, user_name=user_name, password=password)
                            if c == 0:
                                print("information added succesfully")
                                sleep(2) # give the user enough time to see that the information as been added 
                                os.system("cls")
                                os.system("color 7")
                    case _:print("Some is wrong press r to restart")

            elif user_input == "s" or user_input == "show" or user_input == "sa":
                match user_input:
                    case "s":
                        os.system("color 7")
                        os.system("cls")
                        print("getting information from database ...\n")
                        sleep(1)
                        result = display_all_current_information()
                        for i, information in enumerate(result, start=1):
                            print(f"{i}: {information}") # later (create a way for user to view everything in a .txt or something)
                        display_counter = -~ display_counter # is the same as display_counter += 1

            elif user_input == "u" or user_input == "update":
                os.system("cls")
                os.system("color 7")
                if display_counter == 0:
                    print("getting information from database ...")
                    sleep(1)
                    result = display_all_current_information()
                    for i, information in enumerate(result, start=1):print(f"{i}: {information}")
                else:continue

                print("Enter the details of the information you want to change")
                old_acct:str = input("Enter the account name you want to change: ") or ""
                acct_name:str = input("Enter account name: ") or ""
                user_name:str = input("Enter new_username: ") or ""
                password:str = input("Enter new_password: ") or ""

                c = update_information(old_account_name=old_acct, new_account_name=acct_name, new_username=user_name, new_password=password)

                if result == -1:print("Some error occur restart the program")
                else:
                    os.system("cls")
                    os.system("color 7")
                    print("Your information has been succesfully updated\n")
                    print("Displaying updated information")
                    sleep(2)
                    result  = display_all_current_information()
                    for i, information in enumerate(result, start=1):print(f"{i}: {information}")



            elif user_input == "d" or user_input == "delete":
                """
                    deleting a account name with duplicate deletes both of them
                    (To fix this problem every account_name must be unique(every account_name must occur only once)) ==> (Task has been done)
                """
                os.system("cls")
                os.system("color 7")
                result  = display_all_current_information()
                for i, information in enumerate(result, start=1):print(f"{i}: {information}")

                account_name:str = input("\nEnter the account name you want to delete: ")

                result = delete_information(account_name=account_name)

                if result == 0:print(f"{account_name} has been succesfully deleted")
                else: print("some type of error restart")


            elif user_input == "g" or user_input == "generate":
                print("Would you like to add an account name y/n")
                _user:str = input("> ").lower().strip()

                match _user:
                    case 'y':
                        acct_name:str = input("Enter account name: ")
                        user_name:str = input("Enter username: ")
                        result = check_if_account_name_already_exits(account_name=acct_name)
                        if result == -1:
                            print("{} alr exits programm will restart \n".format(acct_name))
                            restart_program()
                        else:
                            pass_len:int = int(input("Enter the len of the generated password: ")) or 6
                            _generated_password:str = generate_password(password_lenght=pass_len)
                            c = add_to_database(account_name=acct_name, user_name=user_name, password=_generated_password)
                            if c == 0:
                                print("information added succesfully")
                                sleep(2) # give the user enough time to see that the information as been added 
                                os.system("cls")
                                os.system("color 7")
                    case 'n':
                        os.system("cls")
                        os.system("color 7")
                        pass_len:int = int(input("Enter the len of the generated password: ")) or 6
                        _generated_password:str = generate_password(password_lenght=pass_len)
                        print("generated password: {}".format(_generated_password))
                    case _:print("Something happend restart the program")


            elif user_input == "q" or user_input == "quit":
                print("Good bye hope to see you soon")
                sleep(2)
                # when the user quits the color goes back to white
                os.system("color 7")
                os.system("cls")
                running = False

            elif user_input == "r" or user_input == "restart":restart_program()

            elif user_input == "c": 
                os.system("cls")
                os.system("color 7")
            else:
                import random
                random_number = random.randint(1, 9)
                # every time the user enter's wrong input change the color of text using os         
                os.system(f"color {random_number}")
                os.system("cls")
                print("\nwrong input")

        except KeyboardInterrupt:
            quit()