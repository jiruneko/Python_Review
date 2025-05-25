def average(*args):
    total = 0
    for a in args:
        total += a
    print(total / len(args))


average(70, 85, 100, 90)


def print_data(**kwargs):
    for key, value in kwargs.items():
        print(f"キー:{key}, 値:{value}")


print_data(item="リンゴ", count=1, price=120)
