from flask_restful import Resource, reqparse

from utilities.video import Video


class Download(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type(str))
        data = parser.parse_args()

        url = data['url']
        v = Video(url)
        v.download()

        return {
                   'url': '/download/{}'.format(v.get_video_id())
               }, 200


class DownloadHighestResolution(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type(str))
        data = parser.parse_args()

        url = data['url']

        v = Video(url)
        v.download_highest_resolution()

        return {
                   'url': '/download/{}'.format(v.get_video_id())
               }, 200
