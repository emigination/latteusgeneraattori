import unittest
from tempfile import NamedTemporaryFile
from sanalaskija import Sanalaskija


class TestSanalaskija(unittest.TestCase):

    def setUp(self):
        self.sanalaskija = Sanalaskija()
        self.opetusdata = NamedTemporaryFile()
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write(
                'Tämä on tekstiä.\nVähän lisää tekstiä.\nLorem ipsum dolor sit amet. Consectetur adipiscing elit.')

    def test_lue_opetusdata(self):
        self.assertEqual(self.sanalaskija._lue_opetusdatatiedosto(self.opetusdata.name), [
                         'Tämä on tekstiä.', 'Vähän lisää tekstiä.', 'Lorem ipsum dolor sit amet. Consectetur adipiscing elit.'])

    def test_seuraavien_sanojen_lista(self):
        seuraavaat = self.sanalaskija._laske_sanat(
            ['Tämä on tekstiä.', 'Niin on tämäkin.', 'Lorem ipsum dolor sit amet.'])
        self.assertEqual(seuraavaat, [[1], [2, 4], [], [
                         1], [], [6], [7], [8], [9], []])

    def test_todennakoisyydet_oikein(self):
        todennakoisyydet = self.sanalaskija._laske_todennakoisyydet(
            [[1, 2], [2, 2, 0, 2], [1]], 3)
        self.assertEqual(todennakoisyydet, [
                         [0, 0.5, 0.5], [0.25, 0, 0.75], [0, 1, 0]])

    def test_aloitussanat_oikein(self):
        aloitussanat = self.sanalaskija.opettele(self.opetusdata.name)[2]
        self.assertEqual(aloitussanat, [0, 3, 5])

    def test_jatkavat_sanat_oikein(self):
        jatkavat_sanat = self.sanalaskija.opettele(self.opetusdata.name)[3]
        self.assertEqual(jatkavat_sanat, [10])
