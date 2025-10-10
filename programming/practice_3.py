import datetime
from decimal import Decimal


goods = {}


def add(items, title, a, expiration_date=None):
    exp_date_obj = None
    if expiration_date:
        exp_date_obj = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
    new_batch = {
        "amount": a,
        "expiration_date": exp_date_obj
    }
    if title in items:
        items[title].append(new_batch)
    else:
        items[title] = [new_batch]


def add_by_note(items, note):
    parts = note.split()
    expiration_date = None
    try:
        datetime.datetime.strptime(parts[-1], "%Y-%m-%d")
        expiration_date = parts[-1]
        amount_str = parts[-2]
        title = " ".join(parts[:-2])
    except (ValueError, IndexError):
        amount_str = parts[-1]
        title = " ".join(parts[:-1])
    amount = Decimal(amount_str)
    add(items, title, amount, expiration_date)


def find(items, needle):
    found_products = []
    needle_lower = needle.lower()
    for title in items:
        if needle_lower in title.lower():
            found_products.append(title)
    return found_products


def amount(items, needle):
    total_amount = Decimal("0")
    matching_titles = find(items, needle)
    for title in matching_titles:
        batches = items[title]
        for batch in batches:
            total_amount += batch["amount"]
    return total_amount

