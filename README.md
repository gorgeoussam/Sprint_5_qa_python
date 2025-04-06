# Sprint_5_qa_python

Checks:

    Registration
test_registration_with_valid_data_success: checks random user can register and log in
test_registration_with_invalid_password_fail: checks less then 6 symbols PW causes an error

    Login
test_login_from_main_page_via_login_button: checks user can login with "Войти" button
test_login_via_personal_account_button: checks login via personal account
test_login_via_registration_form_button: checks login via login button from registration form
test_login_via_password_recovery_form_button: checks login via "Войти" button in password recovery form

    Personal account
test_logout_button_in_personal_account: checks log out by 'Выход' button
test_personal_account_button_redirects_correct: checks user is correctly redirected by clicking "Personal accou;t"
test_navigate_from_personal_account_to_constructor: checks correct redirect after clicking 'Конструктор' from Personal account
test_navigate_to_main_page_via_stellar_burgers_logo: checks redirect by clicking the logo

    Navigation

test_navigate_to_buns_section: checks buns are opened
test_navigate_to_sauces_section: checked sauses tab is opened
test_navigate_to_fillings_section: checks fillings section is opened

    Tests execution
to execute tests run "pytest -v" in terminal