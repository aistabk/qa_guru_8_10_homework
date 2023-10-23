from model.practice_form_full import PracticeFormRegistrationFactCheck
from data.users import User

practice_form = PracticeFormRegistrationFactCheck()


def test_student_registration_form():
    guest = User(first_name='Имя', last_name='Фамилия', email='testmail@mail.gg', gender='Other',
                 month_of_brith='November', phone_number='2589632147', year_of_brith='2006', day_of_brith='19',
                 subject='Physics',
                 hobby='Reading', picture='hedgehog.jpg', current_address='221b, Baker Street, London, NW1 6XE, UK',
                 state='NCR',
                 city='Delhi')
    practice_form.open()

    practice_form.registration(guest)

    practice_form.student_should_be_registred(guest)
