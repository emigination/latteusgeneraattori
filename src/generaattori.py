import random
import io
from sanalaskija import Sanalaskija


class Generaattori:
    """Luokka, joka luo lauseita sanalistojen ja todennäköisyystaulukon avulla.
    """

    def __init__(self, tiedostopolku='/home/emiander/Tiralabra/latteusgeneraattori/data/opetusdata.txt'):
        """Luokan konstruktori, joka hakee tarvittavan datan tiedostoista tai niiden puuttuessa kutsuu sanalaskijan luomaan tarvittava data.
        """

        data = self.lue_tiedostot()
        if not data:
            data = Sanalaskija().opettele(tiedostopolku)
        self.todennakoisyystaulukko = data[0]
        self.sanalista = data[1]
        self.ensimmaiset = data[2]
        self.jatkavat = data[3]

    def generoi(self):
        """Luo lauseita Markovin ketjun avulla.

        Returns:
            Valmis mietelause merkkijonona.
        """
        indeksi = self.ensimmaiset[random.randint(0, len(self.ensimmaiset)-1)]
        lause = self.sanalista[indeksi]
        while len(lause) < 200:
            satunnainen = random.random()
            summa = 0
            for i, todennakoisyys in enumerate(self.todennakoisyystaulukko[indeksi]):
                summa += todennakoisyys
                if summa >= satunnainen and summa>0:
                    lause += ' ' + self.sanalista[i]
                    indeksi = i
                    break
            if summa == 0:
                if len(lause) > 20 or len(self.jatkavat)<1:
                    break
                indeksi = self.jatkavat[random.randint(0, len(self.jatkavat)-1)]
                lause += ' ' + self.sanalista[indeksi]
        return lause

    def lue_tiedostot(self):
        """Lukee tiedostoista lauseiden luomiseen tarvittavat sanalistat sekä todennäköisyystaulukon.

        Returns:
            4-tuple, jossa on kaksiulotteinen taulukko sanoista ja seuraavan sanan todennäköisyyksistä, lista kaikista sanoista, lista sanoista, jotka voivat aloittaa mietelauseen, sekä lista sanoista, jotka voivat aloittaa toisen lauseen mietelauseen sisällä. Jos jonkin tieoston lukeminen ei onnistunut, palautetaan Null.
        """
        try:
            with open(todennakoisyydet.csv) as todennakoisyydet:
                pass
            with open(sanalista.csv) as sanalista:
                pass
            with open(ensimmaiset.csv) as ensimmaiset:
                pass
            with open(jatkavat.csv) as jatkavat:
                pass
        except:
            return
        return (0, 0, 0, 0)
