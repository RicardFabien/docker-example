# from __future__ import absolute_import

import json
from sqlite3 import Cursor
from types import SimpleNamespace
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO,emit,send
import mysql.connector


app = Flask(__name__)
app.config["SECRET"] = "I'm a secret"
socket_io = SocketIO(app, cors_allowed_origins="*")
CORS(app, support_credentials=True)


# @app.route('/')
# def test():

#     cnx = mysql.connector.connect(user='root', password='root',host='database',database ="test")

#     value = "no database"

#     cursor:Cursor = cnx.cursor(buffered=True)
#     cursor.execute("SELECT * FROM COMMENTS")

#     value=cursor.fetchall()

#     cursor.close()
#     cnx.close()
#     return jsonify(value)

@socket_io.on("connect")
def handle_connect(message):

    cnx = mysql.connector.connect(user='root', password='root',host='database',database ="test")

    value = "no database"

    cursor:Cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM COMMENTS")

    value=cursor.fetchall()

    cursor.close()
    cnx.close()
     
    emit("init", value)


@socket_io.on("message")
def handle_message(message):
    # cnx = mysql.connector.connect(user='root', password='root',host='database',database ="test")
    # cursor:Cursor = cnx.cursor()
    # cursor.execute("insert into COMMENT (username, value) values (%s, %s)",(message.username, message.comment))
    # cursor.close()
    # cnx.close()

    send(message, broadcast=True)


if __name__ == "__main__":
    socket_io.run(app,host="0.0.0.0", debug=True,port=8080,allow_unsafe_werkzeug=True)