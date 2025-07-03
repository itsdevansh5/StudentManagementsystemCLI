from db.db_config import get_connection

def add_course(name, course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (name, course_id) VALUES (%s, %s)", (name, course_id))
    conn.commit()
    conn.close()

def view_courses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    for row in cursor.fetchall():
        print(row)
    conn.close()
