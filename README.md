# Backend Assignment
The aim is to create a backend api to perform CRUD operations for a customer table



# Structure
[sample-python-api]
|
|___ connect_postgres.py
|____ create_customer_model.sql  # SQL to find youngest is here
|___ create_records.py
|___ delete_records.py   
|___ main.py            # Main function is executed here
|___ read_table.py
|___README.md
|___ requirements.txt    # Dependencies are kept here
|___ update_table.py




# Step 1:
Create a python virtual environment using command shown below

```
python -m venv env
```

# Step 2:
Activate virtual environment using command shown below
```
env/Scripts/activate.ps1   # For Visual Studio Code IDE
           /activate.sh    # Unix-based Systems
```

# Step 3:
Downlaod dependencies necessary for project
```
  pip install -r requirements.txt

```


# Step 3:
Create a postgres database with the following configuration:
```
dbname=postgres user=postgres password=admin

```


# Step 3:
Create a customer model table for postgres. 
```
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name text, 
    dob date, 
    updated_at timestamp
);

```

# Step 4:
Go into the sample-python-api directory and run the main function with the following command

```
python  main.py

```




# Step 5a:

This application has four endpoints: 

```
   http://localhost:8000/create/<name>/<string:dob>  This is to insert new records into existing table. 
   
    For eg: /John Smith/18-10-1997

   http://localhost:8000/read   This is to read data from the table


   http://localhost:8000/update/<customer_id>/<name>/<string:dob>    This is to update name and date of birth                                                                       for an existing record in the table.

     For eg: /1/John Smith/18-10-1997

   http://localhost:8000/delete/<customer_id>                      This is to delete a record in the table

```


# Step 5b

Can use postman to access api as well
```
https://www.getpostman.com/collections/fc0e256ff379e25cbf19

```

