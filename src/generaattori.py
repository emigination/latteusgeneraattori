import random
from collections import deque
from sanalaskija import Sanalaskija


class Generaattori:
    """Luokka, joka luo lauseita triehen tallennettujen sanojen ja niiden
    esiintymistiheyksien perusteella.
    """

    def __init__(self, aste=2, tiedostopolku='data/opetusdata.txt'):
        """Luokan konstruktori, joka hakee tarvittavan datan tiedostoista tai
        niiden puuttuessa kutsuu sanalaskijan luomaan tarvittavan datan.
        """
        self.tiedostopolku = tiedostopolku
        self.aste = None
        self.trie = None
        self.ensimmaiset = None
        self.tarkistustrie = None
        self._alusta(aste)

    def _alusta(self, aste):
        self.aste = aste
        data = Sanalaskija(self.aste).opettele(self.tiedostopolku)
        if not data:
            return
        self.trie = data[0]
        self.ensimmaiset = data[1]
        self.tarkistustrie = data[2]

    def generoi(self, aste=None, teema=None, omaperaisyystarkistus=False):
        """Luo lauseita Markovin ketjun avulla. Lausetta jatketana pisteen
        jälkeenkin sitä todennäköisemmin, mitä lyhyempi lause on.

        Returns:
            Valmis mietelause merkkijonona.
        """
        if aste and aste != self.aste:
            self._alusta(aste)
        if not self.trie:
            return
        if teema:
            teema = teema[0].capitalize()+teema[1:]
        ei_suoraan_aineistosta = False
        while not ei_suoraan_aineistosta:
            sanat = self._valitse_aloitussanat(teema)
            edelliset = deque(sanat[len(sanat)-self.aste:])
            while len(sanat) < 20:
                seuraavat = self.trie.hae_seuraavat_sanat(list(edelliset))
                if not seuraavat:
                    if len(sanat) > 3 and sanat[len(sanat)-1][len(sanat[len(sanat)-1])-1] \
                            != ',' and random.random() < (0.1*len(sanat)):
                        break
                    while not seuraavat:
                        edelliset = deque(random.choice(self.ensimmaiset))
                        for sana in edelliset:
                            sanat.append(sana)
                        seuraavat = self.trie.hae_seuraavat_sanat(
                            list(edelliset))
                seuraava = self._arvo_seuraava(seuraavat)
                sanat.append(seuraava)
                edelliset.popleft()
                edelliset.append(seuraava)
            lause = self._muuta_merkkijonoksi(sanat)
            ei_suoraan_aineistosta = True
            if omaperaisyystarkistus:
                ei_suoraan_aineistosta = self._tarkista_lauseen_omaperaisyys(
                    lause)
        return lause

    def _valitse_aloitussanat(self, teema=None):
        """Valitsee lauseen aloittavat sanat teeman perusteella tai satunnaisesti.
        Args:
            teema : käyttäjän syöttämä teema, jos mitään.

        Returns:
            aloitussanat listana.
        """
        sanat = []
        if teema:
            if self.aste < 2:
                if self.trie.hae_seuraavat_sanat([teema]):
                    edelliset = [teema]
                else:
                    sanat.append(teema)
                    seuraavat_sanat = ["on", "on", "ei", "ei", "tulee", "odottaa", "voi", "tuntee",
                                       "tahtoo", "näkee"]
                    edelliset = [random.choice(seuraavat_sanat)]
            else:
                loytynyt = [
                    sanoja for sanoja in self.ensimmaiset if teema.lower()
                    in sanoja or teema in sanoja]
                if len(loytynyt) > 0:
                    edelliset = random.choice(loytynyt)
                else:
                    alkukirjaimet = [
                        kirjain for kirjain in self.trie.alkukirjaimet() if kirjain.islower()]
                    alkukirjain = random.choice(alkukirjaimet)
                    edelliset = [teema] + self.trie.hae_satunnainen(
                        alkukirjain).strip().split(' ')
        else:
            edelliset = random.choice(self.ensimmaiset)
        sanat += edelliset
        return sanat

    def _arvo_seuraava(self, seuraavat):
        """Valitse satunnaisesti seuraavan sanan niiden määrät huomioiden.

        Args:
            seuraavat: sanakirja, jossa on avaimina mahdolliset seuraavat sanat
            ja arvoina niiden määrät.

        Returns:
            valittu sana.
        """
        summa = 0
        for maara in seuraavat.values():
            summa += maara
        satunnainen = random.randint(0, summa)
        summa = 0
        for sana, maara in seuraavat.items():
            summa += maara
            if summa >= satunnainen:
                return sana

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

    def _tarkista_lauseen_omaperaisyys(self, lause):
        """Tarkistaa, esiintyykö generoitu latteus aineistossa sellaisenaan.

        Args:
            lause: generoitu lause merkkijonona.

        Returns:
            True, jos lausetta ei löydy aineistosta, muuten False.
        """
        tarkistus = self.tarkistustrie.hae_seuraavat_sanat([lause])
        if tarkistus and 'LOPPU' in tarkistus:
            return False
        return True
