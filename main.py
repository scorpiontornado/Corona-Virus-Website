from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)
current = "/"
last = []


def table():
    try:
        curs.execute("DROP TABLE infected;")
        print("Table dropped")
    except:
        print("Table doesn't exist, so it wasn't dropped.")

    curs.execute("CREATE TABLE infected(person_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name, surname, age, cob, coi, status, quarantined INTEGER);")
    print("Table created")


def execute(command):
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute(command)

    return cur.fetchall()


def back(cur=""):
    # if last[-1] in last, then
    global current
    global last

    try:
        if not(cur):
            last = []
            current = "/"
        elif last[-1] in last and not len(last) < 2:
            last.pop(-1)
        else:
            last.append(current)
            current = cur
    except IndexError:
        last.append(current)
        current = cur

    print(f"current = {current}, last = {last}")


# connect to a database
# if it doesn't exist the code will make the db
# if it does exist it will connect to it
con = sql.connect('database.db')
# need a cursor to loop through the stuff in the database
curs = con.cursor()
# table()
# commit means to save the thing you just did, it's good for avoiding errors
con.commit()
# you need to close a connection to the database at the end
con.close()


@app.route('/')
def home():
    back()

    return render_template('home.html', heading="Home", current=current)


@app.route('/enternew')
def enternew():
    back("/enternew")
    return render_template('enternew.html', heading="Enter New Person", current=current, last=last[-1])


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            # person_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name, surname, age, cob, coi, status, quarantined INTEGER
            fn = request.form['fn']
            sn = request.form['sn']
            age = request.form['age']
            cob = request.form['cob']
            coi = request.form['coi']
            status = request.form['status']
            quar = request.form['quar']
            row_data = (fn, sn, age, status, quar)
            print(row_data)

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute(f"""INSERT INTO infected (first_name, surname, age, cob, coi, status, quarantined) VALUES(?,?,?,?,?,?,?);""",
                            (fn, sn, age, cob, coi, status, quar))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    back("/list")

    rows = execute(
        "select first_name, surname, age, cob, coi, status, quarantined from infected")
    for row in rows:
        print(row["quarantined"])
    return render_template("list.html", heading="List of People", current=current, last=last[-1], rows=rows)


@app.route('/stats/home')
def sHome():
    back("/stats/home")

    return render_template('stats/home.html', heading="Statistics - home", current=current, last=last[-1])


@app.route('/stats/countries')
def sCountries():
    back("/stats/countries")

    rows = execute(
        "SELECT coi, count(coi) FROM infected GROUP BY coi ORDER BY count(coi) DESC, coi")

    return render_template("stats/countries.html", heading="Countries", current=current, last=last[-1], rows=rows)


@app.route('/stats/ages')
def sAges():
    back("/stats/ages")

    rows = execute(
        "SELECT age, count(age) FROM infected GROUP BY age ORDER BY count(age) DESC, age")

    return render_template("stats/ages.html", heading="Ages", current=current, last=last[-1], rows=rows)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# 141 lines w/o execute or back funcs, 134 w/ execute, 120 w/ execute + back (w/o list or home), 131 w/ list and home