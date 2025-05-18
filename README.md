#P.B.C. Project: Password Breach Checker#


#Instalation#


### Prerequisites
Before you begin, ensure that you have Python 3.x and pip installed on your system. You will also need to install the required Python libraries.

### 1. Clone or Download the repository
If you haven't already, clone or download the project to your local machine:


```git clone https://github.com/execRooted/P.B.C-Project.git```

Open a CMD as admin, in the same location as the repository and type in:

```pip install -r requirements.txt ```

Then, type in the CMD:

```python P.B.C.py```

It should run.

You can also open it using python.

## Usage

### 1. Check a password for breaches
You will be prompted to enter a password. The program will then check if the password has been exposed in any known data breaches using the Pwned Passwords API.

If the password is found in any breaches, the program will alert you with the number of occurrences.

If the password is safe, the program will inform you that no breaches were found.

### 2. Check password strength
You will be prompted to enter a password. The program will evaluate the strength of the password based on criteria such as length, and the presence of uppercase letters, numbers, and special characters.

The strength is classified as:

- **Weak**: Password does not meet security criteria (length or character variety).
- **Medium**: Password is decent, but could be improved.
- **Strong**: Password meets most security criteria and is reasonably secure.
- **Very Strong**: Password meets all security criteria and is highly secure.

### 3. Exit program
Exits the application.

## Example check password for breaches


=== Password Breach Checker ===
[1] Check a password for breaches
[2] Check password strength
[3] Exit program

Please select an option: 1
Enter your password to check for breaches: password123
Checking if the password 'password123' has been breached...
Warning! This password has been found in 5 breaches!

Would you like to check another password? (y/n): n

Now it defaults to the main menu.



##Password strenght example

Enter your password to check its strength: !@##I_Like_Github!@##!
Password Strength: Strong. Your password is strong!

Would you like to check another password? (y/n): n

Now it defaults to the main menu

---

##Exit option

This option closes the program. Not much to say here.

## How it works

- The program generates a SHA-1 hash of the password you input.
- It sends the first 5 characters (prefix) of the hash to the Pwned Passwords API.
- The API returns a list of password hashes that start with that prefix. The program then checks if the remaining part (suffix) of the hash matches any in the list.
- If a match is found, the password has been breached.

For strength evaluation, the program checks the length of the password and evaluates whether it contains a mix of:

- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

## Creating an Executable with PyInstaller

If you want to convert the `Password Breach Checker` Python program into a standalone `.exe` file for Windows, you can use **PyInstaller**.

### Prerequisites
Before proceeding, you need to have **PyInstaller** installed. You can install it using `pip`:


```pip install pyinstaller```

```python -m PyInstaller --onefile --icon=theIcon.ico P.B.C.py```

if you dont want an .ico, skip over the --icon=theIcon.ico step

The location of the exe should be:

dist/P.B.C.exe

Navigate to the dist folder, and double-click on P.B.C.exe to run the program as a standalone executable.

---

**Mady by execRooted**
