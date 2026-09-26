import flask
import sqlite3

# only needed for deployment because db may be modified
import TASK4_1

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/process_form/', methods=['POST'])
def process_form():
    form_data = flask.request.form # dictionary

    db = sqlite3.connect('SHENZHENGO.db')
    db.execute('''
        UPDATE Student
        SET Room_ID = ?
        WHERE Student_Name = ?
    ''', (form_data['room_id'], form_data['name']))
    db.commit()
    db.close()
    
    return flask.render_template('index.html', message = 'update successful!')

@app.route('/display/')
def display():
    db = sqlite3.connect('SHENZHENGO.db')
    cursor = db.execute('''
        SELECT Student_Name, Student_Gender, Student_Leader, Room_ID
        FROM Student
        ORDER BY Room_ID ASC
    ''')
    data = cursor.fetchall()
    db.close()

    return flask.render_template('display.html', data=data)

@app.route('/refresh/')
def refresh():
    TASK4_1.create_tables()
    
    return flask.render_template('index.html') 

# only for deploying on Google Cloud (so that you can preview online
app.run('0.0.0.0', port=8080)

# to run on your local machine, use this
# app.run()
