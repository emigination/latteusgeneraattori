import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_lisays_onnistuu(self):
        self.trie.lisaa('sää', 2)
        self.assertEqual(self.trie.solmu['s']['ä']['ä']['indeksi'], 2)

    def test_indeksi_loytyy(self):
        self.trie.lisaa('papu', 0)
        self.trie.lisaa('kissa', 1)
        self.trie.lisaa('mörkö', 2)
        self.assertEqual(self.trie.hae_indeksi('mörkö'), 2)
