import re

def validatePassword(password: str) -> bool:
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return bool(re.match(pattern, password))