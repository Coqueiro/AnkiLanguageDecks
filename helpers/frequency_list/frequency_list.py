import os
from urllib.request import urlretrieve


class FrequencyList:
    def __init__(self, learn_language, quantity_of_words):
        self.learn_language = learn_language
        self.list_url = f"https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/{learn_language}/{learn_language}_50k.txt"
        self.quantity_of_words = quantity_of_words
        self.library_path = os.path.dirname(__file__)
        self.create_list_folders()

        self.full_list_file_path = os.path.join(
            self.full_lists_path, f"{self.learn_language}_50k.txt")

        self.list_file_path = os.path.join(
            self.lists_path, f"{self.learn_language}_{self.quantity_of_words}.txt"
        )

    def create_list_folders(self):
        self.full_lists_path = os.path.join(self.library_path, "full_lists")
        if not os.path.exists(self.full_lists_path):
            os.mkdir(self.full_lists_path)

        self.lists_path = os.path.join(self.library_path, "lists")
        if not os.path.exists(self.lists_path):
            os.mkdir(self.lists_path)

    def get_full_list(self):

        urlretrieve(self.list_url, self.full_list_file_path)

    def trim_list(self):
        words_left = self.quantity_of_words
        with open(self.full_list_file_path, mode="r") as full_list_file:
            with open(self.list_file_path, mode="w+") as list_file:
                for line in range(self.quantity_of_words):
                    list_file.write(
                        next(full_list_file).split(None, 1)[0] + "\n")

    def get_list(self):
        self.get_full_list()
        self.trim_list()
