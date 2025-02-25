def templat(aming):
    x = (aming * 9/5) + 32
    return x

def test(x):
    aming = (x - 32) * 5/9
    return aming


print("برنامج للتحويل بين الوحدات:")
print("1. سيلسيوس إلى فهرنهايت")
print("2. فهرنهايت إلى سيلسيوس")
y = int(input("إدخل خيارتك: "))

if y == 1:
    aming = float(input("إدخل درجة الحرارة في سيلسيوس: "))
    x = templat(aming)
    print(f"درجة الحرارة في فهرنهايت هي: {x}")
elif y == 2:
    x = float(input("إدخل درجة الحرارة في فهرنهايت: "))
    aming = test(x)
    print(f"درجة الحرارة في سيلسيوس هي: {aming}")
else:
    print("اختيار غير صحيح.")