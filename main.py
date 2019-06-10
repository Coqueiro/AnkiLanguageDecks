#!/usr/bin/env python

from helpers.frequency_list import FrequencyList

if __name__ == '__main__':
    print("Starting Anki Language Card Generation!")

    base_language = "Portuguese"
    learn_language = "Spanish"
    frequency_list_builder = FrequencyList(base_language, learn_language)
    frequency_list_builder.run()
