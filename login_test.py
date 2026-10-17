
# AttendX Login Test Script

def test_login():
    username = "student123"
    password = "correct_password"

    if username and password:
        print("PASS: Login fields are filled.")
    else:
        print("FAIL: Login fields are empty.")


def test_empty_login():
    username = ""
    password = ""

    if not username and not password:
        print("PASS: Empty login fields detected.")
    else:
        print("FAIL: Empty login test failed.")


def test_whitespace_login():
    username = "   "

    if not username.strip():
        print("PASS: Whitespace-only username detected.")
    else:
        print("FAIL: Whitespace-only username not detected.")


test_whitespace_login()
test_login()
test_empty_login()
