import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="userroot",database="contact_db");

mycursor = mydb.cursor()

mycursor.execute("use contact_db");

#mycursor.execute("create table contactBook(Name varchar(20))");

#mycursor.execute("alter table contactbook add PhoneNumber BigInt");

def add_contact():
    name = input("Enter Name: ")
    phone = int(input("Enter phone number: "))
    val = (name,phone)
    sql = "insert into contactbook values (%s,%s)"
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"record inserted")

def del_contact():
    name = input("enter contact name to be deleted : ")
    sql = "delete from contactbook where name = " + "'"+name+"'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount,"Record Deleted")

def display_all():
    print("ALL the contacts in the book")
    sql = "select * from contactbook order by name"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    mydb.commit()
    for x in result:
      print(x)

def search_contact():
    name = input("enter contact name to be searched : ")
    sql = "select * from contactbook where name like  " + "'"+name+"%'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    mydb.commit()
    for x in result:
      print(x)

def update_contact():
    name = input("enter name to be updated : ")
    name1 = input("Enter new name : ")
    phone1 = int(input("enter new phone number:"))
    val= (name1,phone1,name)
    sql = "update contactbook set name = %s , phoneNumber = %s where name = %s"
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"Row updated")

i = 1
while(i == 1):
    print("Welcome To Contact Book");
    print("Press 1, To Add a Contact in the book");
    print("Press 2, To Update Contact in the book");
    print("Press 3, To Delete Contact in the book");
    print("Press 4, To Display all contacts in the book");
    print("Press 5, To Search contact in the book");
    print("Press 0, To Exit");
    k = int(input())
    if(k==1):
        add_contact();
    elif(k==2):
        update_contact();
    elif(k==3):
        del_contact();
    elif(k==4):
        display_all();
    elif(k==5):
        search_contact();
    elif(k==0):
        print("You have exited the program")
        break;
    else:
        continue;
