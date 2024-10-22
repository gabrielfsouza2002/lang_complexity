import src.unit as U
import src.strategy as S

class Degrader:
    __strategies = {
        "deletion": S.Deletion,
        "replacement": S.Replacement,
        "sameness": S.Sameness,
        "random_char_replacementUnic": S.RandomCharReplacementUnic,
        "random_word_replacementUnic": S.RandomWordReplacementUnic,
        "word_shuffle": S.WordShuffle,
    }
    __units = {
        "chars": U.Chars(),
        "words": U.NotChar(r"\s"),
        "lines": U.NotChar("\n"),
    }

    def __init__(self, strategy: S.Strategy, unit: U.UnitParser):
        self.unit = unit
        self.strategy = strategy

    @classmethod
    def new(cls, strategy: str, unit: str, **strategy_arguments):
        unit = cls.__units[unit]
        strategy = cls.__strategies[strategy](**strategy_arguments)
        return cls(strategy, unit)

    def degrade(self, text: str) -> str:
        presult = self.unit.parse(text)
        #print(presult)
        output = self.strategy.execute(presult)
        return output


# TESTES COD NOVO
#TESTE 1: Remoção de versos por quebras de linha
texto1 = "Primeiro verso.\nSegundo verso.\nTerceiro verso.\nQuarto verso."
def testeVerseRemoverN(text, seed, percent):
    deletion_strategy = S.Deletion(percent=percent, seed=seed)
    unit_lines = U.NotChar("\n")
    verse_remover = Degrader(deletion_strategy, unit_lines)
    result = verse_remover.degrade(text)
    return result

#TESTE 2 Remove palavras aleatóriamente
texto2 = "Este\n é um exemplo! Texto com várias palavras para remover   aleatoriamente. A vida é bela, só na usp que não. Acaba logo!"
def testeWordRemoverN(text, seed, percent):
    deletion_strategy = S.Deletion(percent=percent, seed=seed)
    unit_words = U.NotChar(r"\s")
    word_remover = Degrader(deletion_strategy, unit_words)
    result = word_remover.degrade(text)
    return result

#TESTE 3 Remove caracteres aleatóriamente
texto3 = "Texto com caracteres diversos, incluindo   espaços e pontuação!"
def testeCharRemoverN(text, seed, percent):
    deletion_strategy = S.Deletion(percent=percent, seed=seed)
    unit_chars = U.Chars()
    char_remover = Degrader(deletion_strategy, unit_chars)
    result = char_remover.degrade(text)
    return result

# Teste 4: Substituição de Palavras por Índices Aleatórios
texto4 = "Transforme cada palavra em um índice aleatório."
def testeWordToIndexN(text, seed):
    replacement_strategy = S.Replacement(seed=seed)
    unit_words = U.NotChar(r"\s")
    word_to_index = Degrader(replacement_strategy, unit_words)
    result = word_to_index.degrade(text)
    return result

# Teste 5: Substituição de Caracteres Aleatórios por Unicode
texto5 = "Este é um texto para testar a substituição de caracteres por Unicode."
def testeRandomCharReplacementUnicN(text, seed, percent):
    random_char_replacement_strategy = S.RandomCharReplacementUnic(percent=percent, seed=seed)
    unit_chars = U.Chars()
    char_replacer = Degrader(random_char_replacement_strategy, unit_chars)
    result = char_replacer.degrade(text)
    return result

# Teste 6: Substituição de Palavras Aleatórias por Unicode
texto6 = "Este é um exemplo de substituição de palavras por Unicode."
def testeWordReplacementUnicN(text, seed, percent):
    word_replacement_unic_strategy = S.RandomWordReplacementUnic(percent=percent, seed=seed)
    unit_words = U.NotChar(r"\s")
    word_replacer = Degrader(word_replacement_unic_strategy, unit_words)
    result = word_replacer.degrade(text)
    return result

# Teste 7: Embaralhamento de Palavras
texto7 = "!Essas, string. É um exemplo de embaralhamento?! Quero que tudo esteja barulhento; mas então voce de um jeito... Testar separadores é muito importe » pois assim faremos um bom trabalho—Pelo menos eu espero que sim. "
def testeWordShuffleN(text, seed):
    word_shuffle_strategy = S.WordShuffle(seed=seed)
    unit_words = U.NotChar(r"\s")
    word_shuffler = Degrader(word_shuffle_strategy, unit_words)
    result = word_shuffler.degrade(text)
    return result


seed = 43
percent = 0.5
#print(testeVerseRemoverN(texto1, seed, percent))
#print(testeWordRemoverN(texto2, seed, percent))
#print(testeCharRemoverN(texto3, seed, percent))
#print(testeWordToIndexN(texto4, seed))
#print(testeRandomCharReplacementUnicN(texto5, seed, percent))
print(testeWordReplacementUnicN(texto6, seed, percent))
#print(testeWordShuffleN(texto7, seed))
