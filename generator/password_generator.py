import secrets
import string


def generate_password(
    length=12,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_symbols=True,
):
    """Generate a secure random password."""

    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password
