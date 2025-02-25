def calculator():
    print("مرحبًا! هذا برنامج آلة حاسبة بسيط.")
    print("العمليات المتاحة: +, -, *, /")

    num1 = float(input("أدخل الرقم الأول: "))

    operation = input("أدخل العملية (+, -, *, /): ")

    num2 = float(input("أدخل الرقم الثاني: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:  
            result = num1 / num2
        else:
            print("خطأ: لا يمكن القسمة على صفر!")
            return
    else:
        print("عملية غير صالحة! الرجاء اختيار عملية من القائمة.")
        return

    print(f"النتيجة: {num1} {operation} {num2} = {result}")

calculator()