import os
import json
import requests


class YandexDictionaryException(Exception):

    """
    Default YandexDictionary exception
    """
    error_codes = {
        401: "ERR_KEY_INVALID",
        402: "ERR_KEY_BLOCKED",
        403: "ERR_DAILY_REQ_LIMIT_EXCEEDED",
        404: "ERR_DAILY_CHAR_LIMIT_EXCEEDED",
        413: "ERR_TEXT_TOO_LONG",
        422: "ERR_UNPROCESSABLE_TEXT",
        501: "ERR_LANG_NOT_SUPPORTED",
        503: "ERR_SERVICE_NOT_AVAIBLE",
    }

    def __init__(self, status_code, *args, **kwargs):
        super(YandexDictionaryException, self).__init__(
            self.error_codes.get(status_code), *args, **kwargs)


class YandexDictionary:
    api_url = "https://dictionary.yandex.net/api/"\
              "{version}/dicservice.json/{endpoint}"
    YANDEX_DICTIONARY_API_KEY = os.getenv('YANDEX_DICTIONARY_API_KEY')

    def __init__(self, api_version=None, api_endpoints=None):
        if not self.YANDEX_DICTIONARY_API_KEY:
            raise ValueError('Yandex dictionay key is not set into env. ')
        self.api_version = api_version or 'v1'
        self.api_endpoints = api_endpoints or \
            {"langs": "getLangs", "lookup": "lookup"}

    def make_url(self, endpoint):
        return self.api_url.format(version=self.api_version,
                                   endpoint=endpoint)

    def is_translate_available_for_languages(self, languages):
        response = requests.get(self.make_url(self.api_endpoints['langs']),
                                params={'key': self.YANDEX_DICTIONARY_API_KEY})
        if response.status_code != 200:
            raise YandexDictionaryException(status_code)
        return languages in json.loads(response.text)

    def translate(self, words, lang='en-ru'):
        return (self.lookup(word, lang) for word in words)

    def lookup(self, word, lang='en-ru'):
        response = requests.get(self.make_url(self.api_endpoints['lookup']),
                                params={'key': self.YANDEX_DICTIONARY_API_KEY,
                                        'lang': lang,
                                        'text': word}
                                )

        if response.status_code != 200:
            print('Data is empty. ')
            return dict()
        result = json.loads(response.text)
        if 'def' not in result:
            return dict()
        return result['def']


def parse_word_definitions(word_definitions):
    text = word_definition['text']


def word_definition_mapper(word_definition):
    text = word_definition['text']
    transcription = word_definition['ts']
    values = ((value['pos'], value['text']) for value in word_definition['tr'])
    return (text, transcription, values)
