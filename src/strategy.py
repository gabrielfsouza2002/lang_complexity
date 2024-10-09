import random
import re
from abc import ABC, abstractmethod
from unit import ParseResult


class Strategy(ABC):
    @abstractmethod
    def execute(self, presult: ParseResult) -> str: ...


class Sameness(Strategy):
    def execute(self, presult: ParseResult) -> str:
        return presult.reconstruct()


class Deletion(Strategy):
    def __init__(self, percent: float, seed=None):
        super().__init__()
        self.percent = percent
        self.rng = random.Random(seed)

    def execute(self, presult: ParseResult) -> str:
        values = list(presult.index)
        sample = set(self.rng.sample(values, k=int(len(values) * self.percent)))
        output = presult.reconstruct(select=presult.index - sample)
        return output

class Replacement(Strategy):
    def __init__(self, seed=None):
        super().__init__()
        self.rng = random.Random(seed)

    def execute(self, presult: ParseResult) -> str:
        pseq = list(presult.iter())
        unique = list(set(pseq))
        self.rng.shuffle(unique)
        encode = {w: i for i, w in enumerate(unique)}
        output = "".join(
            list(
                map(
                    lambda c: "%010d" % encode[c] if c in encode else c,
                    presult.sequence,
                )
            )
        )
        return output


class RandomCharReplacementUnic(Strategy):
    def __init__(self, percent: float, seed=None):
        super().__init__()
        self.percent = percent
        self.rng = random.Random(seed)

    def execute(self, presult: ParseResult) -> str:
        chars = list(presult.sequence)
        non_space_indices = [i for i, char in enumerate(chars) if not char.isspace()]
        num_to_replace = int(len(non_space_indices) * self.percent)
        indices_to_replace = self.rng.sample(non_space_indices, num_to_replace)

        for idx in indices_to_replace:

            chars[idx] = '∑'

        return ''.join(chars)


class WordShuffle(Strategy):
    def __init__(self, seed=None):
        super().__init__()
        self.rng = random.Random(seed)

    def execute(self, presult: ParseResult) -> str:
        # Junta a sequência em uma string
        text = ''.join(presult.sequence)

        # Divide o texto em grupos usando os separadores como delimitadores, preservando espaços
        groups = re.split(r'([!?.]\s*)', text)

        result = []
        for group in groups:
            if re.match(r'[!?.]\s*', group):
                # Se o grupo é um separador (possivelmente seguido de espaços), adiciona-o diretamente
                result.append(group)
            else:
                # Se não, embaralha as palavras dentro do grupo, preservando espaços no início e fim
                leading_space = re.match(r'^\s+', group)
                trailing_space = re.search(r'\s+$', group)
                words = group.strip().split()
                self.rng.shuffle(words)
                shuffled_group = ' '.join(words)
                if leading_space:
                    shuffled_group = leading_space.group() + shuffled_group
                if trailing_space:
                    shuffled_group = shuffled_group + trailing_space.group()
                result.append(shuffled_group)

        # Junta todos os grupos
        return ''.join(result)