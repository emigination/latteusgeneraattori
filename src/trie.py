from solmu import Solmu


class Trie:
    """Trie-tietorakenne sanojen ja niiden indeksien tallentamista varten.
    """

    def __init__(self):
        """Konstruktori, joka luo juureksi tyhjän sanakirjan.
        """
        self.juuri = Solmu()

    def lisaa(self, edelliset, seuraavasana):
        """Lisää 'asteen' pituisen sanajonon ja sitä seuraavan sanan triehen.

        Args:
            edelliset: 'asteen' määrä sanoja
            sana: niitä seuraava sana.
        """
        solmu = self.juuri
        for sana in edelliset:
            sana += ' '
            for kirjain in sana:
                if kirjain not in solmu.lapset:
                    solmu.lapset[kirjain] = Solmu()
                solmu = solmu.lapset[kirjain]
        if seuraavasana not in solmu.sanat:
            solmu.sanat[seuraavasana] = 1
        else:
            solmu.sanat[seuraavasana] += 1

    def hae_seuraavat_sanat(self, sanajono):
        """Hakee annettua sanajonoa seuraavat sanat ja niiden määrät sanajonon seuraajana.

        Args:
            sanajono: lista sanoista, joiden seuraajia haetaan.

        Returns:
            sanakirja, jossa on avaimina mahdolliset seuraavat sanat ja arvoina niiden määrät.
        """
        solmu = self.juuri
        for sana in sanajono:
            sana += ' '
            for kirjain in sana:
                if kirjain not in solmu.lapset:
                    return None
                solmu = solmu.lapset[kirjain]
        return solmu.sanat
