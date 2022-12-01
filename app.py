from flask import Flask, request
from datetime import datetime
from connection_db_PF import Connection
from methods import Methods
app = Flask(__name__)
conn = Connection.connect_db()

@app.route("/")
def index():
    return 'This is the start of the APP.'

@app.post('/register_student')    
def register_user():
    carnet =  request.form['carnet']
    name = request.form['name_student']
    address = request.form['address']
    pnum= request.form['phone_number']
    birth_date = datetime.strptime(request.form['birth_date'], '%d/%m/%Y')
    age = int(Methods.calculate_age(birth_date))  
    career = request.form['career']
    poem_genre =  request.form['poem_genre']
    enrollment = datetime.now()
    participation = 0 # crear un metodo para poder calcular la participacion del estudiante

    data = (carnet, name , address , pnum , birth_date , age , career , poem_genre , enrollment , participation)
    curs_users = conn.cursor()
    Connection.insert_student(conn,curs_users,data)

    curs_users.close()

    return 'The student was registered'

@app.route('/list_of_students')
def list_students():
    curs_students = conn.cursor(dictionary= True,buffered=True)

    Connection.list_students(curs_students)
    students = curs_students.fetchall()
    curs_students.close()

    return students