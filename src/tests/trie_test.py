import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_lisays_onnistuu(self):
        self.trie.lisaa(['a', 'b'], 'kissa')
        self.assertEqual(
            self.trie.juuri.lapset['a'].lapset[' '].lapset['b'].lapset[' '].sanat, {'kissa': 1})

    def test_seuraavat_sanat_loytyvat(self):
        self.trie.lisaa(['sää', 'on'], 'hyvä')
        self.trie.lisaa(['sää', 'on'], 'synkkä')
        seuraavat = self.trie.hae_seuraavat_sanat(['sää', 'on'])
        self.assertEqual(seuraavat, {'hyvä': 1, 'synkkä': 1})

    def test_maarat_oikein(self):
        self.trie.lisaa(['hauki', 'on'], 'kala')
        self.trie.lisaa(['hauki', 'on'], 'kala')
        self.trie.lisaa(['hauki', 'on'], 'eläin')
        maara = self.trie.hae_seuraavat_sanat(['hauki', 'on'])['kala']
        self.assertEqual(maara, 2)

    def test_kolmas_aste_toimii(self):
        self.trie.lisaa(['hauki', 'on', 'kala'], 'joka')
        self.trie.lisaa(['hauki', 'on', 'kala'], 'joka')
        maara = self.trie.hae_seuraavat_sanat(['hauki', 'on', 'kala'])['joka']
        self.assertEqual(maara, 2)
