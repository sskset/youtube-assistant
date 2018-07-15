from flask_restful import Resource, reqparse

class Transfer(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url',type(str))

        data = parser.add_argument()

        url =data['url']
        return {

        },200