"""
Project 2: The Sentinel (Password Strength & Entropy Analyzer)
Author: Mike McGregor
Purpose: Analyzes password complexity using Regex and Information Theory (Entropy).
"""
import re
import math
import sys
import getpass

def calculate_entropy(password: str) -> float:
    """
    Calculates the 'Information Entropy' of a password in bits.
    Formula: E = L * log2(R)
    L = length of the password
    R = Size of the pool of characters used
    """ 
    pool_size = 0

    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r' [0-9]', password):
        pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password): 
        pool_size += 32 

    if pool_size == 0:
        return 0
    
    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)

def check_strength(password: str):
    """
    Checks a password against common complexity rules.
    """
    score = 0
    feedback = []

    if len(password) >= 12:
         score += 2
         feedback.append("[+] Length is good (12+ chars)")
    elif len(password) >= 8:
         score += 1
         feedback.append("[+] Length is okay (8-11 chars), but 12 is recommended")
    else:
         feedback.append("[-] Password is too short (less than 8 chars)")

    if re.search(r'[A-Z]', password):
         score += 1
    else:
         feedback.append("[-] Add uppercase letters")

    if re.search(r'[a-z]', password):
       score += 1
    else:
       feedback.append("[-] Add Lowercase letters")

    if re.search(r'[0-9]', password):
       score += 1
    else:
       feedback.append("[-] Add Numbers")

    if re.search(r'[^a-zA-Z0-9]', password):
       score += 1
    else:
       feedback.append("[-] Add Symbols (!@#$)")

    return score, feedback

def main():
    print("\n=== The Sentinel: Password Strength Analyzer ===")
    print("Type a password to test (input is hidden for security).")
    print("Press Ctrl+C to exit.\n")

    while True:
        try:
            pwd = getpass.getpass("Enter Password to Test: ")

            if pwd.lower() == 'q':
             print("Goodbye! Stay secure! 🛡️")
             break
            
            if not pwd:
                print("(!) Please enter a password.")
                continue

            entropy = calculate_entropy(pwd)
            score, feedback = check_strength(pwd)

            print(f"\n--- Analysis Result ---")
            print(f"Password Length: {len(pwd)}")
            print(f"Entropy Score:   {entropy} bits")

            if entropy < 28:
                print("Time to Crack:   Instantly")
            elif entropy < 60:
                print("Time to Crack:   Minutes to Hours")
            elif entropy < 128:
                print("Time to Crack:   Centuries (Secure)")
            else:
                print("Time to Crack:   Heat Death of the Universe (Overkill)")
     
            print("\nFeedback:")
            for item in feedback:
                print(item)
            
            print("-" * 30 + "\n")

        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit()

if __name__ == "__main__":
    main()







