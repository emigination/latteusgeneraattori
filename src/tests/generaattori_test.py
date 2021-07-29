import unittest
from tempfile import NamedTemporaryFile
from generaattori import Generaattori


class TestGeneraattori(unittest.TestCase):

    def setUp(self):
        self.opetusdata = NamedTemporaryFile()

    def test_lause_tarpeeksi_pitka(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write('Tämä on tekstiä, niin myös tämä, ja vielä tämäkin.\nLorem ipsum dolor sit amet, consectetur adipiscing elit.')
        generaattori = Generaattori(self.opetusdata.name)
        self.assertGreater(len(generaattori.generoi()), 30)

    def test_lause_noudattaa_markovin_ketjua(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write('Tämä on tekstiä.\nLorem ipsum.')
        generaattori = Generaattori(self.opetusdata.name)
        self.assertIn(generaattori.generoi(), ('Tämä on tekstiä.', 'Lorem ipsum.'))
