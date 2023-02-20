# This python program is used to make a connection with the MySql server and create a database in the MySql server.
# mysql.connector doesnt come in default with python 3.X we have to install it by using pip command
import mysql.connector
# This config variable can be changed if the connection of the database is failing. If the connection is failing then
# only this variable should be changed. For example if the host is a remote server the "host" key should have the
# remote server's IP address rather than the localhost, the user and password can be changed. If the password is
# wrong then connection wont be established
config = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "Sikun_123",
        "charset": "utf8",
        "use_unicode": True,
        "get_warnings": True,
    }
# This line is responsible for the connection
myDb = mysql.connector.connect(**config)
print('connection established  successfully')
myCursor = myDb.cursor()
# This line creates a database with a name in this case 'ogdatabase' is the name
myCursor.execute("CREATE DATABASE IF NOT EXISTS ogdatabase")
print("Database Created Successfully..")
# After running this code we have to run main.py in this project directory.
# The main.py creates a database table from an excel sheet

