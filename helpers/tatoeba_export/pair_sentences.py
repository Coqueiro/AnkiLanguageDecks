import csv
import os

from helpers.utils import create_resource_folder, decompress_file, download_file


class PairSentences:
    def __init__(self, base_lang, translate_lang, download=True):
        self.base_lang = base_lang
        self.translate_lang = translate_lang
        self.download = download
        self.sentences_url = "http://downloads.tatoeba.org/exports/sentences.tar.bz2"
        self.sentence_links_url = "http://downloads.tatoeba.org/exports/links.tar.bz2"
        self.sentences_with_audio_url = "http://downloads.tatoeba.org/exports/sentences_with_audio.tar.bz2"
        library_path = os.path.dirname(__file__)
        self.sentences_path = create_resource_folder(
            library_path + "/sentences")
        self.pairs_folder_path = create_resource_folder(
            library_path + "/pairs")

    def get_all_sentences_files(self):
        sentences_compressed = download_file(
            self.sentences_url, self.sentences_path, self.download)

        sentence_links_compressed = download_file(
            self.sentence_links_url, self.sentences_path, self.download)

        sentences_with_audio_compressed = download_file(
            self.sentences_with_audio_url, self.sentences_path, self.download)

        sentences_file_path = decompress_file(
            sentences_compressed, self.download)

        sentence_links_path = decompress_file(
            sentence_links_compressed, self.download)

        sentences_with_audio_path = decompress_file(
            sentences_with_audio_compressed, self.download)

        return sentences_file_path, sentence_links_path, sentences_with_audio_path

    def get_lang_sentences(self, sentences_file_path):
        base_sentences = {}
        translate_sentences = {}

        with open(sentences_file_path, 'r', encoding='utf-8') as sentence_file:
            sentence_file_reader = csv.reader(sentence_file, delimiter='\t')
            for row in sentence_file_reader:
                if row[1] == self.base_lang:
                    base_sentences[row[0]] = row[2]
                elif row[1] in self.translate_lang:
                    translate_sentences[row[0]] = row[2]

        return base_sentences, translate_sentences

    def get_sentence_pairs(self, sentence_links_path, base_sentences, translate_sentences):
        with open(sentence_links_path, 'r', encoding='utf-8') as links_file:
            sentence_pairs = []
            links_file_reader = csv.reader(links_file, delimiter='\t')
            for row in links_file_reader:
                if row[0] in base_sentences and row[1] in translate_sentences:
                    sentence_pairs.append([
                        row[0],
                        base_sentences[row[0]],
                        row[1],
                        translate_sentences[row[1]]
                    ])
        return sentence_pairs

    def create_sentence_pairs(self):
        sentences_file_path, sentence_links_path, sentences_with_audio_path = self.get_all_sentences_files()
        base_sentences, translate_sentences = self.get_lang_sentences(
            sentences_file_path)
        sentence_pairs = self.get_sentence_pairs(
            sentence_links_path, base_sentences, translate_sentences)

        pairs_path = self.pairs_folder_path + \
            f"/{self.base_lang}_to_{self.translate_lang}.csv"

        with open(pairs_path, "w") as pairs_file:
            pairs_file.writelines(
                '\t'.join(sentence_pair) + '\n' for sentence_pair in sentence_pairs)

        return pairs_path
