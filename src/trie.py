class Trie:
    """Trie-tietorakenne sanojen ja niiden indeksien tallentamista varten.
    """

    def __init__(self):
        """Konstruktori, joka luo juureksi tyhjän sanakirjan.
        """
        self.solmu = {}

    def lisaa(self, sana, indeksi):
        """Lisää sanan ja sen indeksin triehen.

        Args:
            sana: lisättävä sana merkkijonona
            indeksi: sanan indeksi sanalistassa kokonaislukuna
        """
        solmu = self.solmu
        for kirjain in sana:
            if kirjain not in solmu:
                solmu[kirjain] = {}
            solmu = solmu[kirjain]
        solmu['indeksi'] = indeksi

    def hae_indeksi(self, sana):
        """Hakee triestä sanan indeksin.

        Args:
            sana: haettava sana merkkijonona.

        Returns:
            indeksi: sanan indeksi sanalistassa int-tyyppisenä.
        """
        solmu = self.solmu
        for kirjain in sana:
            solmu = solmu[kirjain]
        return solmu['indeksi']
