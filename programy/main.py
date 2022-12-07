
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("wybierz opcje.")
print("1.dodaj")
print("2.odejmij")
print("3.mnozenie")
print("4.dzielenie")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("dodaj pierwsza liczbe: "))
        num2 = float(input("dodaj druga liczbe: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))


        next_calculation = input("nowa kalkulacja??? (tak/nie): ")
        if next_calculation == "nie":
            break

    else:
        print("blad")
