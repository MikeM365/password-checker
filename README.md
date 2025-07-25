# Password Strength Checker

A simple, secure, command-line Python script to evaluate the strength of a password based on a set of common complexity criteria.

## How It Works: Purely Local Analysis

This tool prioritizes your security. **Your password is never sent over the internet or stored anywhere.** All analysis happens locally on your machine.

The script evaluates a password against five criteria:
1.  **Length:** Is it at least 8 characters long?
2.  **Uppercase:** Does it contain at least one uppercase letter (A-Z)?
3.  **Lowercase:** Does it contain at least one lowercase letter (a-z)?
4.  **Digits:** Does it contain at least one number (0-9)?
5.  **Special Characters:** Does it contain at least one special character (e.g., `!@#$%&`)?

Based on how many criteria are met, the password is given a score from 0 to 5 and classified into a strength category.

## Features

-   **100% Secure & Offline:** Password analysis is performed entirely on your device.
-   **Clear Scoring System:** Provides a score (0-5) to quantify the password's complexity.
-   **Actionable Feedback:** Gives specific, helpful suggestions on how to improve a weak password.
-   **Strength Categories:** Classifies passwords from "Extremely Weak" to "Strong" for an at-a-glance assessment.
-   **No Dependencies:** Runs using only standard Python libraries.

## Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/MikeM365/password-checker.git
    ```

2.  **Navigate to the Project Directory**
    ```bash
    cd password-checker
    ```
    This project has no external dependencies, so no installation of packages is required.

## Usage

As the script is currently written, you can test it by following these steps:

1.  Open the `password_checker.py` file in a code editor.
2.  Find the line `test_password = "password123!"` near the bottom of the file.
3.  Change the value of `test_password` to the password you want to evaluate.
4.  Save the file and run it from your terminal:
    ```bash
    python password_checker.py
    ```

**Example Output:**
Function is checking password: password123!
Password: password123!
Strength: Moderate (Score: 4)
Suggestions:

Password should contain at least one uppercase letter.
