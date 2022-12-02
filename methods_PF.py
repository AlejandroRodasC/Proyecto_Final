import re
from calendar import monthrange
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class Methods:
    
    def check_carnet(carnet):
        if len(carnet)>6:
            return True
        
        pat  = r"A[a-zA-Z1-9]{3}5(1|3|9){1}"
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
        
        if last_digit == '1' and poem_gener == 'dramática':
            participation = enrollment + timedelta(days=5)

            if participation.weekday() == 5: # if that day is saturday
                participation = participation + timedelta(days=2)
                year1 = participation.year 
                month1= participation.month
                day1= participation.day
                participation1 =  datetime(year1,month1,day1,0,0,0,0)
                return participation

            if participation.weekday() == 6: # if that day is sunday
                participation = participation + timedelta(days=1)
                year1 = participation.year 
                month1= participation.month
                day1= participation.day
                participation1 =  datetime(year1,month1,day1,0,0,0,0)
                return participation1
            
            year1 = participation.year 
            month1= participation.month
            day1= participation.day
            participation1 =  datetime(year1,month1,day1,0,0,0,0)
            return participation1

        #If last digit is 3 and poem genre is épica
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
    
        #In other cases    
        day = enrollment.weekday()
        if day == 0: 
            participation = enrollment + timedelta(days=4)
        elif day == 1:
            participation = enrollment + timedelta(days=3)
        elif day == 2:
            participation = enrollment + timedelta(days=2)
        elif day == 3:
            participation = enrollment + timedelta(days=1)
        elif day == 4:
            participation = enrollment + timedelta(weeks=1)
        elif day == 5:
            participation = enrollment + timedelta(days=6)
        elif day == 6:
            participation = enrollment + timedelta(days=5)
        
        year2 = participation.year 
        month2= participation.month
        day2= participation.day
        participation2 =  datetime(year2,month2,day2,0,0,0,0)

        return participation2
    
    def check_genre(gener):
        if gener not in ['masculino', 'femenino', 'otros']:
            return True
        else: 
            return False
    
    def check_poem_genre(poem_genre):
        if poem_genre not in ['lírica', 'épica', 'dramática']:
            return True
        else: 
            return False
    
    def check_phone_number(phone_number):
        if len(phone_number)>8:
            return True
        
        pat  = r"[0-9]{8}"
        if re.match(pat,phone_number):
            return False
        else:
            return True