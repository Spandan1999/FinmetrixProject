
from tkinter import *
from tkinter import messagebox
import mysql.connector
import threading


def fetch():
    global serial_label, name_label, remark_label, phone_label, count_label
    Id = entry.get()
    try:
        myCursor.execute("SELECT COUNT(REMARKS) FROM OGDB")
        count = myCursor.fetchone()[0]
        myCursor.execute("SELECT * FROM OGDB WHERE `SL NO` =" + Id)
        data = myCursor.fetchall()
        Id = data[0][0]
        customer_name = data[0][1]
        phone_number = data[0][2]
        remarks = data[0][3]
        if remarks is None or remarks == ' ' or remarks == '':
            remarks = "None"
        l1 = Label(window, text="Serial No",
                   font=('Arial', 16),
                   fg='Black')
        l1.grid(row=2, column=0, padx=20, pady=10)
        serial_label.grid_forget()
        serial_label = Label(window, text=Id,
                             font=('Arial', 14),
                             fg='Black')
        serial_label.grid(row=3, column=0, padx=20, pady=10)
        l2 = Label(window, text="Customer Name",
                   font=('Arial', 16),
                   fg='Black')
        l2.grid(row=2, column=1, padx=20, pady=10)
        name_label.grid_forget()
        name_label = Label(window, text=customer_name,
                           font=('Arial', 14),
                           fg='Black')
        name_label.grid(row=3, column=1, padx=20, pady=10)
        l3 = Label(window, text="Phone Number",
                   font=('Arial', 16),
                   fg='Black')
        l3.grid(row=2, column=2, padx=20, pady=10)
        phone_label.grid_forget()
        phone_label = Label(window, text=phone_number,
                            font=('Arial', 16),
                            fg='Black')
        phone_label.grid(row=3, column=2, padx=20, pady=10)
        l4 = Label(window, text="Remarks",
                   font=('Arial', 16),
                   fg='Black')
        l4.grid(row=2, column=3, padx=20, pady=10)
        var = StringVar()
        var.set(remarks)
        remark_label.grid_forget()
        remark_label = Label(window, textvariable=var,
                             font=('Arial', 16),
                             fg='Black')
        remark_label.grid(row=3, column=3, padx=20, pady=10)
        l5 = Label(window, text="Count :",
                   font=('Arial', 16),
                   fg='Black')
        l5.grid(row=6, column=2, padx=5, pady=10)
        count_label.grid_forget()
        count_label = Label(window, text=str(count),
                            font=('Arial', 16),
                            fg='Black')
        count_label.grid(row=7, column=2, padx=5)
        remark_list = ['None', 'NI', 'NC', 'WN', 'ON']
        x = IntVar()

        def select():
            if x.get() == 1:
                var.set('NI')
                try:
                    myCursor.execute('UPDATE OGDB SET REMARKS = %s WHERE `SL NO` = %s',
                                     ('NI', Id))
                    mydb.commit()
                    messagebox.showinfo(title="Status", message='Data Uploaded Successfully')
                except:
                    messagebox.showerror(title="Status", message='Data not uploaded')
            elif x.get() == 2:
                var.set('NC')
                try:
                    myCursor.execute('UPDATE OGDB SET REMARKS = %s WHERE `SL NO` = %s',
                                     ('NC', Id))
                    mydb.commit()
                    messagebox.showinfo(title="Status", message='Data Uploaded Successfully')
                except:
                    messagebox.showerror(title="Status", message='Data not uploaded')
            elif x.get() == 3:
                var.set('WN')
                try:
                    myCursor.execute('UPDATE OGDB SET REMARKS = %s WHERE `SL NO` = %s',
                                     ('WN', Id))
                    mydb.commit()
                    messagebox.showinfo(title="Status", message='Data Uploaded Successfully')
                except:
                    messagebox.showerror(title="Status", message='Data not uploaded')
            elif x.get() == 4:
                var.set('ON')
                try:
                    myCursor.execute('UPDATE OGDB SET REMARKS = %s WHERE `SL NO` = %s',
                                     ('ON', Id))
                    mydb.commit()
                    messagebox.showinfo(title="Status", message='Data Uploaded Successfully')
                except:
                    messagebox.showerror(title="Status", message='Data not uploaded')

            else:
                var.set("None")
                try:
                    myCursor.execute('UPDATE OGDB SET REMARKS = %s WHERE `SL NO` = %s',
                                     (None, Id))
                    mydb.commit()
                    messagebox.showinfo(title="Status", message='Data Uploaded Successfully')
                except:
                    messagebox.showerror(title="Status", message='Data not uploaded')

        for index in range(len(remark_list)):
            radio_button = Radiobutton(window, text=remark_list[index],
                                       variable=x, value=index,
                                       font=("Impact", 10),
                                       bg='#D3D3D3',
                                       command=select)
            radio_button.grid(row=4 + index, column=3)

    except:
        err = messagebox.showerror(title="ERROR", message="Data entered is not Valid")


def ExecuteOperation():
    t1 = threading.Thread(target=fetch())

    t1.start()


'''
config = {
    "host": "192.168.1.5",
    "port": 3306,
    "user": "finmetrixUser",
    "password": "Finmetrix@1981",
    "auth_plugin": "mysql_native_password",
    "database": "ogdatabase",
    "charset": "utf8",
    "use_unicode": True,
    "get_warnings": True
}
'''

if __name__ == '__main__':
    # This below block deals with the reading of the text file config.txt
    config = {}
    with open(r'config.txt') as f:
        d = f.readlines()
    for line in d:
        l = list(line.split(':'))
        if l[1].strip() == 'True':
            config[l[0].strip()] = True
        elif l[1] == 'False':
            config[l[0].strip()] = False
        elif l[0].strip() == 'port':
            config[l[0].strip()] = int(l[1].strip())
        else:
            config[l[0].strip()] = l[1].strip()
    # This block of code is written in try except block because the connection to the database server may raise
    # an exception
    try:
        # This line establishes a connection to the database by passing the config dictionary
        mydb = mysql.connector.connect(**config)
        myCursor = mydb.cursor()
        window = Tk()
        window.geometry('760x340')
        window.title("Finmetrix data entry")
        window.config(background="#D3D3D3")
        serial_label = Label(window)
        name_label = Label(window)
        phone_label = Label(window)
        remark_label = Label(window)
        count_label = Label(window)
        label = Label(window, text="Enter Serial Id :",
                  font=('Arial', 16),
                  fg='Black')
        label.grid(row=0, column=0)
        entry = Entry(window, font=("Arial", 12))
        entry.grid(row=1, column=0, padx=10, pady=20)
        submit = Button(window, text='Check', command=ExecuteOperation)
        submit.grid(row=1, column=1, padx=10, pady=20)
        window.mainloop()
    except:
        messagebox.showerror(message='Cannot Connect to the database please check the config.txt')
