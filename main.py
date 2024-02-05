import time
x = {
    'CRINGE':'coś wyjątkowo dziwnego lub zawstydzającego',
    'XD':'coś śmiesznego',
    'LOL':'Reakcja na coś śmiesznego',
    'EZ':'łatwo'
    }
while True:
    y=input('Wpisz słowo którego chcesz zrozumieć definicje (duże litery)')
    if y in x.keys():
        print(x[y])
        time.sleep(1)
    else:
        print('Nie mamy jeszcze tego słowa')
        time.sleep(1)
