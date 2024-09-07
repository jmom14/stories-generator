import os


def remove_file_async(filename):
    if os.path.exists(filename):
        os.remove(filename)
