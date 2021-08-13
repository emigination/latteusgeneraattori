import io
from collections import deque
from trie import Trie


class Sanalaskija:
    """Luokka, joka lukee opetusdatan ja laskee kullekin sanalle seuraavan sanan todennäköisyydet.
    """

    def __init__(self, aste=2):
        self.aste = aste

    def opettele(self, tiedostopolku):
        """Luo opetusdatasta generaattorin tarvitsemat tietorakenteet.

        Returns:
            4-tuple, jossa on kaksiulotteinen taulukko sanoista ja seuraavan sanan todennäköisyyksistä, lista kaikista sanoista, lista sanoista, jotka voivat aloittaa mietelauseen, sekä lista sanoista, jotka voivat aloittaa toisen lauseen mietelauseen sisällä.
        """
        data = self._lue_opetusdatatiedosto(tiedostopolku)
        tulos = self._laske_sanat(data)
        return(tulos)

    def _lue_opetusdatatiedosto(self, tiedostopolku):
        """Lukee opetusdatan ja luo siitä listan.

        Returns:
            Opetusdatan lauseet listana
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
            seuraaavat: lista listoja, joka kertoo mitkä sanat seuraavat mitäkin sanaa. Sanat on tallennettu indekseinä.
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

    def _laske_todennakoisyydet(self, seuraavat, sanoja):
        """Luo sanoja seuraavien sanojen määrien perusteella todennäköisyystalukon.

        Args:
            seuraavat: lista listoja, joissa on kutakin sanaa seuraavien sanojen indeksit
            sanoja: eri sanojen määrä aineistossa

        Returns:
            kaksiuloitteinen taulukko todennäköisyyksiä, jossa rivi vastaa sanan indeksiä ja sarake sitä seuraavan sanan indeksiä.
        """
        todennakoisyydet = [[0 for i in range(sanoja)] for j in range(sanoja)]
        for i, sana in enumerate(seuraavat):
            for seuraava in sana:
                todennakoisyydet[i][seuraava] += 1/len(sana)
        return todennakoisyydet

    def _tallenna_tiedostoon(self):
        pass
