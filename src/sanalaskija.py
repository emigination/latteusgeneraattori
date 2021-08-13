import io
from collections import deque
from trie import Trie


class Sanalaskija:
    """Luokka, joka lukee opetusdatan ja laskee kullekin sanalle seuraavan sanan todennäköisyydet.
    """

    def __init__(self, aste=2):
        """Konstruktori, jossa asetetaan käytettävien Markovin ketjujen aste.

        Args:
            aste: kokonaisluku, oletuksena 2.
        """
        self.aste = aste

    def opettele(self, tiedostopolku):
        """Luo opetusdatasta generaattorin tarvitsemat tietorakenteet.

        Args:
            tiedostopolku: polku, josta luettevat lauseet haetaan

        Returns:
            3-tuple, jossa sanat trie-rakenteessa, mietelauseen aloittavien sanojen joukko ja pisteen jälkeen mietelausetta jatkavien sanojen joukko.
        """
        data = self._lue_opetusdatatiedosto(tiedostopolku)
        tulos = self._laske_sanat(data)
        return(tulos)

    def _lue_opetusdatatiedosto(self, tiedostopolku):
        """Lukee opetusdatan ja luo siitä listan.

        Args:
            tiedostopolku: polku, josta luettevat lauseet haetaan

        Returns:
            opetusdatan lauseet listana.
        """
        with io.open(tiedostopolku, encoding='utf-8') as tiedosto:
            data = []
            for rivi in tiedosto:
                rivi = rivi.replace("\n", "")
                data.append(rivi)
        return data

    def _laske_sanat(self, data):
        """Käy opetusdatan läpi, luo listan sanoista, tallentaa sanat ja niiden indeksit trie-rakenteeseen ja listaa kutakin sanaa seuraavat sanat.

        Args:
            data: opetusdata listana lauseita

        Returns:
            trie: trie-tietorakenne, jossa on tieto sanojen seuraajista ja niiden määristä
            ensimmaiset: mietelauseen aloittavien sanojen joukko
            jatkavat: pisteen jälkeen mietelausetta jatkavien sanojen joukko.
        """
        trie = Trie()
        ensimmaiset = set()
        jatkavat = set()
        for rivi in data:
            sanat = rivi.split(' ')
            ensimmaiset.add(sanat[0])
            edelliset = deque([])
            for i, sana in enumerate(sanat):
                if i >= self.aste:
                    trie.lisaa(edelliset, sana)
                    edelliset.popleft()
                if len(edelliset) > 0:
                    edellinen = edelliset[len(edelliset)-1]
                    if edellinen[len(edellinen)-1] in ('.', '?', '!'):
                        jatkavat.add(sana)
                edelliset.append(sana)
        return (trie, ensimmaiset, jatkavat)

    def _tallenna_tiedostoon(self):
        pass
