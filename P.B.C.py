import requests
import hashlib
import sys
import time
import os 
from colorama import init, Fore
import re  


init()

os.system('title Password Breach Checker - by execRooted')

API_URL = "https://api.pwnedpasswords.com/range/"


def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def check_password_breach(password):
    
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

  
    prefix = sha1_hash[:5]
   
    suffix = sha1_hash[5:]

   
    response = requests.get(f"{API_URL}{prefix}")

    if response.status_code == 200:
      
        hashes = response.text.splitlines()

        
        for hash in hashes:
            hash_suffix, count = hash.split(':')
            if hash_suffix == suffix:
                return True, count
        return False, 0
    else:
        typewriter(f"{Fore.RED}Error checking password... Please try again later.{Fore.RESET}")
        return False, 0

def check_password_strength(password):
   
    length = len(password)

  
    has_uppercase = re.search(r"[A-Z]", password) is not None
    has_lowercase = re.search(r"[a-z]", password) is not None
    has_number = re.search(r"[0-9]", password) is not None
    has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None


    if length < 8 or not has_uppercase or not has_lowercase or not has_number or not has_special:
        return "Weak", "Password must be at least 8 characters long and contain uppercase letters, numbers, and special characters."
    
    
    if length <= 12:
        if has_uppercase and has_lowercase and has_number and has_special:
            return "Medium", "Password is better, but could be longer."
        return "Medium", "Password could be improved by including uppercase, numbers, and special characters."

   
    if length <= 16:
        if has_uppercase and has_lowercase and has_number and has_special:
            return "Strong", "Your password is strong!"
        return "Medium", "Password could be improved by including uppercase, numbers, and special characters."
    
    
    if length > 16:
        if has_uppercase and has_lowercase and has_number and has_special:
            return "Very Strong", "Your password is very strong and secure!"
        return "Strong", "Password is strong but could benefit from more complexity (e.g., no common patterns)."

    return "Weak", "Password is too weak."

def logo():
    
    print(f"""{Fore.BLUE}
   \\     /  
    \\   /   
     \\ /    
      |     
      |     
      |     
      |     
   _________
  |   PBC   |
  |_________|
{Fore.RESET}""")

def display_main_menu():
    
    typewriter(f"{Fore.CYAN}=== Password Breach Checker ==={Fore.RESET}", delay=0.04)
    typewriter(f"{Fore.GREEN}[1]{Fore.RESET} Check a password for breaches", delay=0.04)
    typewriter(f"{Fore.GREEN}[2]{Fore.RESET} Check password strength", delay=0.04)
    typewriter(f"{Fore.GREEN}[3]{Fore.RESET} Exit program", delay=0.04)

def clear_screen():
    
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def main():
    while True:
        clear_screen()  
        logo()  
        display_main_menu() 

       
        choice = input(f"\n{Fore.YELLOW}Please select an option: {Fore.RESET}").strip()

        if choice == '1':
            
            while True:
                password = input(f"{Fore.YELLOW}Enter your password to check for breaches: {Fore.RESET}").strip()
                if len(password) < 8:
                    print(f"{Fore.RED}Password must be at least 8 characters long!{Fore.RESET}")
                    continue

                typewriter(f"{Fore.CYAN}Checking if the password '{password}' has been breached...{Fore.RESET}", delay=0.04)

               
                is_breached, count = check_password_breach(password)

                if is_breached:
                    typewriter(f"{Fore.RED}Warning! This password has been found in {count} breaches!{Fore.RESET}")
                else:
                    typewriter(f"{Fore.GREEN}This password is safe. No breaches found.{Fore.RESET}")

                
                choice_check_another = input(f"\n{Fore.YELLOW}Would you like to check another password? (y/n): {Fore.RESET}").strip().lower()
                if choice_check_another != 'y':
                    break  

        elif choice == '2':
            
            while True:
                password = input(f"{Fore.YELLOW}Enter your password to check its strength: {Fore.RESET}").strip()

                
                strength, feedback = check_password_strength(password)
                typewriter(f"{Fore.CYAN}Password Strength: {strength}. {feedback}{Fore.RESET}")

                if strength == "Weak":
                    typewriter(f"{Fore.RED}Consider using a stronger password before checking for breaches.{Fore.RESET}")
                    continue

                
                choice_check_another = input(f"\n{Fore.YELLOW}Would you like to check another password? (y/n): {Fore.RESET}").strip().lower()
                if choice_check_another != 'y':
                    break  

        elif choice == '3':
           
            typewriter(f"{Fore.CYAN}Exiting program...{Fore.RESET}", delay=0.04)
            sys.exit()

        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Fore.RESET}")



if __name__ == "__main__":
    main()
