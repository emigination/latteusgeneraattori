import random
from collections import deque
import io
from sanalaskija import Sanalaskija


class Generaattori:
    """Luokka, joka luo lauseita triehen tallennettujen sanojen ja niiden
    esiintymistiheyksien perusteella.
    """

    def __init__(self, aste=1, tiedostopolku='data/opetusdata.txt'):
        """Luokan konstruktori, joka hakee tarvittavan datan tiedostoista tai
        niiden puuttuessa kutsuu sanalaskijan luomaan tarvittavan datan.
        """
        self.aste = aste
        data = self._lue_tiedostot()
        if not data:
            data = Sanalaskija(self.aste).opettele(tiedostopolku)
        self.trie = data[0]
        self.ensimmaiset = data[1]
        self.jatkavat = data[2]

    def generoi(self, aste=None, teema=None):
        """Luo lauseita Markovin ketjun avulla.

        Returns:
            Valmis mietelause merkkijonona.
        """
        if aste:
            self.aste = aste
        sanat = self._valitse_aloitussanat(teema)
        edelliset = deque(sanat[len(sanat)-self.aste:])
        while len(sanat) < 20:
            seuraavat = self.trie.hae_seuraavat_sanat(list(edelliset))
            if not seuraavat:
                if len(self.jatkavat) < 1:
                    break
                if len(sanat) > 3 and random.random() < (0.1*len(sanat)):
                    break
            while not seuraavat:
                edelliset = deque(random.choice(self.jatkavat))
                for sana in edelliset:
                    sanat.append(sana)
                seuraavat = self.trie.hae_seuraavat_sanat(list(edelliset))
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

    def _valitse_aloitussanat(self, teema=None):
        """Valitsee lauseen aloittavat sanat teeman perusteella tai satunnaisesti.

        Args:
            teema : käyttäjän syöttämä teema, jos mitään.

        Returns:
            [type]: [description]
        """
        sanat = []
        if teema and self.aste < 2:
            if self.trie.hae_seuraavat_sanat([teema]):
                edelliset = [teema]
            else:
                sanat.append(teema)
                seuraavat_sanat = ["on", "on", "ei", "ei", "tulee",
                                   "pysyy", "odottaa", "voi", "tuntee",
                                   "tahtoo", "näkee"]
                edelliset = [random.choice(seuraavat_sanat)]
        else:
            edelliset = random.choice(self.ensimmaiset)
        sanat += edelliset
        return sanat

    def _muuta_merkkijonoksi(self, sanalista):
        """Muuttaa sanalistan merkkijonoksi eli valmiiksi lauseeksi.

        Args:
            sanalista: lauseeseen tulevat sanat.

        Returns:
            Lause merkkijonona.
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
        return
        # """Lukee tiedostoista lauseiden luomiseen tarvittavat sanalistat sekä
        # todennäköisyystaulukon.

        # Returns:
        #     4-tuple, jossa on kaksiulotteinen taulukko sanoista ja seuraavan
        # sanan todennäköisyyksistä, lista kaikista sanoista, lista sanoista,
        # jotka voivat aloittaa mietelauseen, sekä lista sanoista, jotka voivat
        # aloittaa toisen lauseen mietelauseen sisällä. Jos jonkin tieoston
        # lukeminen ei onnistunut, palautetaan Null.
        # """
        # try:
        #     with open(todennakoisyydet.csv) as todennakoisyydet:
        #         pass
        #     with open(sanalista.csv) as sanalista:
        #         pass
        #     with open(ensimmaiset.csv) as ensimmaiset:
        #         pass
        #     with open(jatkavat.csv) as jatkavat:
        #         pass
        # except:
        #     return
        # return (0, 0, 0, 0)
