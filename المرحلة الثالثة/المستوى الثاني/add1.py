from datetime import datetime


test = input("إدخل التاريخ الأول (يوم/شهر/سنة): ")


test = datetime.strptime(test, "%d/%m/%Y")


templats = input("إدخل التاريخ الثاني (يوم/شهر/سنة): ")


templats = datetime.strptime(templats, "%d/%m/%Y")


aming = abs((templats - test).days)


if aming > 0:
    print(f"الفاصل الزمني بين التاريخين هو {aming} يومًا.")
elif aming == 0:
    print("التاريخان هما نفس التاريخ.")
else:
    print("التاريخان هما قبل التاريخ الأوّل.")