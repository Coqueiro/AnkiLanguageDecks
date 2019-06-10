#!/usr/bin/env python

from helpers.frequency_list import FrequencyList

if __name__ == '__main__':
    print("Starting Anki Language Card Generation!")

    frequency_list_builder = FrequencyList(
        learn_language="es", quantity_of_words=4000)
    frequency_list_builder.get_list()
