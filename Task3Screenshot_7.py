import re

def check_password_complexity(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[\W_]', password):
        score += 1

    return score
password1 = "strongPassword123"
password2 = "weakpass"
print(check_password_complexity(password1))
print(check_password_complexity(password2))