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
        data = self.sanalaskija._lue_opetusdatatiedosto(self.opetusdata.name)
        self.assertEqual(data, ['Tämä on tekstiä.', 'Vähän lisää tekstiä.',
                         'Lorem ipsum dolor sit amet. Consectetur adipiscing elit.'])

    def test_aloitussanat_oikein(self):
        aloitussanat = self.sanalaskija.opettele(self.opetusdata.name)[1]
        self.assertEqual(
            aloitussanat, [['Tämä', 'on'], ['Vähän', 'lisää'], ['Lorem', 'ipsum'], ['Consectetur', 'adipiscing']])

    def test_trie_rakennettu_oikein(self):
        seuraavat = self.sanalaskija.opettele(self.opetusdata.name)[
            0].hae_seuraavat_sanat(['ipsum', 'dolor'])
        self.assertEqual(seuraavat, {'sit': 1})

    def test_trie_oikein_neljannella_asteella(self):
        uusisanalaskija = Sanalaskija(4)
        seuraavat = uusisanalaskija.opettele(self.opetusdata.name)[
            0].hae_seuraavat_sanat(['Lorem', 'ipsum', 'dolor', 'sit'])
        self.assertEqual(seuraavat, {'amet.': 1})

    def test_trie_pidempi_aineisto(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write(
                'Lorem ipsum dolor. Lorem ipsum agfsad. Lorem ipsum fsdgf. Lorem ipsum hhhh.')
        seuraavat = self.sanalaskija.opettele(self.opetusdata.name)[
            0].hae_seuraavat_sanat(['Lorem', 'ipsum'])
        self.assertIn('dolor.', seuraavat)
