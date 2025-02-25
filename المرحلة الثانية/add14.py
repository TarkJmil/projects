try:

    numerator = int(input("Enter the number you want to divide: "))
    denominator = int(input("Enter the number you want to divide by: "))
    

    result = numerator / denominator
    

    print(f"The result of the division is: {result}")

except ZeroDivisionError:

    print("Error: You can't divide by zero!")

except ValueError:

    print("Error: Only integers should be entered!")

except Exception as e:

    print(f"An unexpected error occurred: {e}")

else:

    print("The operation was successful!")

finally:

    print("Thanks for using the program!")