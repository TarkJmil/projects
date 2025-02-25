def templats(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


x = int(input("إدخل عدد: "))

if templats(x):
    print("الرقم هو عدد أولي.")
else:
    print("الرقم ليس عدد أولي.")