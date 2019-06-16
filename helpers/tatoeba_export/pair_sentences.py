import os

from helpers.utils import create_resource_folder, download_file


class PairSentences:
    def __init__(self, base_lang, translate_lang):
        self.base_lang = base_lang
        self.translate_lang = translate_lang
        self.sentences_url = "http://downloads.tatoeba.org/exports/sentences.tar.bz2"
        self.sentence_links_url = "http://downloads.tatoeba.org/exports/links.tar.bz2"
        self.sentences_with_audio_url = "http://downloads.tatoeba.org/exports/sentences_with_audio.tar.bz2"
        library_path = os.path.dirname(__file__)
        self.sentences_path = self.create_resource_folder(
            library_path + "/sentences")
