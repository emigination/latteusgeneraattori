import io
from collections import deque
from trie import Trie


class Sanalaskija:
    """Luokka, joka lukee opetusdatan, laskee sanojen esiintymiset ja tallentaa
    ne triehen.
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
            tiedostopolku: polku, josta luettevat lauseet haetaan.

        Returns:
            3-tuple, jossa sanat trie-rakenteessa, virkkeen aloittavien
            sanojen lista ja tarkistustrie sen tarkistamiseksi, ettei generoitava
            lause ole suoraan aineistosta..
        """
        data = self._lue_opetusdatatiedosto(tiedostopolku)
        tulos = self._laske_sanat(data)
        return tulos

    def _lue_opetusdatatiedosto(self, tiedostopolku):
        """Lukee opetusdatan ja luo siitä listan.

        Args:
            tiedostopolku: polku, josta luettevat lauseet haetaan.

        Returns:
            Opetusdatan rivit listana.
        """
        with io.open(tiedostopolku, encoding='utf-8') as tiedosto:
            data = []
            for rivi in tiedosto:
                rivi = rivi.replace("\n", "")
                data.append(rivi)
        return data

    def _laske_sanat(self, data):
        """Käy opetusdatan läpi, tallentaa "asteen" pituiset sanayhdistelmät ja
        niitä seuraavat sanat määrineen triehen ja listaa sanayhdistelmät, jotka
        voivat aloittaa virkkeen.

        Args:
            data: opetusdata listana lauseita.

        Returns:
            trie: trie-tietorakenne, jossa on tieto sanojen seuraajista ja niiden määristä.
            ensimmaiset: virkkeen aloittavien sanojen lista.
            tarkistustrie: trie, jossa on jokainen aineiston rivi yksi kerrallaan,
            jotta voidaan tarkistaa ettei generoitava lause ole täysin sama kuin mikään niistä.
        """
        trie = Trie()
        ensimmaiset = []
        tarkistustrie = Trie()
        for rivi in data:
            sanat = rivi.split(' ')
            ensimmaiset.append(sanat[:self.aste])
            edelliset = deque([])
            for i, sana in enumerate(sanat):
                if len(edelliset) >= self.aste:
                    trie.lisaa(list(edelliset), sana)
                    edelliset.popleft()
                    if sana[len(sana)-1] in ('.', '?', '!') and len(sanat) > i+self.aste:
                        edelliset = deque([])
                        ensimmaiset.append(sanat[i+1:i+self.aste+1])
                edelliset.append(sana)
            tarkistustrie.lisaa([rivi], 'LOPPU')
        return (trie, ensimmaiset, tarkistustrie)
