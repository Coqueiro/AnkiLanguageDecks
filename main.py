#!/usr/bin/env python

from helpers.frequency_list import FrequencyList
from helpers.tatoeba_export import PairSentences

if __name__ == '__main__':
    print("Starting Anki Language Card Generation!")

    frequency_list_builder = FrequencyList(
        translate_lang="es", quantity_of_words=6000)
    frequency_list_builder.get_list()

    # pair_sentences = PairSentences("pt_br")
    # pair_sentences.hello_world()
