import unittest

from test_NewDegrader import *
from test_OldDegrader import *

seed = 42
rng = random.Random(seed)
percent = 0.1
texto = [
    "Primeiro     verso.\nSegundo verso.\nTerceiro verso.\nQuarto verso.",
    "Primeiro verso.\nSegundo verso.\nTerceiro verso.\nQuarto verso.",
    "Texto com TAB no começo e no final",
    "Texto com TAB no começo",
    "Texto com TAB no final",
    "Texto com 2 espaços  aqui no meio",
    "Texto com caractéres diversos @*(@#*(@# jijasdj 2#@#89822+-02><",
    "Texto     com  alguns     espaços",
    "Texto com quebras e espaços antes e depois e no meio.\n  Espaços Segundo verso.\n   Terceiro verso.\nQuarto verso."
]

# BUGANDO COM ESPAÇOS OU TABS NO COMEÇO OU NO FINAL

class MyTestCase(unittest.TestCase):
    def test_Verse_Remove(self):
        for i in range(len(texto)):
            self.assertEqual(testeVerseRemoverO(texto[i], rng, percent), testeVerseRemoverN(texto[i],seed, percent))

    def test_Word_Remove(self):
        for i in range(len(texto)):
            self.assertEqual(testeWordRemoverO(texto[i], rng, percent), testeWordRemoverN(texto[i], seed, percent))

    def test_Char_Remove(self):
        for i in range(len(texto)):
            self.assertEqual(testeCharRemoverO(texto[i], rng, percent), testeCharRemoverN(texto[i], seed, percent))

    def test_Word_to_Index(self):
        for i in range(len(texto)):
            self.assertEqual(testeWordToIndexO(texto[i], rng), testeWordToIndexN(texto[i], seed))

if __name__ == '__main__':
    unittest.main()
