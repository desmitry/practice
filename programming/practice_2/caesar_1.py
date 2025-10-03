ea = "abcdefghijklmnopqrstuvwxyz"
ra = "абвгдеёжзийклмнопрстиуфхцчшщьъэюя"


def ceasars_cipher(x: str, y: int) -> str:
    """Process string through Caesar's Cipher."""
    r = ""
    for c in x:
        if c in ea:
            a = ea
        elif c in ra:
            a = ra
        else:
            r += c
            continue
        p = a.index(c) + y
        while p not in range(len(a)):
            p = p + (1 if p < 0 else -1) * len(a)
        r += a[p]
    return r


m = input("Введите Сообщение: ").lower().strip()
s = int(input("Введите Сдвиг: "))
em = ceasars_cipher(m, s)
print("Обработанное Сообщение:", em)
