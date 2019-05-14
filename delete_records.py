from connect_postgres import connect, close
from flask_restful import Resource
import json

class DeleteRecords(Resource):


    def get(self, customer_id):
        self.connection = connect()
        message = self.delete(self.connection, customer_id)
        close(self.connection)
        return message


    def delete(self, connection, customer_id):
        
        cursor = self.connection.cursor()
        # Update single record now
        sql_delete_query = """Delete from customers where id = %s"""
        cursor.execute(sql_delete_query, customer_id )
        self.connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully")
        return "Record deleted successfully"