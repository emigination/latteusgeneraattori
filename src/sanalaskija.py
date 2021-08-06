import io
from trie import Trie


class Sanalaskija:
    """Luokka, joka lukee opetusdatan ja laskee kullekin sanalle seuraavan sanan todennäköisyydet.
    """

    def __init__(self):
        self.sanalista = []
        self.ensimmaiset = []
        self.jatkavat = []
        self.todennakoisyydet = []

    def opettele(self, tiedostopolku):
        """Luo opetusdatasta generaattorin tarvitsemat tietorakenteet.

        Returns:
            4-tuple, jossa on kaksiulotteinen taulukko sanoista ja seuraavan sanan todennäköisyyksistä, lista kaikista sanoista, lista sanoista, jotka voivat aloittaa mietelauseen, sekä lista sanoista, jotka voivat aloittaa toisen lauseen mietelauseen sisällä.
        """
        data = self._lue_opetusdatatiedosto(tiedostopolku)
        seuraavat = self._laske_sanat(data)
        self.todennakoisyydet = self._laske_todennakoisyydet(
            seuraavat, len(self.sanalista))
        return (self.todennakoisyydet, self.sanalista, self.ensimmaiset, self.jatkavat)

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
        sanasetti = set()
        seuraavat = []
        for rivi in data:
            sanat = rivi.split(' ')
            edellinen = -1
            for i, sana in enumerate(sanat):
                if sana not in sanasetti:
                    indeksi = len(self.sanalista)
                    trie.lisaa(sana, indeksi)
                    self.sanalista.append(sana)
                    seuraavat.append([])
                    sanasetti.add(sana)
                else:
                    indeksi = trie.hae_indeksi(sana)
                if i == 0:
                    self.ensimmaiset.append(indeksi)
                if edellinen > -1:
                    seuraavat[edellinen].append(indeksi)
                    if self.sanalista[edellinen][len(self.sanalista[edellinen])-1] in ('.', '?', '!'):
                        self.jatkavat.append(indeksi)
                edellinen = indeksi
        return seuraavat

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
