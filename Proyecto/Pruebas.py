import pymysql

conn = pymysql.connect(host="localhost", user="ErikTamaño", password="admin123", db="hr")
db = conn.cursor()
loc_id = 1700
"SELECT e.employee_id, e.first_name, e.last_name, d.department_name from employees e inner join departments d on e.department_id = d.department_id"
def setIdGame():
    query = "SELECT max(department_id) from departments"
    db.execute(query)
    data = db.fetchall()
    return data[0][0] + 1

print(setIdGame())