import click

from main.translater import YandexDictionary


@click.command()
@click.option('--path_to_file', help='Absalute path to file')
def translate(path_to_file):
    with open(path_to_file) as file:
        dictionary = YandexDictionary()
        result = dictionary.translate([line.strip()
                                      for line in file.readlines()
                                      if line != ''])
