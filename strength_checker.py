# strength_checker.py

import math

def check_password_strength(password: str) -> str:
    """
    Check the strength of a given password.
    Returns: "Weak", "Medium", or "Strong"
    """
    length = len(password)
    categories = 0

    if any(c.islower() for c in password):
        categories += 1
    if any(c.isupper() for c in password):
        categories += 1
    if any(c.isdigit() for c in password):
        categories += 1
    if any(c in "!@#$%^&*()-_=+[]{};:,.<>/?" for c in password):
        categories += 1

    # Calculate a rough entropy score
    entropy = math.log2((categories * 26 + 10 + 32) ** length)

    # Decide strength level
    if entropy < 40 or length < 8:
        return "Weak"
    elif entropy < 60:
        return "Medium"
    else:
        return "Strong"
