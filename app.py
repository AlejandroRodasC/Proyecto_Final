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
    genre = request.form['genre']
    pnum= request.form['phone_number']
    birth_date = datetime.strptime(request.form['birth_date'], '%d/%m/%Y')
    age = int(Methods.calculate_age(birth_date))  
    career = request.form['career']
    poem_genre =  request.form['poem_genre']
    enrollment = datetime.now()
    participation = Methods.calculate_date_participation(enrollment,carnet,poem_genre)
    
    #Verifications
    flag_carnet = Methods.check_carnet(carnet)
    flag_genre =  Methods.check_genre(genre)
    flag_poem = Methods.check_poem_genre(poem_genre)
    if len(carnet)==0:
        return 'The carnet field is required.'
    if len(name) ==0:
        return 'The name field is required.'
    if len(address) ==0:
        return 'The address field is required.'
    if len(genre) ==0:
        return 'The genre field is required.'
    if flag_genre:
        return 'Invalid genre.'
    if len(pnum) ==0:
        return 'The phone number field is required.'
    if birth_date is None:
        return 'The birthdate field is required.'
    if len(career) ==0:
        return 'The career field is required.'
    if len(poem_genre) ==0:
        return 'The poem genre field is required.'
    if flag_poem:
        return 'Invalid poem genre.'
    if flag_carnet:
        return 'The carnet is invalid.'
    if age <= 17:
        return f'You need to be 18 years old, you have {age} years old.'

    data = (carnet, name , address ,genre, pnum , birth_date , age , career , poem_genre , enrollment , participation)
    curs_users = conn.cursor()
    Connection.insert_student(data)
    curs_users.close()

    return 'You are registered, good luck!'

@app.route('/list_of_students')
def list_students():
    curs_students = conn.cursor(dictionary= True,buffered=True)

    Connection.list_students(curs_students)
    students = curs_students.fetchall()
    curs_students.close()

    return students