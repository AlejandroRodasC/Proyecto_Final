from student import register_student
from student_factory import StudentFactory
import pytest

class TestRegisterStudent():
    @pytest.fixture(autouse=True)
    def setup(self):
        self.student_data = StudentFactory.create()
    
    #Happy Path
    def test_student_was_registered(self):
        message = register_student(**self.student_data)
        assert message ==  'The student was registered'
    
    #Edge cases
    def test_invalid_carnet(self):
        with pytest.raises(Exception) as error:
            self.student_data['carnet'] = 'aiif80'
            message = register_student(**self.student_data)
            assert str(error.value) == 'Invalid carnet.'
    
    def test_invalid_genre(self):
        with pytest.raises(Exception) as error:
            self.student_data['genre'] = 'invalid'
            message = register_student(**self.student_data)
            assert str(error.value) == 'Invalid genre.'
    
    def test_underage(self):
        with pytest.raises(Exception) as error:
            self.student_data['age'] = 15
            message = register_student(**self.student_data)
            assert str(error.value) == 'You need to be of legal age.'
    
    def test_invalid_poem_genre(self):
        with pytest.raises(Exception) as error:
            self.student_data['poem_genre'] = 'invalid'
            message = register_student(**self.student_data)
            assert str(error.value) == 'Invalid poem genre.'
    
    def test_invalid_phone_number(self):
        with pytest.raises(Exception) as error:
            self.student_data['phone_number'] = '739874932947'
            message = register_student(**self.student_data)
            assert str(error.value) == 'Invalid phone number.'
