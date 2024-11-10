import bcrypt
import connect

"""
This file contains the functions to register a user with their provided password by hashing it and storing it in the
database. It also contains the function to authenticate a user by comparing the hashed password in the database with the
hashed password provided by the user.
"""

def register_user(username, password, firstName, lastName):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    salt_str = salt.decode('utf-8')
    hashed_password_str = hashed_password.decode('utf-8')

    query_string = (f"INSERT INTO Students VALUES('{username}',"
                    + (f" '{firstName}'," if firstName else " NULL,")
                    + (f" '{lastName}'," if lastName else " NULL,")
                    + f" 'Science', 'Computer Science', '{hashed_password_str}', '{salt_str}')")

    connect.query(query_string)

def authenticate_user(username, password):
    query_string = f"SELECT salt, hashedPassword FROM Students WHERE username = '{username}'"
    results = connect.query(query_string)

    if len(results) == 0:
        return False

    salt = results[0][0].encode('utf-8')
    hashed_password = results[0][1].encode('utf-8')

    if bcrypt.hashpw(password.encode('utf-8'), salt) == hashed_password:
        return True
    else:
        return False