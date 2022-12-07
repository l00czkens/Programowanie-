# Importujemy bibliotekę Tkinter
import tkinter as tk

# Funkcja, która zostanie wywołana po naciśnięciu przycisku "="
def calculate():
    # Pobieramy tekst z pola tekstowego
    expression = entry.get()
    # Wykonujemy działanie matematyczne i wyświetlamy wynik
    result = eval(expression)
    label["text"] = str(result)

# Tworzymy okno aplikacji
root = tk.Tk()

# Tworzymy pole tekstowe, w którym użytkownik będzie wprowadzał działanie matematyczne
entry = tk.Entry(root)
entry.pack()

# Tworzymy przycisk "=", po naciśnięciu którego zostanie wywołana funkcja calculate
button = tk.Button(root, text="=", command=calculate)
button.pack()

# Tworzymy etykietę, w której wyświetlimy wynik działania matematycznego
label = tk.Label(root)
label.pack()

# Uruchamiamy aplikację
root.mainloop()