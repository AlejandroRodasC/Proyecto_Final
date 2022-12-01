import mysql.connector as conn

class Connection:

    def connect_db():
        connec = conn.connect(host='localhost', user='root', passwd = 'alejandro', db='poesia')
        return  connec
    
    def insert_student(data):
        connec = conn.connect(host='localhost', user='root', passwd = 'alejandro', db='poesia')
        request =( 'INSERT INTO Students (carnet , name_st , address , phone_number , birth_date , career , poem_genre , enrollment , participation)' 
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)' )
        cursor = connec.cursor()
        cursor.execute(request,data)
        connec.commit()
    
    def list_students(cursor):
        request =  ('SELECT name_st , career , age , poem_gener , participation from Students')
        cursor.execute(request)
