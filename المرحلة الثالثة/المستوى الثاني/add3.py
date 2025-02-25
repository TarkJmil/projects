test = []
for i in range(int(input("إدخل عدد العناصر في القائمة: "))):
    y = float(input(f"إدخل عنصر {i+1}: "))
    test.append(y)


Positive_Numbers = [x for x in test if x > 0]
Negative_numbers = [x for x in test if x < 0]
templat = [x for x in test if x == 0]


print("الأعداد الموجبة:")
print(Positive_Numbers)
print("الأعداد السالبة:")
print(Negative_numbers)
print("الأعداد الناتجة:")
print(templat)