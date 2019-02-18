import click

from main.translater import YandexDictionary, parse_word_definitions


@click.command()
@click.option('--path_to_file', help='Absalute path to file')
def translate(path_to_file):
    with open(path_to_file) as file:
        dictionary = YandexDictionary()
        translated_data = dictionary.translate([line.strip()
                                                for line in file.readlines()
                                                if line != ''])
        processed_data = (parse_word_definitions(data) for data in translated_data)


if __name__ == '__main__':
    translate()
