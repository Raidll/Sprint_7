from data import helpers

login_for_parameters = helpers.generate_random_string(10)
password_for_parameters = helpers.generate_random_string(10)
first_name_for_parameters = helpers.generate_random_string(10)

payloads_for_parameters = [
    [{"login": login_for_parameters, "password": password_for_parameters}],
    [{"login": login_for_parameters, "firstName": first_name_for_parameters}],
    [{"password": password_for_parameters, "firstName": first_name_for_parameters}]
]
