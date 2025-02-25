numbers = input("ادخل أرقامًا منفصلة بالفاصلة أو بالنقطة: ")

numbers = [int(x) for x in numbers.split(',')]


max_num = max(numbers)
min_num = min(numbers)

print("اكبر رقم في القائمة:", max_num)
print("أصغر رقم في القائمة:", min_num)