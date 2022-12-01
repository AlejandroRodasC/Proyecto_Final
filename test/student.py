from methods_PF import Methods
def register_student(
    carnet,
    name,
    address,
    genre,
    phone_number,
    birthdate,
    age,
    career,
    poem_genre,
    enrollment,
    participation
):
    if check_carnet(carnet):
        raise Exception('Invalid carnet.')
    if check_genre(genre):
        raise Exception('Invalid genre.')
    if check_age(age):
        raise Exception('You need to be of legal age.')
    if check_poem_genre(poem_genre):
        raise Exception('Invalid poem genre.')
    if check_phone(phone_number):
        raise Exception('Invalid phone number.')
    return 'The student was registered'

def check_carnet(carnet):
    return Methods.check_carnet(carnet)

def check_genre(genre):
    return Methods.check_genre(genre)

def check_age(age):
    if age <=17:
        return True
    else: 
        return False

def check_poem_genre(poem_genre):
    return Methods.check_poem_genre(poem_genre)

def check_phone(number):
    return Methods.check_phone_number(number)