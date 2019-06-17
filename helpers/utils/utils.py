import os
import tarfile
from iso639 import languages
from urllib.request import urlretrieve


def create_resource_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def download_file(url, path, download=True):
    file_name = ("/tmp/" + url).split("/")[-1]
    full_path = path + "/" + file_name
    if download:
        urlretrieve(url, full_path)
    return full_path


def decompress_file(path, decompress=True):
    # Only implemented for bz2, returning respective csv file
    if decompress:
        tar = tarfile.open(path, "r:bz2")
        tar.extractall()
        tar.close()
    return path.split(".tar.")[0] + ".csv"


def get_language_code(code, iso):
    if code == "pt_br":
        code = "pt"
    lang = languages.get(alpha2=code)
    if iso == "639-2":
        return lang.terminology
