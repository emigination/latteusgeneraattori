from generaattori import Generaattori


class Kayttoliittyma:

    def __init__(self):
        self.generaattori = Generaattori()

    def kaynnista(self):
        print("Tervetuloa latteusgeneraattoriin.")
        print("Paina enter luodaksesi miete- tai voimalause, jolla voit pilata päiväsi tai jonkun muun päivän.")
        print("Lopeta syöttämällä 0.")
        while(True):
            # teema = input("Syötä haluamasi teema tai lopeta syöttämällä 0: ")
            teema = input()
            if teema == '0':
                break
            print(self.generaattori.generoi())
