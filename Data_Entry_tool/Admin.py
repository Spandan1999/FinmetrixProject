from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
import threading
import xlsxwriter
import pandas as pd
from sqlalchemy import create_engine


def Update(np):
    df = pd.read_excel(np, sheet_name='Sheet1', index_col=0)
    try:
        engine = create_engine('mysql://root:Sikun_123@localhost:3306/ogdatabase')
        try:
            df.to_sql('ogdb1', if_exists='fail', con=engine)
            engine.execute('Drop table ogdb')
            engine.execute('Alter table ogdb1 rename to ogdb ')
            messagebox.showinfo(message='Data Upload Successful')
        except:
            messagebox.showerror(message='Data not uploaded')
    except:
        messagebox.showerror(message='Cannot connect to database')
    print(df)


def excel_to_sql():
    path = filedialog.askopenfile(mode='r')
    if path.name != '':
        newPath = path.name.replace('/', '\\')
        t1 = threading.Thread(target=Update(newPath))
        t1.start()
    else:
        messagebox.showerror(message='Path Specified is empty')


def add_excel_to_database():
    res = messagebox.askyesno(title='Info', message="Old data in the data table will be replaced with the new data "
                                                    "table "
                                                    "(Only proceed if the status of the work is completed). Do you "
                                                    "Really want to Proceed?")

    if res:
        excel_to_sql()


def execute_export_operation():
    myCursor.execute("SELECT * FROM OGDB")
    header = [row[0] for row in myCursor.description]
    rows = myCursor.fetchall()
    path = filedialog.askdirectory(title="Select path to save")
    file_name_entry = Entry(window, font=("Arial", 12))
    file_name_entry.grid(row=4, column=0, padx=10, pady=20)

    def save_text():
        file_name = str(file_name_entry.get())
        if path != '' and file_name != '':
            workbook = xlsxwriter.Workbook(path + '/' + file_name + '.xlsx')
            worksheet = workbook.add_worksheet('Sheet1')
            header_cell_format = workbook.add_format({'bold': True, 'border': True, 'bg_color': 'yellow'})
            body_cell_format = workbook.add_format({'border': True})
            row_index = 0
            column_index = 0
            for column_name in header:
                worksheet.write(row_index, column_index, column_name, header_cell_format)
                column_index += 1
            row_index += 1
            for row in rows:
                column_index = 0
                for column in row:
                    worksheet.write(row_index, column_index, column, body_cell_format)
                    column_index += 1
                row_index += 1
            print(str(row_index) + ' rows written successfully to ' + workbook.filename)
            messagebox.showinfo(title="Status",
                                message=str(row_index) + ' rows written successfully to ' + workbook.filename)
            workbook.close()

    save_button = Button(window, text='Save', command=save_text)
    save_button.grid(row=5, column=0, pady=25, padx=10)


'''
config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "Sikun_123",
    "auth_plugin": "mysql_native_password",
    "database": "ogdatabase",
    "charset": "utf8",
    "use_unicode": True,
    "get_warnings": True
}
'''
d = {}
with open(r'config.txt') as f:
    data = f.readlines()
for line in data:
    l = list(line.split(':'))
    if l[1].strip() == 'True':
        d[l[0].strip()] = True
    elif l[1] == 'False':
        d[l[0].strip()] = False
    elif l[0].strip() == 'port':
        d[l[0].strip()] = int(l[1].strip())
    else:
        d[l[0].strip()] = l[1].strip()
print(d)
try:
    mydb = mysql.connector.connect(**d)
    myCursor = mydb.cursor()
    myCursor.execute("SELECT COUNT(REMARKS) FROM OGDB")
    count = myCursor.fetchone()[0]
    status = True
    window = Tk()
    window.title("Finmetrix Admin")
    window.config(background="#D3D3D3")
    rows_remaining = 103870 - count
    total_count_label = Label(window, text="Rows Remaining : " + str(rows_remaining),
                              font=('Arial', 16),
                              fg='Black')
    total_count_label.grid(row=0, column=0, pady=20)
    rows_entered_label = Label(window, text="Rows Filled : " + str(count),
                               font=('Arial', 16),
                               fg='Black')
    rows_entered_label.grid(row=1, column=0, pady=20)
    if count < 103870:
        status_label = Label(window, text="Status : Not Completed",
                             font=('Arial', 16),
                             fg='Red')
    else:
        status_label = Label(window, text="Status : Completed",
                             font=('Arial', 16),
                             fg='Green')
        status = True
    status_label.grid(row=2, column=0, pady=20)
    export_button = Button(window, text='Click to export the data in data base to a excel sheet',
                           command=execute_export_operation)
    export_button.grid(row=3, column=0, padx=20, pady=35)
    add_button = Button(window, text='Click to add new data',
                        command=add_excel_to_database)
    add_button.grid(row=4, column=0, padx=20, pady=35)
    window.mainloop()
except:
    messagebox.showerror(message='Cannot connect to data base')
