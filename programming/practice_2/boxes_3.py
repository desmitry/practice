def print_pack_report(cakes_count):
    """Return a packaging report."""
    for i in range(cakes_count, 0, -1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} - расфасуем по 3 или по 5")
        elif i % 5 == 0:
            print(f"{i} - расфасуем по 5")
        elif i % 3 == 0:
            print(f"{i} - расфасуем по 3")
        else:
            print(f"{i} - не заказываем!")


print_pack_report(30)
