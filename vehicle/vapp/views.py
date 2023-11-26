from django.shortcuts import render
import mysql.connector
import csv

# Create your views here.
def frontend(request):
    return render(request,'frontend.html')

def register(request):
    if request.method=="POST":
        a=request.POST['a1']
        b=request.POST['b1']
        mydb = mysql.connector.connect(
        host="localhost",
        user="root ",
        password="",
        database="vehicledata"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO vehicledetails (vehicle_no,vehicle_name) VALUES (%s,%s)"
        val = (a,b)
        mycursor.execute(sql, val)
        mydb.commit()
        
    return render(request,'register.html')

def delete(request):
    if request.method=="POST":
        a=request.POST['a1']
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="vehicledata"
        )
        mycursor = mydb.cursor()

        sql = "DELETE FROM vehicledetails WHERE  vehicle_no= %s"
        val=(a,)
        mycursor.execute(sql,val)

        mydb.commit()

    return render(request,'delete.html')

def registerdata(request):
    f = open('registerdata.csv', 'w')
    writer = csv.writer(f)
    header = ['vehicle_no', 'vehicle_name', 'pass_no']
    writer.writerow(header)


    mydb = mysql.connector.connect(
    host="localhost",
    user="root ",
    password="",
    database="vehicledata"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM vehicledetails"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x) 
        data = [x]  
        writer.writerows(data)
    f.close()
    return render(request,'frontend.html')

def ldata(request):
    f = open('logdata.csv', 'w')
    writer = csv.writer(f)
    header = ['vehicle_no', 'vehicle_name', 'pass_no']
    writer.writerow(header)


    mydb = mysql.connector.connect(
    host="localhost",
    user="root ",
    password="",
    database="vehicledata"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM vehicledetails"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x) 
        data = [x]  
        writer.writerows(data)
    f.close()
    return render(request,'frontend.html')


