from sqlite3 import Cursor
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import mysql.connector




app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/api')
@cross_origin(supports_credentials=True)
def hello():
    cnx = mysql.connector.connect(user='root', password='root',host='database',database ="test")
    
    cursor:Cursor = cnx.cursor()
    cursor.execute("SELECT name FROM NAMES where id=1")

    value=cursor.fetchone()

    cursor.close()
    cnx.close()

    return jsonify({"name":"CORS on"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=8080)