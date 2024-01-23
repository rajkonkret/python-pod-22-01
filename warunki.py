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

