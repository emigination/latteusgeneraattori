class Solmu:
    """Solmu käytettäväksi Triessä.
    """

    def __init__(self):
        """Lapset on sanakirja, johon tulee arvoiksi solmun lapsisolmut ja
        avaimiksi niitä vastaava kirjain.
        Sanat on sanakirja, johon tulee sisältöä vain jos solmu päättää jonkin
        sanayhdistelmän. Sanat ovat sanayhdistelmää seuraavat sanat ja niiden
        määrät.
        """
        self.lapset = {}
        self.sanat = {}
