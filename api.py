from flask_restful import Resource, Api
from flask import request, Flask
from helper import database_call, logger

app = Flask(__name__)
api = Api(app)


class req_info(Resource):
    def post(self):
        comp_id = request.form['ID']
        logger(str(request.environ['REMOTE_ADDR']), comp_id)
        return database_call(comp_id)


class get_my_ip(Resource):
    def get(self):
        return str(request.environ['REMOTE_ADDR'])


api.add_resource(req_info, '/req')
api.add_resource(get_my_ip, '/getmyip')

if __name__ == "__main__":
    app.run(host='192.168.43.204', port=8000, debug=True)
