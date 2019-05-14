from connect_postgres import connect, close
from flask_restful import Resource
import json


class UpdateTable(Resource):
    def get(self, customer_id, name, dob):
        self.connection = connect()
        message = self.update(customer_id, name, dob)
        close(self.connection)
        return message

    def update(self, customer_id, name, dob):
        cursor = self.connection.cursor()
        # Update single record now
        sql_update_query = """Update customers set name = %s, dob=%s where id = %s"""
        cursor.execute(sql_update_query, (name, dob,  customer_id))
        self.connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")
        print("Table After updating record ")
        sql_select_query = """select * from customers where id = %s"""
        cursor.execute(sql_select_query, (customer_id))
        record = cursor.fetchone()
        return "Succesfully Updated"

