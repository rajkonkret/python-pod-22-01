# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zaleznosci od warunku (czy True czy False wykonuje odpowiedni blok programu)

odp = True  # prawda - warunek spełniony
odp2 = not odp
print(odp2)  # False

if odp:
    print("Brawo")  # obowiązkowe wciecie, 4 spacje
else:
    print('Musisz sie uczyc dalej')

print("dalsza częśc programu")

# podatek = 0
# zarobki = int(input("podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:  # pozostałe
#     podatek = 0.6
#
# print(f"Zapłacisz {zarobki * podatek}")
# Kolejnośc warunków ma znaczenie
# Pierwszy spełniony powoduje wyjście z drzewka warunków

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabat}")

# zasymulejemy system zbierania logow
# zmienne ktore symuluja dane z innego systemu
# na podstawie tych danych bedziemy wykonywac rózne działania
# email, console, dowolny inny
# alert z consosli wydrukujemy gotowy komunikat
# Stało się coś strasznego
# zapiszemy kounikat do listy i wypiszemy liste, komunikaty moga miec rozne statusy error, medium. inny

alert_system = 'console'
error = 'medium'

error_message = "Stało się coś strasznego"

lista_bledow = []
if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    print("Alert z systemu email")
    if error == 'error':
        lista_bledow.append("bład")
    elif error == 'medium':
        lista_bledow.append("średnie")
    else:
        lista_bledow.append("inny")
else:
    print("Nie znam takiego systemu")

print(lista_bledow)

# napisac test z ...
# zadac pytanie
# pobrac odpowiedz
# sprawdzic czy prawidłowa
# wyswietlic wynik

odp = input("Podaj datę chrztu Polski")
if odp == '966':
    print("Prawidłowa data")
else:
    print("Nieprawidłowa data")
