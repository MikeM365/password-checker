"""
Project 2: The Sentinel (Password Strength & Entropy Analyzer)
Author: Mike McGregor
Purpose: Analyzes password complexity using Regex and Information Theory
         (Entropy), estimates real-world crack time under two threat
         models, and checks against a list of known common/breached
         passwords.
"""

import re
import math
import getpass

# Small illustrative list of widely known common/breached passwords —
# not a full breach-database lookup, just enough to demonstrate that
# entropy alone misses passwords attackers guess first.
COMMON_PASSWORDS = {
    "123456", "password", "123456789", "12345678", "12345", "qwerty",
    "abc123", "password1", "111111", "123123", "letmein", "welcome",
    "monkey", "login", "admin", "iloveyou", "qwerty123", "dragon",
    "sunshine", "princess", "football", "freedom", "whatever", "trustno1",
    "000000", "1q2w3e4r", "zaq1zaq1", "passw0rd", "master", "hello",
}

# Guesses-per-second assumptions for two different attack scenarios.
OFFLINE_FAST_HASH_RATE = 1e10   # offline attack against a weakly-hashed password, modern GPU
ONLINE_RATE_LIMITED = 10        # online login form with basic rate limiting/lockout


def calculate_entropy(password: str) -> float:
    """
    Estimates password entropy in bits: E = L * log2(R), where L is the
    password length and R is the size of the character pool in use.
    Assumes characters are chosen uniformly at random from that pool --
    real human-chosen passwords are usually far more predictable than
    this formula accounts for, which is why the common-password check
    exists alongside it rather than instead of it.
    """
    if not password:
        return 0.0

    pool_size = 0
    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r'[0-9]', password):
        pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        pool_size += 32

    if pool_size == 0:
        return 0.0

    return round(len(password) * math.log2(pool_size), 2)


def estimate_crack_time(entropy_bits: float, guesses_per_second: float) -> str:
    """
    Converts entropy into a real crack-time estimate. On average, a
    brute-force attacker needs about half the keyspace before finding
    a match: average_guesses = 2^(entropy_bits - 1).
    """
    if entropy_bits <= 0:
        return "Instantly"

    average_guesses = 2 ** (entropy_bits - 1)
    seconds = average_guesses / guesses_per_second

    periods = [("seconds", 60), ("minutes", 60), ("hours", 24), ("days", 365), ("years", None)]
    value, unit = seconds, "seconds"
    for name, size in periods:
        unit = name
        if size is None or value < size:
            break
        value /= size

    if unit == "years" and value > 1e12:
        return "Longer than the age of the universe"
    return f"~{value:,.1f} {unit}"


def check_common_password(password: str) -> bool:
    """Returns True if the password appears in the known-common-password list."""
    return password.lower() in COMMON_PASSWORDS


def check_strength(password: str) -> list:
    """Checks character-class diversity and length, returning improvement feedback."""
    feedback = []
    if len(password) >= 12:
        pass
    elif len(password) >= 8:
        feedback.append("Consider using 12+ characters for stronger protection.")
    else:
        feedback.append("Too short — use at least 8 characters, ideally 12+.")

    if not re.search(r'[A-Z]', password):
        feedback.append("Add an uppercase letter.")
    if not re.search(r'[a-z]', password):
        feedback.append("Add a lowercase letter.")
    if not re.search(r'[0-9]', password):
        feedback.append("Add a number.")
    if not re.search(r'[^a-zA-Z0-9]', password):
        feedback.append("Add a symbol.")
    return feedback


def analyze(password: str):
    print()
    if check_common_password(password):
        print("⚠ This password appears in a list of common/breached passwords.")
        print("  No amount of entropy matters here — attackers check these first.")
        return

    entropy = calculate_entropy(password)
    print(f"Entropy: {entropy} bits")
    print(f"Estimated crack time (offline fast-hash attack, ~{OFFLINE_FAST_HASH_RATE:.0e} guesses/sec): "
          f"{estimate_crack_time(entropy, OFFLINE_FAST_HASH_RATE)}")
    print(f"Estimated crack time (online, rate-limited login, ~{ONLINE_RATE_LIMITED} guesses/sec): "
          f"{estimate_crack_time(entropy, ONLINE_RATE_LIMITED)}")

    feedback = check_strength(password)
    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(f"  - {item}")
    else:
        print("\nGood character diversity and length.")


def main():
    print("=== The Sentinel: Password Strength & Entropy Analyzer ===")
    print("Type 'q' to quit.\n")
    while True:
        password = getpass.getpass("Enter a password to test (hidden): ")
        if password.lower() == 'q':
            print("Goodbye!")
            break
        analyze(password)


if __name__ == "__main__":
    main()
