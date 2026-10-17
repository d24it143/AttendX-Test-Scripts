
# AttendX Attendance Test Script

def test_mark_attendance():
    student_id = "STU101"
    subject = "Software Testing"

    if student_id and subject:
        print("PASS: Attendance details are provided.")
    else:
        print("FAIL: Attendance details are missing.")


def test_missing_student_id():
    student_id = ""
    subject = "Software Testing"

    if not student_id:
        print("PASS: Missing student ID detected.")
    else:
        print("FAIL: Student ID validation failed.")


test_mark_attendance()
test_missing_student_id()
