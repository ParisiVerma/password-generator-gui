"""
Password Generator + Strength Checker
Run: python main.py
"""

import secrets
import string
import math
from strength_checker import check_password_strength

# ---------------------------------------------------------
# Step 1: Password Generator
# ---------------------------------------------------------
def generate_password(length=12, use_lower=True, use_upper=True,
                      use_digits=True, use_symbols=True) -> str:
    """
    Generate a secure random password.
    - length: desired password length (int)
    - use_lower/use_upper/use_digits/use_symbols: booleans to include character types
    """
    if length < 1:
        raise ValueError("Length must be at least 1.")

    pools = []
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.<>/?")

    if not pools:
        raise ValueError("At least one character type must be enabled.")

    # ensure at least one char from each chosen pool for guaranteed variety
    password_chars = [secrets.choice(pool) for pool in pools]

    # fill remaining length with random choices from all selected pools
    all_chars = "".join(pools)
    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_chars))

    # securely shuffle and return string
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


# ---------------------------------------------------------
# Step 2: Password Strength Checker
# ---------------------------------------------------------
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


# ---------------------------------------------------------
# Step 3: Demo Runner
# ---------------------------------------------------------
def demo():
    print("Password Generator + Strength Checker\n" + "-"*40)
    p1 = generate_password()
    print("Generated:", p1)
    print("Strength:", check_password_strength(p1))

    p2 = generate_password(length=16)
    print("\nGenerated:", p2)
    print("Strength:", check_password_strength(p2))


if __name__ == "__main__":
    demo()

