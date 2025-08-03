from flask import Flask, render_template, request, redirect
import sqlite3
from flask import session

app = Flask(__name__)

app.secret_key = "2010"  # Қалауыңа сай өзгерте бер

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form["password"] == "2010":  # ← өзіңнің паролің
            session["logged_in"] = True
            return redirect("/admin")
        else:
            return "❌ Қате пароль!"
    return '''
    <form method="POST" style="max-width:300px;margin:100px auto;text-align:center;">
      <input type="password" name="password" class="form-control mb-3" placeholder="Пароль" />
      <button type="submit" class="btn btn-primary">Кіру</button>
    </form>
    '''

@app.route('/logout')
def logout():
    session.pop("logged_in", None)
    return redirect("/")



def get_db_connection():
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    countries = conn.execute('SELECT * FROM countries').fetchall()
    conn.close()
    return render_template('public.html', countries=countries)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get("logged_in"):
        return redirect("/login")

    conn = get_db_connection()

    if request.method == 'POST':
        action = request.form.get("action")

        # Өшіру
        delete_id = request.form.get("delete_id")
        if delete_id:
            conn.execute('DELETE FROM countries WHERE id = ?', (delete_id,))
            conn.commit()
            return redirect('/admin')

        # Қосу
        if action == "add":
            name = request.form.get("name")
            code = request.form.get("code")
            flag = request.form.get("flag")
            price = request.form.get("price")
            conn.execute('INSERT INTO countries (name, code, flag, price) VALUES (?, ?, ?, ?)', (name, code, flag, price))
            conn.commit()
            return redirect('/admin')

        # Жаңарту
        if action == "update":
            for key, value in request.form.items():
                if key.startswith("price_"):
                    id = key.split("_")[1]
                    conn.execute('UPDATE countries SET price = ? WHERE id = ?', (value, id))
            conn.commit()
            return redirect('/admin')

    countries = conn.execute('SELECT * FROM countries').fetchall()
    conn.close()
    return render_template('admin.html', countries=countries)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)