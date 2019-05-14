from flask_restful import Api
from flask import Flask
import os
from create_records import CreateRecords
from read_table import ReadTable
from update_table import UpdateTable
from delete_records import DeleteRecords

app = Flask(__name__)
api = Api(app)

api.add_resource(CreateRecords, '/api/create/<name>/<string:dob>')
api.add_resource(ReadTable, '/api/read')
api.add_resource(UpdateTable, '/api/update/<customer_id>/<name>/<string:dob>')
api.add_resource(DeleteRecords,'/api/delete/<customer_id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)