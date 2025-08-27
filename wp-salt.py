#!/usr/bin/env python3

import random
import string

# These characters must not appear in the keys
import re
DISALLOWED_CHARS_REGEX = re.compile(r"""['"\\]""") 

SALT_CONSTANTS = (
    "AUTH_KEY",
    "SECURE_AUTH_KEY",
    "LOGGED_IN_KEY",
    "NONCE_KEY",
    "AUTH_SALT",
    "SECURE_AUTH_SALT",
    "LOGGED_IN_SALT",
    "NONCE_SALT",
)

def generate_random_string(length=64):
    punctuation = DISALLOWED_CHARS_REGEX.sub("", string.punctuation)
    chars = string.ascii_letters + string.digits + punctuation + " "
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

if __name__ == "__main__":
    # Specifications for the spaces before each key so that the values ​​are aligned
    padding = {
        "AUTH_KEY": 9,
        "SECURE_AUTH_KEY": 2,
        "LOGGED_IN_KEY": 4,
        "NONCE_KEY": 8,
        "AUTH_SALT": 8,
        "SECURE_AUTH_SALT": 1,
        "LOGGED_IN_SALT": 3,
        "NONCE_SALT": 7,
    }
    for constant in SALT_CONSTANTS:
        value = generate_random_string(64)
        spaces = ' ' * padding[constant]
        print(f"define('{constant}',{spaces}'{value}');")


# Fenster offen halten, wenn das Script direkt ausgeführt wird (z.B. per Doppelklick oder Tool Launcher)
    try:
        input("\nPress Enter to exit...")
    except EOFError:
        pass




