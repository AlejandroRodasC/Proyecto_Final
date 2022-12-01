from faker import Faker
from datetime import datetime
from methods_PF import Methods
fake = Faker()
created_at = datetime.now()
birthdate = datetime.strptime(str(fake.date_of_birth()), '%Y-%m-%d')
age = Methods.calculate_age(birthdate)
class StudentFactory():
    def create():
        student_data = {
            'carnet' : 'Ajhf53',
            'name' : fake.name(),
            'address' : fake.address(),
            'genre' : 'masculino',
            'phone_number' : str(fake.random_int(10000000,99999999)),
            'birthdate' : birthdate,
            'age' : age,
            'career' : fake.job(),
            'poem_genre' : 'épica',
            'enrollment' : created_at,
            'participation' : '2022-12-02'
        }
    
        return student_data
