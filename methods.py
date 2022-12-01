import re
from calendar import monthrange
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class Methods:
    
    def check_carnet(carnet):
        if len(carnet)>6:
            return True
        
        pat  = r"A[a-zA-Z0-9]{3}5(1|3|9){1}"
        if re.match(pat,carnet):
            return False
        else:
            return True

    def calculate_age(birth_date):
        age = datetime.today().year - birth_date.year
        birthday =  birth_date + relativedelta(years=age)

        if birthday > datetime.today():
            age = age -1
        
        return age
    
    def calculate_date_participation(enrollment,carnet,poem_gener):
        last_digit =  carnet[5:6]
        
        if last_digit == '1' and poem_gener == 'dramático':
            participation = enrollment + timedelta(days=5)

            if participation.weekday() == 5: # if that day is saturday
                participation = participation + timedelta(days=2)
                return participation

            if participation.weekday() == 6: # if that day is sunday
                participation = participation + timedelta(days=1)
                return participation

        if last_digit == '3' and poem_gener == 'épica':
            year = int(enrollment.year)
            month =  int(enrollment.month)
            days_of_month =  int(monthrange(year, month)[1])
            participation = datetime(year,month,days_of_month)

            if participation.weekday() == 5: # if that day is saturday
                participation = participation + timedelta(days=2)
                return participation

            if participation.weekday() == 6: # if that day is sunday
                participation = participation + timedelta(days=1)
                return participation
            
        day = enrollment.weekday()
        if day == 0: 
            participation = enrollment + timedelta(days=4)
            return participation
        elif day == 1:
            participation = enrollment + timedelta(days=3)
            return participation
        elif day == 2:
            participation = enrollment + timedelta(days=2)
            return participation
        elif day == 3:
            participation = enrollment + timedelta(days=1)
            return participation
        elif day == 4:
            participation = enrollment + timedelta(weeks=1)
            return participation
        elif day == 5:
            participation = enrollment + timedelta(days=6)
            return participation
        elif day == 6:
            participation = enrollment + timedelta(days=5)
            return participation
    
    def check_genre(gener):
        if gener not in ['masculino', 'femenino', 'otros']:
            return True
        else: return False
    
    def check_poem_genre(poem_genre):
        if poem_genre not in ['lírica', 'épica', 'dramática']:
            return True
        else: return False