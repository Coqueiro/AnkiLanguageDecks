import os
import tarfile
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
