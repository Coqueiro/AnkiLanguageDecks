import os
from urllib.request import urlretrieve


def create_resource_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def download_file(url, path):
    file_name = ("/tmp/" + path).split("/")[-1]
    full_path = path + "/" + file_name
    urlretrieve(url, full_path)
    return full_path
