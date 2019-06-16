import os

from helpers.utils import create_resource_folder, download_file


class FrequencyList:
    def __init__(self, translate_lang, quantity_of_words):
        self.translate_lang = translate_lang
        self.translate_lang_file = f"{self.translate_lang}_50k.txt"
        self.list_url = f"https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/{translate_lang}/{self.translate_lang_file}"
        self.quantity_of_words = quantity_of_words
        self.library_path = os.path.dirname(__file__)

    def trim_list(self, full_list_file_path):
        self.list_file_path = os.path.join(
            self.lists_path, f"{self.translate_lang}_{self.quantity_of_words}.txt"
        )
        words_left = self.quantity_of_words
        with open(full_list_file_path, mode="r") as full_list_file:
            with open(self.list_file_path, mode="w+") as list_file:
                for line in range(self.quantity_of_words):
                    list_file.write(
                        next(full_list_file).split(None, 1)[0] + "\n")

    def get_list(self):
        self.full_lists_path = create_resource_folder(
            self.library_path + "/full_lists")
        self.lists_path = create_resource_folder(self.library_path + "/lists")

        full_list_file_path = download_file(
            self.list_url, self.full_lists_path)
        self.trim_list(full_list_file_path)
