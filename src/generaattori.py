import random
from collections import deque
import io
from sanalaskija import Sanalaskija


class Generaattori:
    """Luokka, joka luo lauseita sanalistojen ja todennäköisyystaulukon avulla.
    """

    def __init__(self, aste=1, tiedostopolku='data/opetusdata.txt'):
        """Luokan konstruktori, joka hakee tarvittavan datan tiedostoista tai niiden puuttuessa kutsuu sanalaskijan luomaan tarvittava data.
        """
        self.aste = aste
        data = self._lue_tiedostot()
        if not data:
            data = Sanalaskija(self.aste).opettele(tiedostopolku)
        self.trie = data[0]
        self.ensimmaiset = data[1]
        # self.jatkavat = data[2]

    def generoi(self):
        """Luo lauseita Markovin ketjun avulla.

        Returns:
            Valmis mietelause merkkijonona.
        """
        edelliset = random.choice(list(self.ensimmaiset))
        sanat = []
        for sana in edelliset:
            sanat.append(sana)
        edelliset = deque(edelliset)
        while len(sanat) < 20:
            seuraavat = self.trie.hae_seuraavat_sanat(list(edelliset))
            if not seuraavat and len(sanat) > 3 and random.random() < 0.3:
                break
            while not seuraavat:
                edelliset = deque(random.choice(list(self.ensimmaiset)))
                for sana in edelliset:
                    sanat.append(sana)
                seuraavat = self.trie.hae_seuraavat_sanat(edelliset)
            summa = 0
            for maara in seuraavat.values():
                summa += maara
            satunnainen = random.randint(0, summa)
            summa = 0
            for sana, maara in seuraavat.items():
                summa += maara
                if summa >= satunnainen:
                    seuraava = sana
                    break
            sanat.append(seuraava)
            edelliset.popleft()
            edelliset.append(seuraava)
        lause = self._muuta_merkkijonoksi(sanat)
        return lause

    def _muuta_merkkijonoksi(self, sanalista):
        """Muuttaa sanalistan merkkijonoksi eli valmiiksi lauseeksi.

        Args:
            sanalista: lauseeseen tulevat sanat

        Returns:
            lause merkkijonona.
        """
        lause = ''
        for sana in sanalista[:len(sanalista)-1]:
            lause += sana
            lause += ' '
        lause += sanalista[len(sanalista)-1]
        if lause[len(lause)-1] not in ('.', '!', '?'):
            lause += '.'
        return lause

    def _lue_tiedostot(self):
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
