bill = float(input("Enter your bill amount: "))

if bill > 5000:
    discount = bill * 20 / 100
    final_bill = bill - discount
    print("Discount: ₹", discount)
    print("Final Bill: ₹", final_bill)

elif bill > 3000:
    discount = bill * 10 / 100
    final_bill = bill - discount
    print("Discount: ₹", discount)
    print("Final Bill: ₹", final_bill)

else:
    print("No discount")
    print("Final Bill: ₹", bill)






num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")




num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")




sales = float(input("Enter sales amount: "))
attendance = float(input("Enter attendance percentage: "))

if sales >= 100000 and attendance >= 90:
    print("Employee is eligible for bonus")
else:
    print("Employee is not eligible for bonus")




age = int(input("Enter your age: "))
citizenship = input("Enter your citizenship: ")

if age >= 18 and citizenship == "Indian":
    print("Person is eligible to vote")
else:
    print("Person is not eligible to vote")    
