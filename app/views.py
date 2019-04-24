from app import app
from flask import jsonify, Flask, request
from flask import render_template 
import pymysql as sql

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def     route_index():
        return render_template('index.html', title="Bienvenue !")



@app.route('/user/<username>', methods=['POST'])
def     route_add_user(username):
    return "User added!\n"   

@app.route('/user')
def     route_all_user():
    result = ""
    try:
        connect = sql.connect(host='localhost',
                              unix_socket='path_to_our_mysql_socket',
                              user='_user',
                              passwd='_password',
                              db='name_of_your_database'
                            )
        cursor = connect.cursor()
        cursor.execute("SELECT * from user")
        result = cursor.fetchall()
        cursor.close()
        connect.close()
    except Exception as e :
            print("Caught an exception : ", e)
    return jsonify(result)
