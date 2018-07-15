import json
import operator
import os
import subprocess
import uuid

from settings import abs_dir_path


class Video:

    def __init__(self, url):
        self.url = url
        self.info = None
        self.video_id = str(uuid.uuid4())

        if not os.path.exists(abs_dir_path):
            os.mkdir(abs_dir_path)

        self.video_folder_path = '{}/{}'.format(abs_dir_path, self.video_id)
        os.mkdir(self.video_folder_path)

    def get_video_id(self):
        return self.video_id

    def get_info(self):
        if self.info is None:
            output = subprocess.check_output(['you-get', self.url, '--json'])
            self.info = json.loads(output)
        return self.info

    def find_highest_resolution_format(self):
        info = self.get_info()
        streams = info.get('streams')

        size_dict = dict()
        for key, value in streams.items():
            size_dict[key] = value.get('size')

        highest_resolution_format = max(size_dict.items(), key=operator.itemgetter(1))

        (format, size) = highest_resolution_format
        return format

    def download(self):
        print('downloading to {}'.format(self.video_folder_path))
        try:
            output = subprocess.check_output(["you-get", "-o", self.video_folder_path, self.url])
            output_text = output.decode(encoding='utf-8')
            print(output_text)
        except subprocess.CalledProcessError as ex:
            print(ex)

    def download_highest_resolution(self):
        print('downloading highest resolution video to {}'.format(self.video_folder_path))
        format = self.find_highest_resolution_format()
        print(format)
        subprocess.call(["you-get", "--format", format, "-o", self.video_folder_path, self.url])

    def transfer_highest_resolution_to_youtube(self):
        title = self.info.get('title')
        self.download_highest_resolution()
        subprocess.call(["youtube-upload", "--title", title, "--description", title])

    def upload_to_youtube(self):
        pass
