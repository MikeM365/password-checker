def check_password_strength(password):
    print(f"Function is checking password: {password}")

    score = 0
    feedback = []

    #Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    #Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    #Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    #Check for digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    #Check for special characters
    if any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")  

    #Determine strength based on score
    if score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Moderate"
    elif score == 3:
        strength = "Weak"  
    elif score == 2:
        strength = "Very Weak"
    else:
        strength = "Extremely Weak"

    #Return the result
    return {"score": score,"strength": strength,"feedback": feedback}

#Test the function
test_password = "password123!"
result = check_password_strength(test_password)
print(f"Password: {test_password}")
print(f"Strength: {result['strength']} (Score: {result['score']})")
if result['feedback']:
    print("Suggestions:")
    for suggestion in result['feedback']:
        print(f"- {suggestion}")
      
  