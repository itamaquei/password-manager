import sqlite3
from random import choice
import keyboard
from typing import Any

type Anything = Any
def add_to_database(account_name:str=None, user_name:str=None, password:str=None) -> int | Anything:
    try:
        # connect allows you to connect to the database
        con = sqlite3.connect("userdata.db")

        # allows you to write sql commands
        cursor = con.cursor()

        # create table if it does not exits
        cursor.execute("CREATE TABLE IF NOT EXISTS user_data(account_name TEXT, user_name TEXT, password TEXT)")
        data = [(account_name, user_name, password)]
        # add user info to db
        cursor.executemany("INSERT INTO user_data VALUES(?, ?, ?)", data)

        # make sure changes have been commited after every Insert
        con.commit()
    except sqlite3.Error as e:print("An error occurred: {}".format(e))
    else: return 0 # got the idea from C retun 0 means the function run with no error
    finally: con.close() # close the connection to the database

def check_if_account_name_already_exits(account_name:str) -> int | Anything:
    try:
        con = sqlite3.connect("userdata.db")
        cursor = con.cursor()

        cursor.execute("SELECT * FROM user_data WHERE account_name=?", (account_name,))
        result = cursor.fetchone()

        if result:
            return -1 # if -1 is return than the account name alr exits 
        else:
            return 0 # 0 is return when the account does not exits
        
    except sqlite3.Error as e: print("Some error occur: {}".format(e))
    finally: con.close()

def display_all_current_information() -> Anything:
    try:
        con = sqlite3.connect("userdata.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM user_data")
        records = cursor.fetchall() # fetchall allows you to get every thing from the db
        return records
    
    except sqlite3.Error as e: print("An Error occurred: {}".format(e))
    finally: con.close() # always remeber to close the connection to database after you done


def update_information(old_account_name:str,new_account_name:str=None, new_username:str=None, new_password:str=None) -> int | Anything:
    try:
        con = sqlite3.connect("userdata.db")
        cursor = con.cursor()

        # use the user old account name
        cursor.execute("SELECT * FROM user_data WHERE account_name=?", (old_account_name,))
        record = cursor.fetchone() # to check if there is data in the db is not return -1

        if not record:
            return -1
        
        #unpack the exitsing values from db
        current_account_name, current_username, current_password = record

        final_username = new_username if new_username is not None else current_username
        final_password = new_password if new_password is not None else current_password
        final_acct_name = new_account_name if new_account_name is not None else current_account_name
        
        cursor.execute("UPDATE user_data SET account_name=?, user_name=?, password=? WHERE account_name=?", (final_acct_name, final_username, final_password, old_account_name))

        con.commit()
        return 0
    except sqlite3.Error as e: print("An Error occurred:{}".format(e))
    finally: con.close()

# the delete function dont work fix it (The function has been fixed) 
def delete_information(account_name) -> int | Anything:
    try:
        con = sqlite3.connect("userdata.db")
        cursor = con.cursor()

        # chceck if there is any record in the database
        cursor.execute("SELECT * FROM user_data WHERE account_name=?", (account_name,))
        record = cursor.fetchone()
        if not record:
            return -1

        # always commit after using INSERT, DELETE, and UPDATE
        cursor.execute("DELETE FROM user_data WHERE account_name=?", (account_name,))
        con.commit()
        return 0

    except sqlite3.Error as e: print(f"An error occur: {e}")
    finally:con.close()

def generate_password(password_lenght:int=6) -> str | Anything:
    alphabeth:list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q","s", "t", "u", "v", "w", "x", "y", "z"]
    
    symbols:list[str] = ["!", "@", "#", "$", "%", "^", "&", "*", "?"]
    numbers:list[int] = [str(num) for num in range(10)]

    password:list[str] = []
    # check to make sure password len is valid
    if password_lenght <= 4:
        return -1
    
    password.append(choice(alphabeth))
    password.append(choice(symbols))
    password.append(choice(numbers))
    password.append(choice(alphabeth).upper())

    while len(password) < password_lenght:
        password.append(choice(alphabeth + symbols + numbers))
    
    random_password = "".join(password)
    return random_password


def keyboard_restart() -> None:
    keyboard.write("python data.py")
    keyboard.press_and_release('enter')
