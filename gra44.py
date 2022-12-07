# Importujemy bibliotekę Tkinter
import tkinter as tk

# Importujemy funkcję randint z biblioteki random, która pozwoli nam na wylosowanie liczby
from random import randint

# Tworzymy okno aplikacji
root = tk.Tk()

# Tworzymy etykietę, w której wyświetlimy instrukcję dla użytkownika
label = tk.Label(root, text="Zgadnij liczbę od 1 do 100:")
label.pack()

# Tworzymy pole tekstowe, w którym użytkownik będzie wprowadzał swoją odpowiedź
entry = tk.Entry(root)
entry.pack()

# Funkcja, która zostanie wywołana po naciśnięciu przycisku "Zgaduj"
def guess():
    # Pobieramy liczbę, którą podał użytkownik
    number = int(entry.get())

    # Sprawdzamy, czy użytkownik zgadł liczbę
    if number == secret_number:
        # Jeśli tak, to wyświetlamy komunikat o wygranej i kończymy grę
        label["text"] = "Brawo, zgadłeś! Gratulacje!"
        button["state"]