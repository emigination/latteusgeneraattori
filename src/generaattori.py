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
        self.tiedostopolku = tiedostopolku
        self.trie = None
        self.ensimmaiset = None
        self.jatkavat = None
        self.tarkistustrie = None
        self._alusta()

    def _alusta(self):
        data = Sanalaskija(self.aste).opettele(self.tiedostopolku)
        self.trie = data[0]
        self.ensimmaiset = data[1]
        self.jatkavat = data[2]
        self.tarkistustrie = data[3]

    def generoi(self, aste=None, teema=None):
        """Luo lauseita Markovin ketjun avulla.

        Returns:
            Valmis mietelause merkkijonona.
        """
        if aste and aste!=self.aste:
            self.aste = aste
            self._alusta()
        ei_suoraan_aineistosta = False
        while not ei_suoraan_aineistosta:
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
            ei_suoraan_aineistosta = self._tarkista_lauseen_alkuperaisyys(lause)
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

    def _tarkista_lauseen_alkuperaisyys(self, lause):
        tarkistus = self.tarkistustrie.hae_seuraavat_sanat(lause)
        if tarkistus:
            return False
        return True
