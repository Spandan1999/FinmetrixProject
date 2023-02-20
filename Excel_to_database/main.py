# pip install both pandas and sqlalchemy
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote

# This line of code converts an excel file to a pandas data frame. The pd.read_excel takes the location of the
# excel_file as its parameter
# Here the FinmetrixData is the file provided by the company which I worked for.
# You can try your personal files or anything as per your wish.
df = pd.read_excel(r'E:\finmetrix data\FinmetrixData.xlsx', sheet_name='Sheet1', index_col=0)
print(df)
# This line of code makes a connection to the database created in the DatabaseCreator.py in this project structure
# and creates an engine object.
engine = create_engine('mysql://root:%s@localhost:3306/ogdatabase10' % quote('Sikun_123'))
# This line converts the pandas data frame to sql by using the engine object as connector
df.to_sql('ogdb4', if_exists='fail', con=engine)
# cursor is created to parse the database
cur = engine.execute('Select * from ogdb4')
for row in cur:
    print(row)
# In the output the datasheet is printed two times.
# In the first time it is printed for the successful conversion of excel to dataFrame
# In the second time its printed after the the successful conversion of the excel sheet to sql.
# If the conversion is not successful then errors are displayed and the program halts.
# This can be handled using try and except blocks.
