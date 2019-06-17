#!/usr/bin/env python
from helpers.frequency_list import FrequencyList
from helpers.tatoeba_export import PairSentences
from helpers.utils import get_language_code

if __name__ == '__main__':
    print("Starting Anki Language Card Generation!")

    base_lang = "pt_br"
    translate_lang = "es"

    frequency_list_builder = FrequencyList(
        translate_lang, quantity_of_words=6000)
    frequency_list_builder.get_list()

    pair_sentences = PairSentences(
        get_language_code(base_lang, "639-2"),
        get_language_code(translate_lang, "639-2"),
        download=False)
    pairs_path = pair_sentences.create_sentence_pairs()
