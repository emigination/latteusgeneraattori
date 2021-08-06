import unittest
from tempfile import NamedTemporaryFile
from generaattori import Generaattori


class TestGeneraattori(unittest.TestCase):

    def setUp(self):
        self.opetusdata = NamedTemporaryFile()

    def test_lause_tarpeeksi_pitka(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write(
                'Tämä on tekstiä, niin myös tämä, ja vielä tämäkin.\n' +
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
        generaattori = Generaattori(self.opetusdata.name)
        self.assertGreater(len(generaattori.generoi()), 30)

    def test_lause_tarpeeksi_lyhyt(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write(
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' +
                'Mauris porttitor a mi eu feugiat. Etiam rhoncus faucibus ' +
                'pulvinar. Quisque porta, ligula vel egestas pharetra, diam ' +
                'felis venenatis libero, id aliquam leo nunc a nunc. Mauris ' +
                'accumsan lacus sit amet lorem faucibus mattis. Maecenas ' +
                'egestas facilisis feugiat. Ut vel malesuada dolor, a ' +
                'malesuada lacus. Integer sit amet eros lorem. Maecenas ' +
                'elementum, ipsum eu tempus pharetra, elit dolor commodo ' +
                'leo, quis suscipit.\n' +
                'At four in the morning wake up owner meeeeeeooww scratch at ' +
                'legs and beg for food then cry and yowl until they wake up ' +
                'at two pm jump on window and sleep while observing the ' +
                'bootyful cat next door that u really like but who already ' +
                'has a boyfriend end up making babies with her and let her ' +
                'move in demand to have some of whatever the human is ' +
                'cooking, then sniff the offering and walk away yet pushes ' +
                'butt to face for cat sit like bread.')
        generaattori = Generaattori(self.opetusdata.name)
        self.assertLess(len(generaattori.generoi()), 240)

    def test_lause_noudattaa_markovin_ketjua(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write('Tämä on tekstiä.\nLorem ipsum.')
        generaattori = Generaattori(self.opetusdata.name)
        self.assertIn(generaattori.generoi(),
                      ('Tämä on tekstiä.', 'Lorem ipsum.'))

    def test_lause_jatkuu_vaikkei_seuraavaa_sanaa_datassa(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write('Tekstiä. Sana.\nLorem ipsum.')
        generaattori = Generaattori(self.opetusdata.name)
        self.assertIn('Sana.', generaattori.generoi())
