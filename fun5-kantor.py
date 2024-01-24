# funkcjia kantor
# usd eur

def kantor(waluta):
    print('Uruchomienie kantoru')

    def usd(kwota=0):
        print(f'Wymieniam {kwota} dol. Dostajesz {kwota * 4.00} pln.')

    def eur(kwota=0):
        print(f'Wymieniam {kwota} eur. Dostajesz {kwota * 4.37} eur.')

    if waluta.lower().replace(" ", "") == 'eur':
        return eur
    else:
        return usd


mirek = kantor('usd')
mirek(1000)  # Wymieniam 1000 dol. Dostajesz 4000.0 pln.

zenek = kantor('eur')
zenek(1000)  # Wymieniam 1000 eur. Dostajesz 4370.0 eur.
