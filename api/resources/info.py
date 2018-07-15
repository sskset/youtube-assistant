import json
import subprocess

from flask_restful import Resource, reqparse


class Info(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type(str))
        data = parser.parse_args()

        url = data['url']

        info = subprocess.check_output(["you-get", url, "--json"])

        return {
                   'info': json.loads(info)
               }, 200
