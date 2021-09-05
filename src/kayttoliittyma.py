from generaattori import Generaattori


class Kayttoliittyma:

    def __init__(self):
        self.generaattori = Generaattori()

    def kaynnista(self):
        print('Tervetuloa latteusgeneraattoriin, joka luo miete- tai ' +
              'voimalauseen, jolla voit pilata päiväsi tai jonkun muun päivän.')
        print('Syötä haluamasi teema tai luo satunnainen latteus ' +
              'jättämällä teema tyhjäksi ja painamalla enter. Lopeta syöttämällä 0.')
        while True:
            teema = input('Teema (lopeta syöttämällä 0): ')
            if teema == '0':
                break
            aste = ''
            while not aste.isnumeric() or int(aste) < 1:
                aste = input('Anna Markovin ketjujen aste, 1 tai 2: ')
            latteus = self.generaattori.generoi(int(aste), teema, True)
            print(latteus)
