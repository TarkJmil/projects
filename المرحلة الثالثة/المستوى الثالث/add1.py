filename = input("ادخل اسم الملف النصي: ")

try:
    with open(filename, 'r') as file:
        text = file.read()
        
    words = text.split()
    
    num_words = len(words)
    
    print("عدد الكلمات في الملف:", num_words)
    
except FileNotFoundError:
    print("الملف لا يوجد")