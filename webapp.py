from flask import Flask, render_template,request,flash, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ='Game'
mysql= MySQL(app)
	
	



@app.route("/show")
def show ():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT game_name FROM game where id = 1''')
	rv = cur.fetchone()
	
	return str((rv)[0]), render_template('show_all.html')
	
@app.route("/show2")
def show2 ():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT game_name FROM game where id = 2''')
	rv = cur.fetchone()
	
	return str((rv)[0]), render_template('show_all.html')

@app.route("/show3")
def show3 ():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT game_name FROM game where id = 3''')
	rv = cur.fetchone()
	
	return str((rv)[0]), render_template('show_all.html')
	
@app.route("/show4")
def show4 ():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT game_name FROM game where id = 4''')
	rv = cur.fetchone()
	
	return str((rv)[0]), render_template('show_all.html')
	

@app.route("/show5")
def show5 ():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT game_name FROM game where id = 5''')
	rv = cur.fetchone()
	
	return str((rv)[0]), render_template('show_all.html')


 



@app.route("/")
def root ():
	return app.send_static_file("index.html")
	
	


	
		  
	
	
@app.route("/unchart4")
def name():
    return render_template('unchart.html')

@app.route("/forza")
def name2():
    return render_template('forza.html')
	
@app.route("/inside")
def name3():
    return render_template('inside.html')

@app.route("/tomb")
def name4():
    return render_template('tomb.html')
	
@app.route("/battlefield")
def name5():
    return render_template('battlefield1.html')

	
@app.route("/outwatch")
def name7():
    return render_template('outwatch.html')
	
@app.route("/sun")
def name6():
    return render_template('poke.html')
	
@app.route("/zelda")
def new1():
    return render_template('zelda.html')
	
@app.route("/god")
def new2():
    return render_template('god.html')
	
@app.route("/resident")
def new3():
    return render_template('resident.html')

@app.route("/gran")
def new4():
    return render_template('gran.html')

@app.route("/tekken")
def new5():
    return render_template('tekken.html')

@app.route("/red")
def new6():
    return render_template('red.html')
	
	
	
	
@app.route("/switch")
def switch():
    return render_template('switch.html')

@app.route("/sales")
def sales():
    return render_template('sales.html')

@app.route("/hide")
def hide():
    return render_template('hide.html')	
	
@app.route("/hide2")
def hide2():
    return render_template('hide.html')

@app.route("/hide3")
def hide3():
    return render_template('hide.html')	

@app.route("/hide4")
def hide4():
    return render_template('hide.html')		




	

	
if __name__ == "__main__": 
	app.run(debug = True)
