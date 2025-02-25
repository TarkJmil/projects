y = int(input("إدخل عدد العناصر: "))


x = []
for i in range(y):
    a = float(input(f"إدخل عنصر {i+1}: "))
    x.append(a)


d = [abs(a) for a in x]


print("القائمة الأصلية:")
print(x)
print("القائمة بعد حساب القيم المطلقة:")
print(d)