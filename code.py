import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd="root",database="library1")


def addbook():
    bn = input("Enter BOOK Name: ")
    c= input("Enter BOOK Code : ")
    t= input("Total Books : ")
    s= input("Enter Subject : ")
    data = (bn,c,t,s)
    sql='insert into books values(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("Data Entered Successfully")
    main()

def issueb():
    n = input("Enter Name : ")
    r= input("Enter Reg No : ")
    co = input("Enter Book Code : ")
    d= input("Enter Date (mm/dd/yyyy): ")
    a = "insert into issue values(%s,%s,%s,%s)"
    data = (n,r,co,d)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("Book issued to : " , n)
    bookissue(co)



def submitb():
    n = input("Enter Name : ")
    r= input("Enter Reg No : ")
    co = input("Enter Book Code :")
    d= input("Enter Date (mm/dd/yyyy): ")
    a = "insert into submit values(%s,%s,%s,%s)"
    data = (n,r,co,d)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("Book Submitted from :", n)
    booksubmit(co)



def bookissue(co):
    a="select TOTAL from books where BCODE = %s"
    data = (co,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    t= myresult[0]- 1
    sql = "update books set TOTAL = %s where BCODE = %s"
    d= (t,co)
    c.execute(sql,d)
    con.commit()
    main()

def booksubmit(co):
    a="select TOTAL from books where BCODE = %s"
    data = (co,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    t= myresult[0]+ 1
    sql = "update books set TOTAL = %s where BCODE = %s"
    d= (t,co)
    c.execute(sql,d)
    con.commit()
    main()



def dbook():
    ac = input("Enter Book Code : ")
    a = "delete from books where BCODE = %s"
    data = (ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    main()


def dispbook():
    a = "select * from books"
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    for i in myresult:
        print("Book Name : ",i[0])
        print('Book Code :',i[1])
        print("Total Books : ",i[2])
        print("Subject:",i[3])
        print(">-------------------------------------------------------------<")
    main()
def bookname():
    co = input("Enter Book Code :")
    n = input("Enter new name:")
    data =(n,co)
    sql = "update books set bname = %s where BCODE = %s"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("Book name succssfully changed to : " , n)
    main()



def totalbooks():
    co = input("Enter Book Code :")
    n = input("Total no. of books:")
    data =(n,co)
    sql = "update books set total = %s where BCODE = %s"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("Total no. of books updated to : " , n)
    main()
def subject():
    co = input("Enter Book Code :")
    n = input("Enter new subject:")
    data =(n,co)
    sql = "update books set subject = %s where BCODE = %s"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("Subject succssfully changed to : " , n)
    main()



def issuename():
    co = input("Enter reg. no. :")
    n = input("Enter new name:")
    data =(n,co)
    sql = "update issue set name = %s where regno = %s"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("Name succssfully changed to : " , n)
    main()
def issueregno():
    co = input("Enter reg. no. :")
    n = input("Enter new reg. no.:")
    data =(n,co)
    sql = "update issue set regno = %s where regno = %s"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("reg. no. succssfully changed to : " , n)
    main()



def issuedate():
    co = input("Enter reg. no. :")
    n = input("Enter new date(mm/dd/yyyy):")
    data =(n,co)
    sql = "update issue set date = %s where regno = %s"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("Date succssfully changed to : " , n)
    main()
def submitname():
    co = input("Enter reg. no. :")
    n = input("Enter new name:")
    data =(n,co)
    sql = "update submit set name = %s where regno = %s"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("Name succssfully changed to : " , n)
    main()



def submitregno():
    co = input("Enter reg. no. :")
    n = input("Enter new reg. no.:")
    data =(n,co)
    sql = "update submit set regno = %s where regno = %s"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("reg. no. succssfully changed to : " , n)
    main()
def submitdate():
    co = input("Enter reg. no. :")
    n = input("Enter new date(mm/dd/yyyy):")
    data =(n,co)
    sql = "update submit set date = %s where regno = %s"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("Date succssfully changed to : " , n)
    main()



def books():
    print('''
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

                              MODIFY TABLE BOOKS
    SELECT TERM TO BE MODIFIED

    1.Book Name
    2.Total Books
    3.Subject
    ''')
    choice=input("ENTER Task No.")
    print(">-------------------------------------------------------------<")
    if(choice=='1'):
        bookname()
    elif(choice=='2'):
        totalbooks()
    elif(choice=='3'):
        subject()
    else:
        print("Wrong choice............")
        books()



def issue():
    print('''
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

                              MODIFY TABLE ISSUE
    SELECT TERM TO BE MODIFIED

    1.Name
    2.Reg. no.
    3.Date
    ''')
    choice=input("ENTER Task No.")
    print(">-------------------------------------------------------------<")
    if(choice=='1'):
        issuename()
    elif(choice=='2'):
        issueregno()
    elif(choice=='3'):
        issuedate()
    else:
        print("Wrong choice............")
        main()



def submit():
    print('''
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

                              MODIFY TABLE SUBMIT
    SELECT TERM TO BE MODIFIED

    1.Name
    2.Reg. no.
    3.Date
    ''')
    choice=input("ENTER Task No.")
    print(">-------------------------------------------------------------<")
    if(choice=='1'):
        submitname()
    elif(choice=='2'):
        submitregno()
    elif(choice=='3'):
        submitdate()
    else:
        print("Wrong choice............")
        submit()


    
def modify():
    print('''
                              MODIFY DATA
    SELECT TABLE

    1.BOOKS
    2.ISSUE
    3.SUBMIT
    ''')
    choice=input("ENTER Task No.")
    print(">-------------------------------------------------------------<")
    if(choice=='1'):
        books()
    elif(choice=='2'):
        issue()
    elif(choice=='3'):
        submit()
    else:
        print("Wrong choice............")
        modify()



def main():
    print('''
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

                               LIBRARY MANAGER
    1.ADD BOOK
    2.ISSUE BOOK
    3.SUBMIT BOOK
    4.DELETE BOOK
    5.DISPLAY BOOKS
    6.MODIFY
    ''')
    choice=input("ENTER Task No.")
    print(">-------------------------------------------------------------<")
    if(choice=='1'):
        addbook()
    elif(choice=='2'):
        issueb()
    elif(choice=='3'):
        submitb()
    elif(choice=='4'):
        dbook()
    elif(choice=='5'):
        dispbook()
    elif(choice=='6'):
        modify()
    else:
        print("Wrong choice............")
        main()

def pswd():
    ps=input("Enter Password")
    if ps=="python":
        main()
    else:
        print("Wrong Password")
        pswd()
pswd()
