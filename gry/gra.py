import random

# wylosuj liczbę od 1 do 100
number = random.randint(1, 100)

# określ maksymalną liczbę prób
max_guesses = 5

# zmień liczbę prób na liczbę prób, które pozostały graczowi
guesses_left = max_guesses

# główna pętla gry
while guesses_left > 0:
    # pobierz liczbę od gracza
    guess = int(input("Zgadnij liczbę: "))

    # sprawdź, czy liczba jest poprawna
    if guess == number:
        # jeśli liczba jest poprawna, wyświetl komunikat o wygranej i zakończ grę
        print("Zgadłeś! Gratulacje!")
        break
    elif guess < number:
        # jeśli liczba jest za mała, wyświetl komunikat i zmniejsz liczbę pozostałych prób
        print("Twoja liczba jest za mała. Spróbuj ponownie.")
        guesses_left -= 1
    else:
        # jeśli liczba jest za duża, wyświetl komunikat i zmniejsz liczbę pozostałych prób
        print("Twoja liczba jest za duża. Spróbuj ponownie.")
        guesses_left -= 1

# jeśli gracz wykorzystał wszystkie próby, wyświetl komunikat o przegranej
if guesses_left == 0:
    print("Niestety, nie udało Ci się zgadnąć liczby. Koniec gry.")