from generaattori import Generaattori


class Kayttoliittyma:

    def __init__(self):
        self.generaattori = Generaattori()

    def kaynnista(self):
        print("Tervetuloa latteusgeneraattoriin, joka luo miete- tai voimalauseen, jolla voit pilata päiväsi tai jonkun muun päivän.")
        while(True):
            print("Syötä haluamasi teema tai luo satunnainen latteus painamalla vain enter. Lopeta syöttämällä 0.")
            teema = input("Teema: ")
            if teema == '0':
                break
            print(self.generaattori.generoi(teema))
