# Password Checker

A secure, command-line tool to check if your password has been compromised in a data breach. This script uses the haveibeenpwned.com 'Pwned Passwords' API.

## How It Works: A Focus on Security

Your security and privacy are paramount. This tool **never** sends your actual password anywhere. It uses a security model called **k-Anonymity** to protect your data. Here's the process:

1.  **Local Hashing:** Your password is first converted into a SHA-1 hash on your own machine.
2.  **Partial Hash Transmission:** Only the **first 5 characters** of that hash are sent to the Pwned Passwords API.
3.  **Receiving a List:** The API returns a list of all password hash suffixes that begin with those same 5 characters.
4.  **Local Verification:** The script then searches that list locally on your machine to see if the remaining part of your hash is present.

This process ensures that your full password (or even your full password hash) is never exposed to any external service.

## Features

-   **Secure by Design:** Uses the k-Anonymity model to protect your privacy.
-   **Bulk Checking:** Check multiple passwords in a single command.
-   **Informative Feedback:** Reports exactly how many times a compromised password has appeared in the data breach database.
-   **Lightweight and Fast:** A simple command-line tool with minimal dependencies.

## Installation

To get this tool running on your local machine, follow these steps.

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/MikeM365/password-checker.git
    ```

2.  **Navigate to the Project Directory**
    ```bash
    cd password-checker
    ```

3.  **Create and Activate a Virtual Environment**
    A virtual environment is recommended to keep project dependencies isolated.
    ```bash
    # Create the environment
    python -m venv venv

    # Activate the environment
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

4.  **Install Required Packages**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script from your terminal, followed by one or more passwords you wish to check.

**Syntax:**
```bash
python password_checker.py <password_1> <password_2> ...
