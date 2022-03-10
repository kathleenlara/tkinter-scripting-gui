from tkinter import *
import cx_Oracle
import pandas as pd
import math
import logging
conn_usr = u'Username'
conn_pw = u'Password'
dsnStr = cx_Oracle.makedsn(" "," "," ")
con = cx_Oracle.connect(user = conn_usr, password = conn_pw, dsn= dsnStr)

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to INFO
logger.setLevel(logging.INFO)

# Read Oracle tables
def read_query(con, query):
    cursor = con.cursor()
    try:
        cursor.execute(query)
        names = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        return pd.DataFrame(rows, columns=names)
    finally:
        if cursor is not None:
            cursor.close()
            
            
# Write Oracle tables
def oracle_insert(DM_FINAL_SHIPMENTS, tablename):
    conn_usr = u'Username'
    conn_pw = u'Password;
    dsnStr = cx_Oracle.makedsn(" ", " ", " ")
    con = cx_Oracle.connect(user=conn_usr, password=conn_pw, dsn=dsnStr)

    for col in range(1, len(DM_FINAL_SHIPMENTS.columns) + 1):
        if col == 1:
            inserttext = ':1'
        else:
            inserttext = inserttext + ', :{}'.format(col)

    sql_query1 = 'TRUNCATE TABLE {}'.format(tablename)
    sqlquery = 'INSERT INTO {} VALUES({})'.format(tablename, inserttext)
    sql_query2 = 'GRANT SELECT ON {} TO PUBLIC'.format(tablename)

    df_list = DM_FINAL_SHIPMENTS.values.tolist()
    cur = con.cursor()

    cur.execute(sql_query1)
    for b in df_list:

        for index, value in enumerate(b):
            if isinstance(value, float) and math.isnan(value):
                b[index] = None
            elif isinstance(value, type(pd.NaT)):
                b[index] = None

    con.cursor().executemany(sqlquery, df_list)
    cur.execute(sql_query2)
    con.close()
    
 # Finding the
def find_min(x):
    # Removed chunk of code for confidentiality purposes
    


# MyWindow Class
module_logger = logging.getLogger(__name__)

class MyWindow:
    def __init__(self, win):
        self.lbl4 = Label(win, text='Supply Chain Algorithm', fg='red', font=("Helvetica", 16))
        self.lbl4.place(x=50, y=45)

        self.lbl1=Label(win, text='SHIPMENTS TABLE::')
        self.lbl1.place(x=40, y=100)

        self.lbl2=Label(win, text='OUTPUT TABLE:')
        self.lbl2.place(x=40, y=130)

        self.t1=Entry(bd=3,width = 35)
        self.t1.place(x=200, y=100)

        self.t2=Entry(bd=3,width = 35)
        self.t2.place(x=200, y=130)

        self.btn1 = Button(win, text='Allocate')
        self.b1=Button(win, text='Allocate', command=self.algorithm)
        self.b1.place(x=200, y=180,width = 200)

        self.lbl1 = Label(win, text='ALLOCATION SUMMARY:')
        self.lbl1.place(x=40, y=250)

        self.orders = Label(win, text='AVAILABLE SHIPMENTS:')
        self.orders.place(x=40, y=280)
        self.torders = Entry(width=35)
        self.torders.place(x=200, y=280)

        self.shipments = Label(win, text='TOTAL ALLOCATED:')
        self.shipments.place(x=40, y=310)
        self.tshipments = Entry(width=35)
        self.tshipments.place(x=200, y=310)


        self.lbl3=Label(win, text='Total Need:')
        self.lbl3.place(x=40, y=350)
        self.t3 = Entry(width = 35)
        self.t3.place(x=200, y=350)

        self.lbl5 = Label(win, text='Excess Shipments')
        self.lbl5.place(x=40, y=380)
        self.t5 = Entry(width=35)
        self.t5.place(x=200, y=380)


    # Function that runs the algorithm
    def algorithm(self):     
        # Removed chunk of code for confidentiality purposes
        
        # writes the output tale back to oracle database
        oracle_insert(FINAL_TABLE, 'SCHEMA.{}'.format(final_ship))



#Callers
window=Tk()
mywin=MyWindow(window)
window.title('Algorithm')
window.geometry("500x530+10+10")
window.mainloop()