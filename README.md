# P.B.C. Project: Password Breach Checker

## Installation

### Prerequisites
- **Python 3.x** installed on your system.
- **pip** (Python package manager).

### Dependencies
Install required libraries via pip:

```bash
pip install -r requirements.txt
```

Alternatively, install the `pycryptodome` and `requests` packages directly:

```bash
pip install pycryptodome requests
```

## Usage

### 1. Clone or Download the Repository
```bash
git clone https://github.com/execRooted/P.B.C-Project.git
cd P.B.C-Project
```

### 2. Run the Program
```bash
python P.B.C.py
```

You will see the main menu:

```
=== Password Breach Checker ===
[1] Check a password for breaches
[2] Check password strength
[3] Exit program
```

Select an option by entering `1`, `2`, or `3`.

#### a. Check Password for Breaches
- Enter a password when prompted.
- The program uses the Pwned Passwords API to check if the SHA-1 hash of your password appears in known breaches.
- If found, it reports the number of occurrences.

#### b. Check Password Strength
- Enter a password when prompted.
- The program evaluates strength based on:
  - Length
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- It classifies your password as **Weak**, **Medium**, **Strong**, or **Very Strong**.

#### c. Exit Program
- Closes the application.

## How It Works

1. **Breach Check**  
   - Computes SHA-1 hash of the input password.
   - Sends the first 5 characters of the hash (prefix) to the Pwned Passwords API.
   - Compares the suffix against returned hash suffixes to detect breaches.

2. **Strength Evaluation**  
   - Checks password length.
   - Verifies presence of different character types (uppercase, lowercase, digits, symbols).
   - Assigns a strength rating.

## Examples

**Breach Check**

```
Enter your password to check for breaches: password123
Checking if 'password123' has been breached...
Warning! This password has been found in 5 breaches!
```

**Strength Check**

```
Enter your password to check its strength: !@##I_Like_Github!@##!
Password Strength: Strong. Your password is strong!
```

## Creating a Standalone Executable

Use **PyInstaller** to bundle the script:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Build the executable:
   ```bash
   python -m PyInstaller --onefile --icon=theIcon.ico P.B.C.py
   ```
3. Find the executable in `dist/P.B.C.exe`.

---

 **Made by execRooted**
