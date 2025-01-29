from tests.src.randomizers import randomizer_phone, randomizer_mail, randomizer_company, randomizer_digit, \
    randomizer_person

fake_users = [
    {"id": randomizer_digit.generate_int_digit(period_from=1, period_to=30),
     "first_name": randomizer_person.generate_first_name_male(),
     "last_name": randomizer_person.generate_last_name_male(),
     "patronymic": randomizer_person.generate_middle_name_male(),
     "age": randomizer_digit.generate_int_digit(period_from=1, period_to=80),
     "phone_number": randomizer_phone.generate_phone_number(),
     "email": randomizer_mail.generate_email(),
     "company": randomizer_company.generate_company_name(),
     "profession": randomizer_company.generate_profession_name(),
     } for _ in range(10)
]
