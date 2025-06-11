def circle_area(r):
    return r * r * 3.14


a = circle_area(2.5)
print("半径2.5の円の面積は", a)


def is_positive(i):
    if i > 0:
        return True
    else:
        return False


a = 10
if is_positive(a) == True:
    print("aの値は正です")
else:
    print("aの値は負またはゼロです")
