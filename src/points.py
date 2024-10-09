import csv
import unicodedata

def get_punctuation_separators(text):
    separators = {}
    for char in text:
        category = unicodedata.category(char)
        if category.startswith('P'):
            separators[char] = category
    return separators


def print_csv_separators(file_path):
    all_text = ""
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                all_text += ' '.join(row)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        return
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return

    separators = get_punctuation_separators(all_text)

    print("Separadores encontrados no arquivo CSV:")
    for separator, category in sorted(separators.items()):
        print(
            f"'{separator}' - Unicode: U+{ord(separator):04X} - Nome: {unicodedata.name(separator)} - Categoria: {category}")


if __name__ == "__main__":
    # Defina o caminho do seu arquivo CSV aqui
    csv_file_path = "../dataset/bibles_lcm.csv"
    print_csv_separators(csv_file_path)


