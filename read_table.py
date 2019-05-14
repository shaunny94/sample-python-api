from connect_postgres import connect, close
from flask_restful import Resource
import json


class ReadTable(Resource):
    def get(self):
        self.connection = connect()
        self.read()
        close(self.connection)
        return self.data


    def read(self):
        cursor = self.connection.cursor()
        postgreSQL_select_Query = "select * from customers"
        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from customers table using cursor.fetchall")
        self.customer_records = cursor.fetchall()
        self.process_transactions() 
        print("Print each row and it's columns values")

    def process_transactions(self):
        self.data = {}
        for row in self.customer_records:
            print("Name = ", row[1], )
            print("DOB = ", row[2])
            print("Updated At  = ", row[3], "\n")
            row = list(row)
            row[2] = str(row[2])
            row[3] = str(row[3])
            self.data[row[0]] = row
            self.data[row[0]].pop(0)
        print(self.data)
       
       


