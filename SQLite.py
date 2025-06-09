from flask import Flask,render_template,request
import sqlite3 as sql

app = Flask(__name__)



import sqlite3

conn = sqlite3.connect("database.db")  
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS studentsWorld (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        addr TEXT NOT NULL,
        city TEXT NOT NULL,
        pin TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
print("Table created successfully.")


@app.route('/sql')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('studentsql.html')

@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method=='POST':
        try:
            nm=request.form['nm']
            addr=request.form['add']
            city=request.form['city']
            pin=request.form['pin']
            with sql.connect("database.db") as con:
                cur=con.cursor()
                cur.execute("INSERT INTO studentsWorld (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin))
                con.commit()
                msg="Record successfully added"
        except:
            con.rollback()
            msg="error in insert operation"    
        finally:
            return render_template("resultsql.html",msg=msg)
            con.close()
@app.route('/list')
def list():                    
    con=sql.connect("database.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from studentsWorld")
    rows=cur.fetchall();
    return render_template("listsql.html",rows=rows)


if __name__=="__main__":
    app.run(debug=True)
