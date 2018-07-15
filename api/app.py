from flask import Flask
from flask_restful import Api

from resources.download import Download, DownloadHighestResolution
from resources.info import Info

app = Flask(__name__)
api = Api(app, prefix='/api')
dir_path = "videos"

api.add_resource(Download, '/download')
api.add_resource(DownloadHighestResolution, '/download_highest_resolution')
api.add_resource(Info, '/info')

if __name__ == '__main__':
    from settings import init_container

    init_container()

    app.run(debug=True, host='0.0.0.0', port=5000)
