from tests.src import user_test_api
from tests.src.helper import asserts
from tests.src.randomizers import randomizer_phone, randomizer_mail, randomizer_company, randomizer_digit, \
    randomizer_person


def test_create_user():
    first_name_crt = randomizer_person.generate_first_name_male()

    new_user = user_test_api.post(
        first_name=first_name_crt,
        last_name=randomizer_person.generate_last_name_male(),
        patronymic=randomizer_person.generate_middle_name_male(),
        age=randomizer_digit.generate_int_digit(period_from=1, period_to=80),
        phone_number=randomizer_phone.generate_phone_number(),
        email=randomizer_mail.generate_email(),
        company=randomizer_company.generate_company_name(),
        profession=randomizer_company.generate_profession_name(),
    )
    tmp = new_user.json()

    id_ = tmp.get("id", "There is no key id")

    asserts.status_code(response=new_user)

    asserts.equal(expected_result="Ok",
                  actual_result=new_user.json().get("status"),
                  message="AC != EC for POST method")

    user_id = user_test_api.get_id(id_=id_).json()

    user_id_crt = user_test_api.get_id(id_=id_)
    asserts.equal(
        expected_result=first_name_crt,
        actual_result=user_id_crt.json().get("first_name"),
        message="AC != EC first for POST method"
    )

    first_name = user_id.get("first_name")
    first_name_upd = randomizer_person.generate_first_name_male()

    user = user_test_api.patch(
        id_=id_,
        first_name=first_name_upd,
        last_name=randomizer_person.generate_last_name_male(),
        patronymic=randomizer_person.generate_middle_name_male(),
        age=randomizer_digit.generate_int_digit(period_from=1, period_to=80),
        phone_number=randomizer_phone.generate_phone_number(),
        email=randomizer_mail.generate_email(),
        company=randomizer_company.generate_company_name(),
        profession=randomizer_company.generate_profession_name(),
    )

    user_id_upd = user_test_api.get_id(id_=id_)

    asserts.status_code(response=user)
    asserts.equal(expected_result="Ok",
                  actual_result=user.json().get("status"),
                  message="AC != EC for PATCH method")
    asserts.equal(expected_result=first_name_upd,
                  actual_result=user_id_upd.json().get("first_name"),
                  message="AC != EC word for patch method")

    user_dl = user_test_api.delete(id_=id_)
    asserts.status_code(response=user_dl)
    print(user_dl.json())
    asserts.equal(expected_result="Ok",
                  actual_result=user_dl.json().get("status"),
                  message="AC != EC for delete method")

    user_id_dl = user_test_api.get_id(id_=id_)
    asserts.status_code(response=user_id_dl, is_positive=False)
