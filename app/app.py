from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ['MYSQL_HOST'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE']
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        project_name = request.form['project_name']
        manager = request.form['manager']
        developer = request.form['developer']
        tester = request.form['tester']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        notes = request.form['notes']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO projects (project_name, manager, developer, tester, start_date, end_date, notes)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (project_name, manager, developer, tester, start_date, end_date, notes))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
