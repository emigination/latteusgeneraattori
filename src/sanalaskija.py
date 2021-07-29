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

    def opettele(self):
        """Käy opetusdatan läpi, luo listan sanoista, tallentaa sanat ja niiden indeksit trie-rakenteeseen ja laskee taulukon, jossa on todennäköisyydet millä mikäkin sana seuraa jotakin toista sanaa.

        Returns:
            4-tuple, jossa on kaksiulotteinen taulukko sanoista ja seuraavan sanan todennäköisyyksistä, lista kaikista sanoista, lista sanoista, jotka voivat aloittaa mietelauseen, sekä lista sanoista, jotka voivat aloittaa toisen lauseen mietelauseen sisällä.
        """
        trie = Trie()
        sanasanakirja = {}
        maarat = {}
        seuraavat = []
        data = self._lue_opetusdatatiedosto()
        for rivi in data:
            sanat = rivi.split(' ')
            edellinen = None
            for i, sana in enumerate(sanat):
                if sana not in sanasanakirja:
                    indeksi = len(self.sanalista)
                    sanasanakirja[sana] = indeksi
                    self.sanalista.append(sana)
                    seuraavat.append([])
                else:
                    indeksi = sanasanakirja[sana]
                if i==0:
                    self.ensimmaiset.append(indeksi)
                if edellinen:
                    seuraavat[edellinen].append(indeksi)
                    if self.sanalista[edellinen][len(self.sanalista[edellinen])-1] in ('.', '?', '!'):
                        self.jatkavat.append(indeksi)
                edellinen = indeksi
        self.todennakoisyydet = self._laske_todennakoisyydet(seuraavat)
        return (self.todennakoisyydet, self.sanalista, self.ensimmaiset, self.jatkavat)

    def _lue_opetusdatatiedosto(self):
        """Lukee opetusdatan ja luo siitä listan.

        Returns:
            Opetusdatan lauseet listana
        """
        with io.open('latteusgeneraattori/data/opetusdata.txt', encoding='utf-8') as tiedosto:
            data = []
            for rivi in tiedosto:
                rivi = rivi.replace("\n", "")
                data.append(rivi)
        return data

    def _laske_todennakoisyydet(self, seuraavat):
        """Luo sanoja seuraavien sanojen määrien perusteella todennäköisyystalukon.

        Args:
            seuraavat: lista listoja, joissa on kutakin sanaa seuraavien sanojen indeksit.

        Returns:
            kaksiuloitteinen taulukko todennäköisyyksiä, jossa rivi vastaa sanan indeksiä ja sarake sitä seuraavan sanan indeksiä.
        """
        sanoja = len(self.sanalista)
        todennakoisyydet = [[0 for i in range(sanoja)] for j in range(sanoja)]
        for i, sana in enumerate(seuraavat):
            for seuraava in sana:
                todennakoisyydet[i][seuraava] += 1/len(sana)
        return todennakoisyydet

    def _tallenna_tiedostoon(self):
        pass
