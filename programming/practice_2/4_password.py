import random
import string


def generate_password(
    l, low, up, digits, specials
):
    """Generate a password based on given criteria."""
    character_pool = ""
    if low:
        character_pool += string.ascii_lowercase
    if up:
        character_pool += string.ascii_uppercase
    if digits:
        character_pool += string.digits
    if specials:
        character_pool += string.punctuation

    if not character_pool:
        return None

    password_list = [random.choice(character_pool) for _ in range(l)]
    return "".join(password_list)


def prompt(text):
    while True:
        answer = input(text + " [Y/n]: ").lower().strip()
        if answer in ("y", ""):
            return True
        if answer == "n":
            return False
        print("[Y/n]: ")


length = int(input("Введите длину пароля: "))
if length <= 0:
    print("Длина должна быть положительным числом.")
    exit()
while True:
    use_lower = prompt("Включить нижний регистр?")
    use_upper = prompt("Включить верхний регистр?")
    use_digits = prompt("Включить цифры?")
    use_symbols = prompt("Включить специальные символы?")

    if any((use_lower, use_upper, use_digits, use_symbols)):
        break
    print("\nВыберите хоть что-то!\n")

password = generate_password(
    length, use_lower, use_upper, use_digits, use_symbols
)
print(f"Ваш пароль: {password}")
