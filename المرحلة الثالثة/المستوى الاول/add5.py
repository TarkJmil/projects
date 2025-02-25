test = input("إدخل الجملة: ")


x = test.lower()


y = {}
for e in x:
    if e.isalpha():
        if e in y:
            y[e] += 1
        else:
            y[e] = 1

# طباعة النتيجة
print("عدد مرات تكرار كل حرف:")
for e, a in y.items():
    print(f"{e}: {a}")