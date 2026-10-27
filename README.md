# The Sentinel

A Python password strength analyzer that estimates real-world crack time and checks against known common/breached passwords.

## Description

The Sentinel measures password entropy (in bits), estimates how long a password would realistically take to crack under two different attack scenarios, and checks it against a list of widely known common/breached passwords — since entropy alone can't catch a password like `password123`, which scores reasonably on character diversity but gets guessed in seconds by any real attacker.

## Features

- Calculates entropy based on character-class diversity and length
- Estimates crack time under two threat models: an offline fast-hash attack (~10^10 guesses/sec) and an online rate-limited login (~10 guesses/sec)
- Flags passwords that appear in a list of common/breached passwords, skipping the entropy math entirely since it doesn't apply
- Reports which character types (uppercase, lowercase, digits, symbols) a password is missing
- Hides password input while typing
- Lets you test multiple passwords in one session; type `q` to quit

## Requirements

- Python 3.x (standard library only — no external dependencies)

## Usage

Run `python password_analyzer.py` and enter a password when prompted. For each password tested, it reports:

1. Whether the password appears in the common/breached password list
2. If not, its entropy in bits and estimated crack time under both threat models
3. Suggestions for improving character diversity or length, if any

## Limitations

The common-password list is a small, illustrative set (around 40 entries) for demonstration purposes — not a comprehensive breach database like haveibeenpwned's Pwned Passwords. The entropy formula also assumes characters are chosen uniformly at random, which overestimates the real strength of predictable human-chosen passwords not already in the list; the common-password check exists specifically to catch some of that gap, not all of it.

## Author

Mike McGregor
