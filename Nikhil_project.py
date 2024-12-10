import pymysql


'''
def b_table():
    conn=pymysql.connect(host='localhost',user='root',password='Nikhil@141937',db='mynewproject')
    cur=conn.cursor()
    cur.execute("create table banksystem(cust_Account int primary key,cust_Name varchar(20) ,FatherName varchar(20) ,
    cust_Address varchar(20),cust_Contactno bigint  unique,Acc_Type varchar(20) ,Govt_ID varchar(),Amount int)")
    print("create table")
    conn.close

b_table()
'''


def new_Customer():

    conn=pymysql.connect(host='localhost',user='root',password='Nikhil@141937',db='mynewproject')
    cur=conn.cursor()
    print("\t\t\tWELCOME TO OUR BANK")
    a=input("Enter account no:")    
    b=input("Enter your name: ")
    c=input("Enter your father's name: ")
    d=input("Enter your address:")
    e=input("Enter your mobile number: ")
    f=input("Account type(SAVING/CURRENT): ")
    g=input("Type of govt ID(PAN/AADHAAR): ")
    h=input("Enter amount to deposit:")
    s='insert into banksystem values(%s,%s,%s,%s,%s,%s,%s,%s)'
    t=(a,b,c,d,e,f,g,h)
    cur.execute(s,t)
    print("record is add")
    conn.commit()
    conn.close()
    exit

def existing_customer():
    conn=pymysql.connect(host='localhost',user='root',password='Nikhil@141937',db='mynewproject')
    cur=conn.cursor()
    print("\n1) DEPOSIT MONEY","\n2) WITHDRAW MONEY","\n3) CHECK BALANCE")
    choice=int(input("\nENTER YOUR CHOICE: "))
    if(choice==1):
        cust_account=input("Enter your account number:")
        amount=input("Enter your amount to deposit:")
        s="update banksystem set amount=amount+%s where cust_account=%s"
        cur.execute(s,(amount,cust_account))
        print("amount deposit")
        conn.commit()
        conn.close()
    elif(choice==2):
        
        
        cust_account=input("Enter your account number:")
        amount=input("Enter your amount to withdraw:")
        
        n="update banksystem set amount=amount-%s where cust_account=%s"
        
        cur.execute(n,(amount,cust_account))
        print("amount withdraw")
           
       
        conn.commit()
        conn.close()
    elif(choice==3):
        conn=pymysql.connect(host='localhost',user='root',password='Nikhil@141937',db='mynewproject')
        cur=conn.cursor()
        cust_account=input("Enter your account number")
        m=('select amount from banksystem where cust_account=%s')
        cur.execute(m,(cust_account))
        r=cur.fetchone()
        print("Your balance=",r[0])
        
        conn.commit()
        conn.close()

     
        exit
    

while True:
    print("_"*80)
    print("                        WELCOME TO BANKING MANAGEMENT SYSTEM")
    
    print("_"*80)
    print("\n1) NEW CUSTOMER","\n2) EXISTING CUSTOMER","\n3) EXIT")
    choice=int(input("ENTER CHOICE: "))
    if(choice==1):
        new_Customer()
    elif(choice==2):
        existing_customer()
    elif(choice==3):
        exit()
    else:
        print("WRONG CHOICE!!!!!")

