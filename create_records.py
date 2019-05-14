from connect_postgres import connect, close
from flask_restful import Resource
from datetime import datetime

class CreateRecords(Resource):
    
    def get(self, name, dob):
        self.connection = connect()
        response = self.create(name, dob)
        close(self.connection)
        return response


    def create(self, name, dob):
        cursor = self.connection.cursor()
        postgres_insert_query = """ INSERT INTO customers (name, dob, updated_at) VALUES (%s,%s,%s)"""
        record_to_insert = (name, dob, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        cursor.execute(postgres_insert_query, record_to_insert)
        self.connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into customers table")
        return "Record inserted successfully into customers table"
    


