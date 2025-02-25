def test(N):
    y = [0, 1]
    while len(y) < N:
        y.append(y[-1] + y[-2])
    return y[:N]

N = int(input("إدخل عدد العناصر: "))

y = test(N)

print("أول N أعداد في سلسلة الفيبوناتشي:")
print(y)