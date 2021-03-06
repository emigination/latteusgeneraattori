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
                'Tämä on toinen teksti, niin myös tämä, ja vielä tämäkin.\n' +
                'Tämä on erilainen teksti. Tämä myös.\n' +
                'Tämä on neljäs teksti.\n')
        lause = Generaattori(1, self.opetusdata.name).generoi()
        self.assertGreater(len(lause), 20)

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
        lause = Generaattori(2, self.opetusdata.name).generoi()
        self.assertLess(len(lause), 240)

    def test_lause_noudattaa_markovin_ketjua(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write('Tämä on tekstiä.\nLorem ipsum dolor.')
        lause = Generaattori(2, self.opetusdata.name).generoi()
        self.assertIn(lause[:15], 'Tämä on tekstiä.\nLorem ipsum dolor.')

    def test_lause_jatkuu_pisteen_jalkeen(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write(
                'Tämä on tekstiä. Niin myös tämä.\n' +
                'Lorem ipsum dolor. Niin on.')
        lause = Generaattori(1, self.opetusdata.name).generoi()
        self.assertIn('. Niin', lause)

    def test_omaperaisyystarkistus_palauttaa_false(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write(
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
        generaattori = Generaattori(1, self.opetusdata.name)
        omaperaisyys = generaattori._tarkista_lauseen_omaperaisyys(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
        self.assertEqual(omaperaisyys, False)

    def test_omaperaisyystarkistus_palauttaa_true(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write(
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
        generaattori = Generaattori(1, self.opetusdata.name)
        omaperaisyys = generaattori._tarkista_lauseen_omaperaisyys(
            'Lorem elit.')
        self.assertEqual(omaperaisyys, True)

    def test_omaperaisyystarkistusta_kaytetaan(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write(
                'Tämä on tekstiä. Niin myös tämä.\n' +
                'Lorem ipsum dolor. Niin on.')
        lause = Generaattori(1, self.opetusdata.name).generoi(1, None, True)
        self.assertNotIn(
            lause, ('Tämä on tekstiä. Niin myös tämä.', 'Lorem ipsum dolor. Niin on.'))

    def test_lause_oikein_kun_teema_loytyy_triesta(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write('Tämä on tekstiä.\nLorem ipsum dolor.')
        lause = Generaattori(1, self.opetusdata.name).generoi(1, 'Tämä')
        self.assertIn('Tämä on tekstiä.', lause)

    def test_lause_oikein_kun_uusi_teema_1_aste(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write('Tämä on tekstiä.\nLorem ipsum dolor.\n' +
                           'Tämä ei ole kissa.\nKesä tulee joka vuosi.\nKissa pysyy jossain.' +
                           '\nJoku odottaa sitä.\nHuomenna voi sataa.\nJoku tuntee jotain.' +
                           'Koira tahtoo ulos.\nPöllö näkee pimeässä.')
        lause = Generaattori(1, self.opetusdata.name).generoi(1, 'T')
        self.assertIn(
            lause[:8], ['T on tek', 'T ei ole', 'T tulee ', 'T pysyy ', 'T odotta', 'T voi sa', 'T tuntee', 'T tahtoo', 'T näkee '])

    def test_lause_oikein_kun_teema_loytyy_2_aste(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write(
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n' +
                'Tämä on tekstiä, niin myös tämä, ja vielä tämäkin.')
        lause = Generaattori(2, self.opetusdata.name).generoi(2, 'ipsum')
        self.assertEqual(lause[:11], 'Lorem ipsum')

    def test_lause_oikein_kun_uusi_teema_2_aste(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write(
                'Lorem ipsum ipsum ipsum ipsum ipsum ipsum.\n' +
                'Tämä tekstiä tekstiä tekstiä tekstiä tekstiä.')
        lause = Generaattori(2, self.opetusdata.name).generoi(2, 'teema')
        self.assertIn(lause[:11], ('Teema ipsum', 'Teema tekst'))

    def test_asteen_vaihto_toimii(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write(
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
        generaattori = Generaattori(2, self.opetusdata.name)
        generaattori.generoi(1)
        self.assertEqual(generaattori.aste, 1)

    def test_lause_paattyy_pisteeseen(self):
        with open(self.opetusdata.name, mode='w') as tiedosto:
            tiedosto.write(
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit\n' +
                'Tämä on tekstiä, niin myös tämä, ja vielä tämäkin')
        lause = Generaattori(2, self.opetusdata.name).generoi()
        self.assertEqual(lause[len(lause)-1], '.')

    def test_virhe_tiedostonluvussa_ei_kaada(self):
        lause = Generaattori(1, 'tama/ei/ole/tiedosto.txt').generoi()
        self.assertEqual(lause, None)
