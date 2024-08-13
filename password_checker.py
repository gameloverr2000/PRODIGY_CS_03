import re

def password_strength_checker(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Count how many criteria are met
    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    # Determine strength
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Feedback
    feedback = {
        "length": length_criteria,
        "uppercase": upper_criteria,
        "lowercase": lower_criteria,
        "digit": digit_criteria,
        "special_character": special_criteria,
        "strength": strength
    }

    return feedback

# Example usage
password = input("Enter a password to check its strength: ")
result = password_strength_checker(password)

print("\nPassword Strength Assessment:")
print(f"Strength: {result['strength']}")
print(f"Meets Length Requirement: {'Yes' if result['length'] else 'No'}")
print(f"Contains Uppercase Letters: {'Yes' if result['uppercase'] else 'No'}")
print(f"Contains Lowercase Letters: {'Yes' if result['lowercase'] else 'No'}")
print(f"Contains Digits: {'Yes' if result['digit'] else 'No'}")
print(f"Contains Special Characters: {'Yes' if result['special_character'] else 'No'}")