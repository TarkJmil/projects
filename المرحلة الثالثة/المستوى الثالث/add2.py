import numpy as np

rows = int(input("ادخل عدد السطور في المصفوفة: "))
columns = int(input("ادخل عدد العمود في المصفوفة: "))


matrix = np.random.rand(rows, columns)

mean_rows = np.mean(matrix, axis=1)
std_rows = np.std(matrix, axis=1)
mean_cols = np.mean(matrix, axis=0)
std_cols = np.std(matrix, axis=0)


print("المصفوفة:")
print(matrix)
print("\nمتوسط الصفوف:")
print(mean_rows)
print("\نانحراف المعياري للصفوف:")
print(std_rows)
print("\nمتوسط المعاملات:")
print(mean_cols)
print("\نانحراف المعياري للمعاملات:")
print(std_cols)