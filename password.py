import string
import secrets


def password_gen(Length: int, Symbols: bool, Uppercase: bool):
    combination = (
        string.ascii_lowercase + string.digits
    )  # starting point lowercase letters and digit
    if Symbols:
        combination += string.punctuation  # Let users decide to use symbols or not

    if Uppercase:
        combination += (
            string.ascii_uppercase
        )  # Let users decide to use uppercase or not

    combination_length = len(combination)  # user set combination lenghth

    new_password = ""

    for _ in range(Length):
        new_password += combination[
            secrets.randbelow(combination_length)
        ]  # get index of all of the above random

    return new_password


for _, index in enumerate(range(5)):  # print range
    password = password_gen(
        Length=30, Symbols=True, Uppercase=True
    )  # change password parameter
    print(index + 1, ">>", password)
