import os
import shutil

dir_path = "videos"
abs_dir_path = os.path.abspath(dir_path)


def init_container():
    if not os.path.exists(abs_dir_path):
        os.mkdir(abs_dir_path)
    else:
        shutil.rmtree(abs_dir_path)
