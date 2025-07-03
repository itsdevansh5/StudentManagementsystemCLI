from db.db_config import get_connection

def add_student(name,reg_no,DOB,gender,address,Mob):
    conn=get_connection
    cursor=conn.cursor
    cursor.execute("Insert into students values (%s,%s,%s,%s,%s,%s)",(name,reg_no,DOB,gender,address,Mob))
    conn.commit()
    cursor.close()
    conn.close()
def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def delete_student(reg_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (reg_no,))
    conn.commit()
    conn.close()    