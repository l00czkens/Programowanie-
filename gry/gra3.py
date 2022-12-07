# Definujemy zmienną memory, w której będziemy przechowywać wartość zapisaną w pamięci
memory = 0

# Pętla, w której będzie działać kalkulator
while True:
    # Pobieramy od użytkownika działanie, które chce wykonać
    action = input("Co chcesz zrobić? (+, -, *, /, MS, MR, MC, q): ")

    # Sprawdzamy, co użytkownik chce zrobić
    if action == "+":
        # Jeśli chce dodać, to pobieramy dwie liczby od użytkownika i wyświetlamy wynik
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        result = a + b
        print(f"{a} + {b} = {result}")

    elif action == "-":
        # Jeśli chce odjąć, to pobieramy dwie liczby od użytkownika i wyświetlamy wynik
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        result = a - b
        print(f"{a} - {b} = {result}")

    elif action == "*":
        # Jeśli chce pomnożyć, to pobieramy dwie liczby od użytkownika i wyświetlamy wynik
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        result = a * b
        print(f"{a} * {b} = {result}")

    elif action == "/":
        # Jeśli chce podzielić, to pobieramy dwie liczby od użytkownika i wyświetlamy wynik
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))