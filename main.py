from generator.password_generator import generate_password


def main():
    password = generate_password()
    print("Generated password:", password)


if __name__ == "__main__":
    main()
