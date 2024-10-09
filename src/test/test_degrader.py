import math
import unittest
import re
from test_NewDegrader import Degrader


class testDegrader(unittest.TestCase):

    def test_deletion_char(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        p = 0.1
        q = 1 - p
        d = Degrader.new("deletion", "chars", percent=p)
        o = d.degrade(s)

        len_degraded = len(o)
        len_expected = math.ceil(len(s) * q)

        self.assertEqual(len_degraded, len_expected)

    def test_deletion_lines(self):
        st = "abcdefghijklmnopqrstuvwxyz"
        s = "\n".join(st)
        p = 0.1
        q = 1 - p
        d = Degrader.new("deletion", "lines", percent=p)
        o = d.degrade(s)

        len_degraded = len(o)
        len_expected = len(s) - int(len(st) * p)
        self.assertEqual(len_degraded, len_expected)

    def test_deletion_word(self):
        s = " ".join("abcdefghijklmnopqrstuvwxyz")
        p = 0.1
        q = 1 - p
        d = Degrader.new("deletion", "words", percent=p)
        o = d.degrade(s)

        len_degraded = len(o.split())
        len_expected = math.ceil(len(s.split()) * q)
        self.assertEqual(len_degraded, len_expected)

    def test_replace_char(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        d = Degrader.new("replacement", "chars")
        o = d.degrade(s)

        len_degraded = len(o)
        len_expected = 10 * len(s)
        self.assertEqual(len_degraded, len_expected)

    def test_replace_word(self):
        s = " ".join("abcdefghijklmnopqrstuvwxyz")
        d = Degrader.new("replacement", "words")
        o = d.degrade(s)

        len_degraded = len(o.split())
        len_expected = len(s.split())
        self.assertEqual(len_degraded, len_expected)

    def test_replace_lines(self):
        s = "\n".join("abcdefghijklmnopqrstuvwxyz")
        d = Degrader.new("replacement", "lines")
        o = d.degrade(s)

        len_degraded = len(o.split("\n"))
        len_expected = len(s.split("\n"))
        self.assertEqual(len_degraded, len_expected)

    def test_sameness(self):
        s = "".join("abcdefghijklmnopqrstuvwxyz")
        d1 = Degrader.new("sameness", "chars")
        self.assertEqual(s, d1.degrade(s))

        s = " ".join("abcdefghijklmnopqrstuvwxyz")
        d2 = Degrader.new("sameness", "words")
        self.assertEqual(s, d2.degrade(s))

        s = "\n".join("abcdefghijklmnopqrstuvwxyz")
        d3 = Degrader.new("sameness", "lines")
        self.assertEqual(s, d3.degrade(s))

    def test_random_char_replacementUnic(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        p = 0.1
        d = Degrader.new("random_char_replacementUnic", "chars", percent=p)
        o = d.degrade(s)

        # Verifica se o comprimento da string não mudou
        self.assertEqual(len(o), len(s))

        # Verifica se a porcentagem de caracteres alterados está próxima do esperado
        changed_chars = sum(1 for a, b in zip(s, o) if a != b)
        expected_changes = int(len(s) * p)
        self.assertAlmostEqual(changed_chars, expected_changes, delta=1)

        # Verifica se todos os caracteres alterados são diferentes dos originais
        for a, b in zip(s, o):
            if a != b:
                self.assertNotEqual(a, b)

    def test_word_shuffle(self):
        s = "The quick brown fox jumps over the lazy dog"
        d = Degrader.new("word_shuffle", "words")
        o = d.degrade(s)

        # Verifica se o número de palavras não mudou
        self.assertEqual(len(o.split()), len(s.split()))

        # Verifica se todas as palavras originais estão presentes no resultado
        self.assertEqual(set(o.split()), set(s.split()))

        # Verifica se a ordem das palavras é diferente (a menos que por acaso seja igual)
        self.assertNotEqual(o, s)

    def test_word_shuffle_with_separators_and_spaces(self):
        s = "!Essa, string. É um exemplo de embaralhamento?! Quero que tudo esteja barulhento; mas voce... QUero que cale-se!?"
        d = Degrader.new("word_shuffle", "words", seed=42)
        o = d.degrade(s)

        # Verifica se os separadores e espaços estão na posição correta
        self.assertEqual(o[0], '!')
        self.assertIn('. ', o)  # Note o espaço após o ponto
        self.assertEqual(o[-1], '?')

        # Verifica se todas as palavras originais estão presentes
        original_words = set(re.findall(r'\w+', s))
        result_words = set(re.findall(r'\w+', o))
        self.assertEqual(original_words, result_words)

        # Verifica se a ordem das palavras é diferente (a menos que por acaso seja igual)
        self.assertNotEqual(s, o)

        # Verifica se o número de espaços é o mesmo
        self.assertEqual(s.count(' '), o.count(' '))


if __name__ == "__main__":
    unittest.main()
