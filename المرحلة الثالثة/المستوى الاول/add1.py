x = int(input("إدخل عدد الأرقام: "))


a = []
for i in range(x):
    y = int(input(f"إدخل رقم {i+1}: "))
    a.append(y)


s = sum(a) / x


print(f"المتوسط الحسابي هو: {s}")