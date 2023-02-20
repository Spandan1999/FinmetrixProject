This project converts an excel worksheet to a sql relational table.

This project is written in python.

Requirements for the project to run on different systems:-
	-> Python 3.x should be installed
	-> MySql should be installed along with its tools like	(workbench(GUI) & sql shell(CLI)
	-> pip install pandas
	-> pip install sqlalchemy
	-> pip install mysql.connector


After the requirements have been fulfilled go to DatabaseCreator.py and run the program. The DatabaseCreator.py is documented. I would recommend to understand the code first and then change it according to your requirement. The databaseCreator.py makes connection to mysql server using mysql.connector module and creates a database in it to store data.

After creating the database in DatabaseCreator.py run the main.py for converting a excel file to a database table and storing the table in the database 
