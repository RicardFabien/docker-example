from sqlite3 import Cursor
from flask import Flask
from flask import jsonify
import mysql.connector




app = Flask(__name__)

@app.route('/')
def hello():
    cnx = mysql.connector.connect(user='root', password='root',host='database',database ="test")
    
    cursor:Cursor = cnx.cursor()
    cursor.execute("SELECT name FROM NAMES where id=1")

    value=cursor.fetchone()

    cursor.close()
    cnx.close()

    return jsonify({"name":value})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=80)