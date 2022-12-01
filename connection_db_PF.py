import mysql.connector as conn

class Connection:

    def connect_db():
        connec = conn.connect(host='localhost', user='root', passwd = 'alejandro', db='poesia')
        return  connec
    
    def insert_student(data):
        connec = conn.connect(host='localhost', user='root', passwd = 'alejandro', db='poesia')
        request =( 'INSERT INTO Students (carnet , name_st , address , genre , phone_number , birth_date , age , career , poem_genre , enrollment , participation)' 
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' )
        cursor = connec.cursor()
        cursor.execute(request,data)
        connec.commit()
    
    def list_students(cursor):
        request =  ('SELECT name_st , career , age , poem_genre , participation from Students')
        cursor.execute(request)
    
    def list_students_for_career(cursor,data):
        request =  ('SELECT * from Students where career = %s')
        cursor.execute(request,data)
    
    def list_students_for_age(cursor,data):
        request =  ('SELECT * from Students where age > %s')
        cursor.execute(request,data)
    
    def list_students_for_poem_genre(cursor,data):
        request =  ('SELECT * from Students where poem_genre = %s')
        cursor.execute(request,data)
    
    def list_students_for_participation(cursor,data):
        request =  ('SELECT * from Students where participation = %s')
        cursor.execute(request,data)
    