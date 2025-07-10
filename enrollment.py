from db.db_config import get_connection

def enroll_student(reg_no, course_id,enrollment_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO enrollment (reg_no, course_id,enrollment_date) VALUES (%s, %s,%s)", (reg_no, course_id,enrollment_date))
    conn.commit()
    conn.close()

def view_enrollments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.name, c.name FROM enrollment e
        JOIN students s ON e.reg_no = s.reg_no
        JOIN courses c ON e.course_id = c.course_id
    """)
    for row in cursor.fetchall():
        print(f"Student: {row[0]}, Course: {row[1]}")
    conn.close()
